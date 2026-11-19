#!/usr/bin/env node
// Encrypts the LaurAmolDay chapter: ordered photos + story text, AES-256-GCM,
// key = PBKDF2-SHA256(lowercased password). Only ciphertext is committed.
// Usage: CHAPTER_PASSWORD=… node scripts/encrypt_lauramolday.js <story.json> <photo-dir> <out-dir>
// story.json: { hero: "<file>", frames: [{ file, chapter, title, time }], ... }
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const [storyPath, photoDir, outDir] = process.argv.slice(2);
const password = process.env.CHAPTER_PASSWORD;
if (!storyPath || !photoDir || !outDir || !password) {
  console.error("Usage: CHAPTER_PASSWORD=… node scripts/encrypt_lauramolday.js <story.json> <photo-dir> <out-dir>");
  process.exit(1);
}

const iterations = 310000;
const salt = crypto.randomBytes(16);
const key = crypto.pbkdf2Sync(password.trim().toLocaleLowerCase("en-US"), salt, iterations, 32, "sha256");
const seal = (buf) => {
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv("aes-256-gcm", key, iv);
  return { iv, data: Buffer.concat([c.update(buf), c.final(), c.getAuthTag()]) };
};

fs.mkdirSync(outDir, { recursive: true });
const story = JSON.parse(fs.readFileSync(storyPath, "utf8"));
const files = [story.hero, ...story.frames.map((f) => f.file)];
const blobs = {};
for (const name of new Set(files)) {
  const { iv, data } = seal(fs.readFileSync(path.join(photoDir, name)));
  const opaque = `${crypto.createHash("sha256").update(data).digest("hex")}.bin`;
  fs.writeFileSync(path.join(outDir, opaque), data);
  blobs[name] = { file: opaque, iv: iv.toString("base64") };
}

// Story text (captions, chapter names) is encrypted too; the public shell holds no content.
const plainStory = {
  ...story,
  hero: blobs[story.hero],
  frames: story.frames.map((f) => ({ ...f, ...blobs[f.file], type: "image/webp" })),
};
const s = seal(Buffer.from(JSON.stringify(plainStory)));

const manifest = {
  version: 1,
  cipher: "AES-GCM",
  keyDerivation: { name: "PBKDF2", hash: "SHA-256", iterations, salt: salt.toString("base64") },
  story: { iv: s.iv.toString("base64"), data: s.data.toString("base64") },
};
fs.writeFileSync(path.join(outDir, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`Encrypted ${Object.keys(blobs).length} photographs + story into ${outDir}`);
