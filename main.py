from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

item_search = "Blue partyhat"
item = ""

# Load selenium web browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Navigate to website
driver.get("https://secure.runescape.com/m=itemdb_oldschool/")

# Allow cookies
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# Search for item
search = driver.find_element_by_name("query")
search.send_keys(item_search)
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "results-table"))
    )
    # item = main.text + "\n"

    driver.find_element_by_link_text(item_search).click()
    stats = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "stats"))
    )
    item_description = driver.find_element_by_class_name("item-description")
    stats = driver.find_element_by_class_name("stats")

    item += item_description.text + "\n \n"
    item += stats.text
finally:
    driver.quit()

print(item)

