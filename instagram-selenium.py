from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import requests
import os
from selenium.webdriver.firefox.options import Options

username = "pyasiarun"
url = 'http://instagram.com/'+username
driver = webdriver.Chrome()

driver.get(url)
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')
soup = BeautifulSoup(driver.page_source,'html.parser')
images = soup.find_all(class_ ="FFVAD")
os.mkdir(username)
for imagesrc in images:
    image_url = imagesrc["src"]
    resp = requests.get(image_url)
    print("Downloading",image_url)
    image_data = resp.content
    with open(username+"/"+str(images.index(imagesrc))+".jpg","wb") as f:
        f.write(image_data)
print ("Headless Firefox Initialized")
driver.quit()
print("files are downloaded")



