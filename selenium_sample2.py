#This is required to automate tasks through browser.
from selenium import webdriver
# This library is required to type text into textboxself.
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
elem1 = driver.find_element_by_name("email")
elem1.send_keys("vipashadhiman.11@gmail.com")
elem2 = driver.find_element_by_id("pass")
elem2.send_keys("mybeautifulworld")
elem3 = driver.find_element_by_id("loginbutton")
elem3.click()
elem4 = driver.find_element_by_id("userNavigationLabel")
elem4.click()
elem5 = driver.find_element_by_class("_54nh")
elem5.click()
driver.close()
#driver.get("http://www.google.com")
# these forward and backward commands are used to move fwd and bkwd in history.
#driver.forward()
#driver.back()
#print driver.get_cookies()
#driver.forward()
## Now set the cookie. This one's valid for the entire domain
#cookie = {'name' : 'secret', 'value' : 'vipasha'}
#driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
#print driver.get_cookies()
