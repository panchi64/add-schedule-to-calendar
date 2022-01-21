from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys as press_key
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import WebDriverException

# Get the directory for the python file
parent_dir = __file__.replace("s2c.py", "")

# Open the old UPRM portal with selenium
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://home.uprm.edu/")
assert "LOGIN" in browser.title

# Wait for the user to log in (timeout of 10 mins)
WebDriverWait(browser, 600).until(EC.url_contains("home.php"))
assert "My Home" in browser.title

# Direct the user into the schedule page
browser.find_element(by=By.XPATH,value='//*[@title="Services for Students"]').click()
assert "Estudiantes" in browser.title

browser.find_element(by=By.XPATH,value='//*[@title="Matricula"]').click()
assert "Matrícula" in browser.title

browser.find_element(by=By.CSS_SELECTOR,value="a[href*='matricula/appviewmtr.php']").click()
assert "Clases Matriculadas" in browser.title