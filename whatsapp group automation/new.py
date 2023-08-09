from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.service import Service

# Set the path to the chromedriver executable
PATH = "C:/Program Files (x86)/chromedriver-win64/chromedriver.exe"

# Initialize the Chrome webdriver with the specified path
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com/")
time.sleep(80)

# Click on the new chat button
new_chat_button = driver.find_element(By.XPATH, "//div[@title='Menu']")
new_chat_button.click()

# Click on the new group option
new_group_option = driver.find_element(By.XPATH, "//div[@aria-label='New group']")
new_group_option.click()


time.sleep(2)

# Add contacts to the group
contact_search_box = driver.find_element(By.XPATH, "//div[@data-testid='list-item-10']")
time.sleep(2)
contact_search_box.click()


# Click the next button
next_button = driver.find_element(By.XPATH, "//div[@data-testid='group-participants-btn']")
next_button.click()

# Enter group subject
group_subject = driver.find_element(By.XPATH, "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
group_subject.send_keys("new Group")

# Click the create button
create_button = driver.find_element(By.XPATH, "//div[@aria-label='Create group']")
create_button.click()

time.sleep(20)

# Quit the webdriver
driver.quit()
