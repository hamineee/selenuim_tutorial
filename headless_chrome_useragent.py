
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/84.0.4147.125 Safari/537.36

URL = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(URL)
detected_value = browser.find_element_by_id('detected_value')

print(detected_value.text)
