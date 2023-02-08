from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')


# from Django to To-Do
assert 'To-Do' in browser.title

browser.quit()
