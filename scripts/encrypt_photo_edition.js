#!/usr/bin/env node

const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const [sourceDir, outputDir] = process.argv.slice(2);
const password = process.env.PHOTO_EDITION_PASSWORD;

if (!sourceDir || !outputDir || !password) {
  console.error(
    "Usage: PHOTO_EDITION_PASSWORD=… node scripts/encrypt_photo_edition.js <source-dir> <output-dir>"
  );
  process.exit(1);
}

const iterations = 310000;
const salt = crypto.randomBytes(16);
const key = crypto.pbkdf2Sync(password.toLocaleLowerCase("en-US"), salt, iterations, 32, "sha256");

fs.mkdirSync(outputDir, { recursive: true });

const sourceFiles = fs
  .readdirSync(sourceDir)
  .filter((name) => /\.(avif|jpe?g|png|webp)$/i.test(name))
  .sort((a, b) => a.localeCompare(b, "en", { numeric: true }));

const images = sourceFiles.map((name, index) => {
  const clear = fs.readFileSync(path.join(sourceDir, name));
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
  const encrypted = Buffer.concat([cipher.update(clear), cipher.final(), cipher.getAuthTag()]);
  const opaqueName = `${crypto.createHash("sha256").update(encrypted).digest("hex")}.bin`;

  fs.writeFileSync(path.join(outputDir, opaqueName), encrypted);

  return {
    id: String(index + 1).padStart(2, "0"),
    file: opaqueName,
    iv: iv.toString("base64"),
    type: mimeType(name),
  };
});

const manifest = {
  version: 1,
  cipher: "AES-GCM",
  keyDerivation: {
    name: "PBKDF2",
    hash: "SHA-256",
    iterations,
    salt: salt.toString("base64"),
  },
  images,
};

fs.writeFileSync(path.join(outputDir, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`Encrypted ${images.length} images into ${outputDir}`);

function mimeType(name) {
  const extension = path.extname(name).toLowerCase();
  return {
    ".avif": "image/avif",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
  }[extension];
}
