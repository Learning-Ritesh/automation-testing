from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from login import login_to_medtransgo
import time

driver, wait = login_to_medtransgo()

try:
    wait.until(EC.url_to_be("https://admin-v3-test.medtransgo.com/"))
    print("Logged in and landed on dashboard")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Admin']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Billing Code Management']"))).click()

    wait.until(EC.url_contains("/billing-codes"))
    print("Reached Billing Code Management page")

    # Scroll to and click "Create New Billing Code"
    create_btn = wait.until(EC.presence_of_element_located((
        By.XPATH, "//p[text()='Create New Billing Code']/parent::div"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", create_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", create_btn)
    print("Clicked 'Create New Billing Code'")

    # Fill input fields
    fields = {
        "Code": "A1123",
        "Name": "Transportation",
        "Description": "Test Transportation",
        "Base Charge": "5",
        "Per Unit Charge": "5",
        "Quantity Per Unit": "5",
        "Free Units": "5",
        "Waiting Charge Per Unit": "5",
        "Per Included Waiting Units": "5",
        "Minimum Units": "5",
        "Peak Hours Base Charge": "5",
        "Peak Hours Unit Charge": "5",
        "Cancellation Fee": "200"
    }

    for label, value in fields.items():
        input_el = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{label}']/following-sibling::div//input")))
        input_el.clear()
        input_el.send_keys(value)

    # Select dropdowns
    dropdowns = {
        "Request Type": "Transportation",
        "Service Type": "Stretcher"
    }

    for label, option_text in dropdowns.items():
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[text()='{label}']/following-sibling::div")))
        dropdown.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{option_text}']"))).click()

    # Select "Miles" radio button for Unit
    unit_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Unit')]/following::label[contains(., 'Miles')][1]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", unit_radio)
    unit_radio.click()

    # Fill in time range
    start_time = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='hh:mm aa'])[1]")))
    start_time.clear()
    start_time.send_keys("08:00 AM")

    end_time = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='hh:mm aa'])[2]")))
    end_time.clear()
    end_time.send_keys("10:00 AM")

    # Select "Absolute" for Pricing Type
    pricing_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Pricing Type']/following::label[contains(., 'Absolute')][1]")))
    pricing_radio.click()

    # Click Save button using JS
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Save']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", save_btn)

    # Confirm success
    success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Billing code created successfully')]")))
    print("Billing code created successfully!")

except Exception as e:
    print("Something went wrong:", str(e))

finally:
    time.sleep(5)
    driver.quit()
