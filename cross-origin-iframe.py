from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Variables
base_url = "https://selectorshub.com/xpath-practice-page/"

# Customize Firefox Before It Opens
firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--start-maximized")
firefox_options.add_argument("--incognito")

# Opens Firefox Browser
driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()

# Wait Timer
wait = WebDriverWait(driver, 20)

# Open URL
driver.get(base_url)
driver.implicitly_wait(30)

# Wait until iframe is presence
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//iframe[@id='coming google']")))

# Locate iframe once it is presence
iframe = driver.find_element(
    By.XPATH, "//iframe[@id='coming google']")
print("iframe located successfully")

# Switch to iFrame
driver.switch_to.frame(iframe)
print("Switch to iframe successfully")

time.sleep(2)

# Locate button and click button
button = driver.find_element(
    By.CSS_SELECTOR, "body > div:nth-child(8) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1)")

button.click()
print("Button Clicked")

time.sleep(5)

# Quit Browser
driver.quit()
