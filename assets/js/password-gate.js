(function passwordGate() {
  var PASSWORD = 'Morrissey';
  var SESSION_KEY = 'tp_access_session_v2';
  var DEVICE_KEY = 'tp_access_device_v2';
  var DEVICE_TTL_MS = 30 * 24 * 60 * 60 * 1000; // 30 days

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
      if (typeof parsed.grantedAt !== 'number') {
        return null;
      }
      if (typeof parsed.expiresAt !== 'number') {
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
      if (record.expiresAt <= record.grantedAt) {
        window.localStorage.removeItem(DEVICE_KEY);
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
      var grantedAt = now();
      window.localStorage.setItem(
        DEVICE_KEY,
        JSON.stringify({
          grantedAt: grantedAt,
          expiresAt: grantedAt + DEVICE_TTL_MS
        })
      );
    } catch (error) {
      // Local storage unavailable.
    }
  }

  function denyAccess() {
    document.documentElement.innerHTML = '<body style="margin:0;display:grid;place-items:center;min-height:100vh;font-family:system-ui,sans-serif;background:#000;color:#fff;">Access cancelled.</body>';
    throw new Error('Access cancelled by user');
  }

  var sessionAccess = hasSessionAccess();
  var deviceAccess = hasDeviceAccess();

  if (sessionAccess || deviceAccess) {
    if (deviceAccess) {
      try {
        window.sessionStorage.setItem(SESSION_KEY, 'true');
      } catch (error) {
        // Ignore session storage failure.
      }
    }
    return;
  }

  while (true) {
    var entry = window.prompt('Enter password to view this site:');

    if (entry === null) {
      denyAccess();
    }

    if (entry === PASSWORD) {
      grantAccess();
      return;
    }

    window.alert('Incorrect password. Try again.');
  }
})();
