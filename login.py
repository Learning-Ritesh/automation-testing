from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_medtransgo():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    driver.get("https://admin-v3-test.medtransgo.com")

    wait.until(EC.url_contains("/login"))
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        if "Proceed To Log In" in button.text:
            driver.execute_script("arguments[0].click();", button)
            break

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("aniketpatil9929@gmail.com")

    next_buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in next_buttons:
        if btn.text.strip().lower() == "next":
            driver.execute_script("arguments[0].click();", btn)
            break

    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("aA@325325")

    continue_buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in continue_buttons:
        if btn.text.strip().lower() == "continue":
            driver.execute_script("arguments[0].click();", btn)
            break

    wait.until_not(EC.url_contains("/login"))

    print("Logged in successfully")

    return driver, wait  
