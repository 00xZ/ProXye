from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

# Set Chrome options to run in headless mode
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

options.add_argument("--headless")  # Run without GUI
options.add_argument("--no-sandbox")  # Disable sandbox for running in restricted environments
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in some environments

# Manually set the ChromeDriver path if necessary
service = Service('/usr/bin/chromedriver')  # Provide the path to chromedriver manually
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Navigating to URL...")
    # Navigate to Spys.one
    urls = ["http://spys.one/en/", "http://spys.one/fr/"]
    random_url = random.choice(urls)
    url = random_url
    #url = "http://spys.one/en/"
    driver.get(url)
    
    # Wait for the page to load and elements to be visible
    WebDriverWait(driver, 31).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//tr[@class="spy1xx"]//font[@class="spy14"]')
    ))

    print("Page loaded. Extracting proxy data...")
    # Extract proxy data
    proxies = driver.find_elements(By.XPATH, '//tr[@class="spy1xx"]//font[@class="spy14"]')
    
    if not proxies:
        print("No proxies found.")
    else:
        for proxy in proxies:
            print(proxy.text)
except TimeoutError as te:
    print(f"Timeout error occurred: {te}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Closing the driver.")
    driver.quit()
