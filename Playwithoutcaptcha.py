from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
from dotenv import load_dotenv
import os

user_agents = [
    'HTC: Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
    'Google Nexus: Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
    # Add more user agents as needed
]

# Choose a random user agent
random_user_agent = random.choice(user_agents)
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--dns-server=8.8.8.8')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

# Check if cookies are saved from a previous session
try:
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
except FileNotFoundError:
    cookies = None

driver = webdriver.Chrome(options=chrome_options)

if cookies:
    # Load cookies if available
    driver.get("https://freebitco.in")  # Open any URL to set domain
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

else:
    # Open the website
    url = 'https://freebitco.in/signup/?op=s'
    driver.get(url)

    # Wait for the specific button to appear and click it
    try:
        specific_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='login_menu_button']/a"))
        )
        specific_button.click()
        print('Login menu button clicked')
    except:
        print("login menu button not found or not clickable")

   
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    email_field = driver.find_element('id', 'login_form_btc_address')
    email_field.send_keys(email)
    password_field = driver.find_element('id', 'login_form_password')
    password_field.send_keys(password)

    # Submit the login form
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login_button"))
        )
        login_button.click()
        print('Login button clicked')
    except:
        print("LOGIN button not found or not clickable")
        time.sleep(5)

        # Save cookies after successful login
        with open('cookies.json', 'w') as file:
            json.dump(driver.get_cookies(), file)
            print('Cookies saved')

    # Wait for the checkbox to appear and click it
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")        
# Assuming driver is already defined and the page is loaded
try:
    play_without_captchas_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()=" PLAY WITHOUT CAPTCHA "]'))
    )
    play_without_captchas_button.click()
    print("Play Without Captchas Button clicked")
except:
    print("Play Without Captchas Button not found or not clickable")

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