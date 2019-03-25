from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
# (use for browser testing--selenium)
driver = webdriver.Chrome(executable_path="/home/asmita/Downloads/chromedriver")

class Instagram:
    def get_page(self,user_name):
        try:
            driver.get("https://www.instagram.com/"+user_name)
            soup = BeautifulSoup(driver.page_source,'html.parse')
            return soup
        except Exception:
            print("Failed to get instagram account")

instaobj = Instagram()
username = "saurav_mgr"
page_resp = instaobj.get_page(username)
