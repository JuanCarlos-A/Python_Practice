from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys


# options = webdriver.ChromeOptions()

# options.add_experimental_option("detach", True)

browser = webdriver.Chrome()

browser.implicitly_wait(10)

browser.get("https://github.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")

link.click()



user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")


user_input.send_keys(os.environ.get("GH_USER"))
pass_input.send_keys(os.environ.get("GH_PASS"))

pass_input.send_keys(Keys.RETURN)



link_2 = browser.find_element(By.LINK_TEXT, "Verify")
link_2.click()

verify_code = browser.find_element(By.ID, "app_totp")

verify_code.send_keys("916671")
verify_code.send_keys(Keys.RETURN)


profile = browser.find_element(By.CLASS_NAME, "elemento_con_nombre")

label =profile.get_attribute("innerHTML")

assert "JuanCarlos-A" in label

browser.quit()