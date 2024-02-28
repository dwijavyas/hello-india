from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
#driver.get("http://www.google.com")

#driver.find_element(By.ID,'email')
driver.find_element(By.CLASS_NAME,'MV3Tnb').click()
driver.quit()
