PUSH_NOTIFICATIONS_SETTINGS = {
    "CONFIG": "push_notifications.conf.AppConfig",
    "APPLICATIONS": {
        "xyz.celuv.celuv": {
            "PLATFORM": "APNS",
            "CERTIFICATE": os.path.join(BASE_DIR, 'apns.pem'),
            "TOPIC": "xyz.celuv.celuv",
            "USE_SANDBOX": False,
        },
    },
}