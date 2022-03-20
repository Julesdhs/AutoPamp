from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome()
driver.get("https://ns3085211.ip-147-135-255.eu/ensai/index.php?p=100")
# Select the id box
id_box = driver.find_element(by=By.ID, value='username')
# Fill the id box
id_box = id_box.send_keys(os.environ['ID'])
# Find password box
pass_box = driver.find_element(by=By.NAME, value='password')
# Send password
pass_box.send_keys(os.environ['PASSWORD'])
# Find login button
login_button = driver.find_element(by=By.NAME, value='submit')
# Click login
login_button.click()
# On va sur l'EDT, je fonctionne avec le lien pour refresh l'EDT qui a tendance à bug (vérifier si ça fonctionne)
driver.get("https://ns3085211.ip-147-135-255.eu/ensai/index.php?p=121")
# On trouve le nom de la semaine
semaine = driver.find_element(by=By.TAG_NAME, value='h2').text
nom = str.format("screenshot{}.png", semaine)
driver.get_screenshot_as_file(nom)
driver.quit()
