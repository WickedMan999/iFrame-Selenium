from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables
base_url = "https://selectorshub.com/iframe-scenario/"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Wait Timer
wait = WebDriverWait(driver, 20)

# Open URL
driver.get(base_url)
driver.implicitly_wait(30)

# ------------------------------------------------- Same origin Iframe: iframe 1 -------------------------------------------------------- #
# Wait until first iframe is visible
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//iframe[@id='pact1']")))

# Locate iframe1 once it is visible
iframe_1 = driver.find_element(
    By.XPATH, "//iframe[@id='pact1']")
print("First iframe visible")

# Switch to iFrame1
driver.switch_to.frame(iframe_1)
print("Switched to 1st iframe")

# Enter text on iframe1 text box
first_crush = driver.find_element(By.CSS_SELECTOR, "#inp_val")
first_crush.send_keys("Keti")

time.sleep(2)

# ---------------------------------------------- Same origin Iframe: iframe 2 (nested) -------------------------------------------------- #
# Wait until second iframe is visible
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//iframe[@id='pact2']")))

# Locate iframe2 once it is visible
iframe_2 = driver.find_element(
    By.XPATH, "//iframe[@id='pact2']")
print("Second iframe is visible")

# Switch to iFrame2
driver.switch_to.frame(iframe_2)
print("Switched to 2nd iframe")

# Enter text on iframe2 text box
first_crush = driver.find_element(By.CSS_SELECTOR, "#jex")
first_crush.send_keys("Keti Part 2")

time.sleep(2)

# ---------------------------------------------- Same origin Iframe: iframe 3 (nested) -------------------------------------------------- #
# Wait until second iframe is visible
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//iframe[@id='pact3']")))

# Locate iframe3 once it is visible
iframe_3 = driver.find_element(
    By.XPATH, "//iframe[@id='pact3']")
print("Third iframe is visible")

# Switch to iFrame3
driver.switch_to.frame(iframe_3)
print("Switched to 3rd iframe")

# Enter text on iframe3 text box
first_crush = driver.find_element(By.CSS_SELECTOR, "#glaf")
first_crush.send_keys("Keti Part 3")

time.sleep(5)
