from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from dotenv import load_dotenv
import os

user_agents = [
    'HTC: Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
    'Google Nexus: Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
    'Samsung Galaxy Note 4: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    'Samsung Galaxy Note 3: Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Samsung Phone: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    'Apple iPad: Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
    'Microsoft Internet Explorer 11 / IE 11: Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Microsoft Internet Explorer 7 / IE 7: Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
    # Add more user agents as needed
]

# Choose a random user agent
random_user_agent = random.choice(user_agents)
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--dns-server=8.8.8.8') 
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 })
driver = webdriver.Chrome(options=chrome_options)
# Open the website
url='https://freebitco.in/signup/?op=s'
driver.get(url)



# Wait for the specific button to appear and click it
try:
    specific_button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.XPATH, "//li[@class='login_menu_button']/a"))
    )
    specific_button.click()
    print('Login menu button clicked')
except:
    print("Specific button not found or not clickable")

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
email_field = driver.find_element('id','login_form_btc_address')
email_field.send_keys(email)
password_field = driver.find_element('id', 'login_form_password')
password_field.send_keys(password)

# Submit the login form
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login_button"))
    )
    login_button.click()
    print("LOGIN button clicked")
except:
    print("LOGIN button not found or not clickable")
time.sleep(5)

# Wait for the checkbox to appear and click it
try:
    iframe_element = driver.find_element(By.XPATH, '//iframe[contains(@src, "https://newassets.hcaptcha.com/captcha")]')
    # Switch to the iframe
    driver.switch_to.frame(iframe_element)
    #  interact with elements inside the iframe
    checkbox_element = driver.find_element(By.XPATH, '//*[@id="checkbox"]')
    checkbox_element.click()
    print("Captcha found and clicked")
except Exception as e:
    print("Captcha not found or not clickable:", str(e))

# Click on the roll button
try:
    roll_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'free_play_element'))
    )
    driver.execute_script("arguments[0].click();", roll_button_element)
    print("Roll Button clicked")
except:
    print("Roll Button not found or not clickable")

time.sleep(500)
# Close the browser
driver.quit()
