URLS = {
    'https://www.code0x378.com': 'Jeff',  # The control
    'https://www.amazon.com/primepantry': 'Pantry is temporarily closed',  # Bastards
}

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = "tacotim@example.com"
EMAIL_HOST_PASSWORD = "password1"
EMAIL_USE_TLS = True
EMAIL_TO = "tacotim@example.com"
EMAIL_FROM = "admin@example.com"

DELAY_BETWEEN_CHECKS = 300
DELAY_BETWEEN_URLS_MIN = 3
DELAY_BETWEEN_URLS_MAX = 10

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
