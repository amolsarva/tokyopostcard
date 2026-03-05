(function passwordGate() {
  var SESSION_KEY = 'tp_access_granted_v1';
  var REQUIRED_PASSWORD = 'Morrissey';

  try {
    if (window.sessionStorage.getItem(SESSION_KEY) === 'true') {
      return;
    }
  } catch (error) {
    // Continue to prompt if sessionStorage is unavailable.
  }

  var attempts = 0;
  while (true) {
    var entry = window.prompt('Enter password to view this site:');
    if (entry === REQUIRED_PASSWORD) {
      try {
        window.sessionStorage.setItem(SESSION_KEY, 'true');
      } catch (error) {
        // Ignore storage failures; access remains for this page lifetime.
      }
      return;
    }

    attempts += 1;
    if (entry === null && attempts >= 1) {
      document.documentElement.innerHTML = '<body style="margin:0;display:grid;place-items:center;min-height:100vh;font-family:system-ui,sans-serif;background:#000;color:#fff;">Access cancelled.</body>';
      throw new Error('Access cancelled by user');
    }

    window.alert('Incorrect password. Try again.');
  }
})();
