from selenium import webdriver

chrome = webdriver.Chrome('chromedriver.exe', chrome_options=options)
chrome.get("https://www.facebook.com/")