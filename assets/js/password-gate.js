(function passwordGate() {
  var SESSION_KEY = 'naiy_access_session_v3';
  var DEVICE_KEY = 'naiy_access_device_v3';
  var DEVICE_TTL_MS = 90 * 24 * 60 * 60 * 1000;
  var HASH_SALT_HEX = '3b9ededaa5d836767826a0f0b582a17d';
  var HASH_ITERATIONS = 210000;
  var HASH_HEX = 'd5fc2125162bc8d4b06fc03718d1625d1b08322f1c829d5a650b1e900f2c4376';
  var currentScript = document.currentScript;
  var mode = currentScript && currentScript.dataset.passwordGate ? currentScript.dataset.passwordGate : 'overlay';

  function now() {
    return Date.now();
  }

  function parseRecord(raw) {
    if (!raw) {
      return null;
    }

    try {
      var parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== 'object') {
        return null;
      }
      if (typeof parsed.grantedAt !== 'number' || typeof parsed.expiresAt !== 'number') {
        return null;
      }
      return parsed;
    } catch (error) {
      return null;
    }
  }

  function hasSessionAccess() {
    try {
      return window.sessionStorage.getItem(SESSION_KEY) === 'true';
    } catch (error) {
      return false;
    }
  }

  function hasDeviceAccess() {
    try {
      var record = parseRecord(window.localStorage.getItem(DEVICE_KEY));
      if (!record) {
        return false;
      }
      if (record.expiresAt < now()) {
        window.localStorage.removeItem(DEVICE_KEY);
        return false;
      }
      return true;
    } catch (error) {
      return false;
    }
  }

  function grantAccess() {
    try {
      window.sessionStorage.setItem(SESSION_KEY, 'true');
    } catch (error) {
      // Session storage unavailable.
    }

    try {
      window.localStorage.setItem(
        DEVICE_KEY,
        JSON.stringify({
          grantedAt: now(),
          expiresAt: now() + DEVICE_TTL_MS
        })
      );
    } catch (error) {
      // Local storage unavailable.
    }
  }

  function hexToBytes(hex) {
    var bytes = new Uint8Array(hex.length / 2);
    for (var i = 0; i < hex.length; i += 2) {
      bytes[i / 2] = parseInt(hex.slice(i, i + 2), 16);
    }
    return bytes;
  }

  function bytesToHex(bytes) {
    return Array.prototype.map.call(bytes, function toHex(byte) {
      return byte.toString(16).padStart(2, '0');
    }).join('');
  }

  function secureCompare(a, b) {
    if (a.length !== b.length) {
      return false;
    }

    var mismatch = 0;
    for (var i = 0; i < a.length; i += 1) {
      mismatch |= a.charCodeAt(i) ^ b.charCodeAt(i);
    }
    return mismatch === 0;
  }

  async function derivePasswordHash(password) {
    if (!window.crypto || !window.crypto.subtle) {
      throw new Error('This browser cannot verify the private gate.');
    }

    var encoder = new TextEncoder();
    var keyMaterial = await window.crypto.subtle.importKey(
      'raw',
      encoder.encode(password),
      'PBKDF2',
      false,
      ['deriveBits']
    );
    var bits = await window.crypto.subtle.deriveBits(
      {
        name: 'PBKDF2',
        salt: hexToBytes(HASH_SALT_HEX),
        iterations: HASH_ITERATIONS,
        hash: 'SHA-256'
      },
      keyMaterial,
      256
    );

    return bytesToHex(new Uint8Array(bits));
  }

  async function verifyPassword(password) {
    var derived = await derivePasswordHash(password || '');
    var valid = secureCompare(derived, HASH_HEX);
    if (valid) {
      grantAccess();
    }
    return valid;
  }

  var ready = Promise.resolve(hasSessionAccess() || hasDeviceAccess()).then(function normalizeAccess(hasAccess) {
    if (hasAccess) {
      try {
        window.sessionStorage.setItem(SESSION_KEY, 'true');
      } catch (error) {
        // Ignore session storage failure.
      }
    }
    return hasAccess;
  });

  window.NewAIYorkGate = {
    ready: ready,
    hasAccess: function hasAccess() {
      return hasSessionAccess() || hasDeviceAccess();
    },
    verify: verifyPassword
  };

  function installOverlay() {
    ready.then(function maybeShowOverlay(hasAccess) {
      if (hasAccess) {
        return;
      }

      var overlay = document.createElement('div');
      overlay.className = 'naiy-gate-overlay';
      overlay.innerHTML = [
        '<form class="naiy-gate-panel" autocomplete="off">',
        '<p class="naiy-gate-kicker">NEWAIYORK</p>',
        '<h1>Private</h1>',
        '<label>',
        '<span>Password</span>',
        '<input name="password" type="password" autocomplete="current-password" autofocus />',
        '</label>',
        '<button type="submit">Enter</button>',
        '<p class="naiy-gate-error" role="alert" aria-live="polite"></p>',
        '</form>'
      ].join('');

      var style = document.createElement('style');
      style.textContent = [
        '.naiy-gate-overlay{position:fixed;inset:0;z-index:2147483647;display:grid;place-items:center;padding:24px;background:#050505;color:#fff4ec;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;}',
        '.naiy-gate-panel{width:min(360px,100%);display:grid;gap:16px;padding:24px;border:1px solid rgba(255,244,236,.2);background:rgba(15,15,14,.92);box-shadow:0 24px 90px rgba(0,0,0,.55);}',
        '.naiy-gate-kicker{margin:0;color:rgba(255,244,236,.62);font-size:11px;letter-spacing:.28em;text-transform:uppercase;}',
        '.naiy-gate-panel h1{margin:0;font-size:32px;line-height:1;text-transform:uppercase;}',
        '.naiy-gate-panel label{display:grid;gap:8px;color:rgba(255,244,236,.72);font-size:12px;letter-spacing:.14em;text-transform:uppercase;}',
        '.naiy-gate-panel input{width:100%;border:1px solid rgba(255,244,236,.22);background:#050505;color:#fff4ec;padding:13px 14px;border-radius:0;font:inherit;font-size:16px;letter-spacing:0;text-transform:none;}',
        '.naiy-gate-panel button{border:1px solid rgba(255,244,236,.34);background:#fff4ec;color:#050505;padding:13px 14px;font:inherit;font-weight:700;text-transform:uppercase;letter-spacing:.18em;cursor:pointer;}',
        '.naiy-gate-error{min-height:18px;margin:0;color:#ffb0a3;font-size:13px;}'
      ].join('');

      document.head.appendChild(style);
      document.body.appendChild(overlay);

      var form = overlay.querySelector('form');
      var input = overlay.querySelector('input');
      var error = overlay.querySelector('.naiy-gate-error');
      input.focus();

      form.addEventListener('submit', async function onSubmit(event) {
        event.preventDefault();
        error.textContent = '';
        form.querySelector('button').disabled = true;

        try {
          if (await verifyPassword(input.value)) {
            overlay.remove();
            style.remove();
            return;
          }
          error.textContent = 'That did not open it.';
          input.select();
        } catch (verificationError) {
          error.textContent = verificationError.message;
        } finally {
          form.querySelector('button').disabled = false;
        }
      });
    });
  }

  if (mode !== 'manual') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', installOverlay, { once: true });
    } else {
      installOverlay();
    }
  }
})();
