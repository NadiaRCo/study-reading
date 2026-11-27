// Study Club app helper, loaded by the pages copied in by tools/sync_study_club.py.
// 1. Registers the service worker so the app opens offline.
// 2. Sends reminder pop-ups through the service worker. iPhones only show
//    notifications that way, and only for an app added to the Home Screen.
(function () {
  if (!("serviceWorker" in navigator)) return;
  var ready = navigator.serviceWorker.register("sw.js").then(function () {
    return navigator.serviceWorker.ready;
  }).catch(function () { return null; });

  var Native = window.Notification;
  if (!Native) return;
  function AppNotification(title, options) {
    ready.then(function (reg) {
      if (reg && reg.showNotification) {
        reg.showNotification(title, Object.assign({ icon: "icons/icon-192.png", badge: "icons/icon-192.png" }, options || {}));
      } else {
        try { new Native(title, options); } catch (e) {}
      }
    });
  }
  Object.defineProperty(AppNotification, "permission", { get: function () { return Native.permission; } });
  AppNotification.requestPermission = function (cb) { return Native.requestPermission(cb); };
  try { window.Notification = AppNotification; } catch (e) {}
})();
