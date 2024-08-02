from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

search_engine = webdriver.Chrome(options=chrome_options)

search_engine.get("https://tinder.com/")

# Wait for and accept cookies
WebDriverWait(search_engine, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'))
).click()

# Wait for and click the login button
WebDriverWait(search_engine, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'))
).click()

# Wait for and click the login with Google button
WebDriverWait(search_engine, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb '))
).click()

# Handle Google login if it opens in a new window
time.sleep(3)
base_window = search_engine.window_handles[0]
google_login_window = search_engine.window_handles[1]

search_engine.switch_to.window(google_login_window)

# Wait for email input and enter credentials
WebDriverWait(search_engine, 10).until(
    EC.visibility_of_element_located((By.ID, "identifierId"))
).send_keys("sandaru.20231835@iit.ac.lk", Keys.ENTER)

# Wait for password input and enter credentials
WebDriverWait(search_engine, 10).until(
    EC.visibility_of_element_located((By.NAME, 'Passwd'))
).send_keys("Sandaru_perera", Keys.ENTER)

# Switch back to base window
search_engine.switch_to.window(base_window)

# Wait for and handle location permission buttons if present
try:
    WebDriverWait(search_engine, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))
    ).click()

    WebDriverWait(search_engine, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/div[2]/div[2]'))
    ).click()
except Exception as e:
    print("Location permissions not found or already handled.")

time.sleep(5)
WebDriverWait(search_engine, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[2]/button'))).click()
time.sleep(5)
like_proceed = True

try:
    for n in range(100):
        try:
            WebDriverWait(search_engine, 3).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div'
                                                      '[1]/div[1]/div/div[3]/div/div[4]/button'))).click()
        except ElementClickInterceptedException:
            tinderplus_popup = search_engine.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button')
            tinderplus_popup.click()

        except TimeoutException:
            try:
                WebDriverWait(search_engine, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/'
                                                          'div[1]/div/div[4]/div/div[4]/button'))).click()

            except ElementClickInterceptedException:
                try:
                    tinder_home_screen_not_interested_button = search_engine.find_element(By.XPATH,
                                                                                          '/html/body/div[2]/div/div/div[2]/button[2]')
                    tinder_home_screen_not_interested_button.click()
                except TimeoutException:
                    tinderplus_popup = search_engine.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/button')
                    tinderplus_popup.click()
                    print("No add_to_home_screen button found")
except Exception:
    print("You've reached the maximum amount of likes for the day!!")
    search_engine.quit()
