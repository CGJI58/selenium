from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

print(search_bar)

browser.quit()