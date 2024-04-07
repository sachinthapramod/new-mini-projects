from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user : ')
filepath = input('Enter your filepath (images/video): ') #file path you need to send

input('Enter anything after scanning QR code')

user = driver.find_elements_by_xpath('//div[@title = "{}"]'.format(name))
user.click()

attachment = driver.find_element_by_xpath('//div[@title = "Attach"]') # details of attachment icon
attachment.click() #click on attachment icon

file = driver.find_element_by_xpath(
   '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
file.send_keys(filepath)

sleep(3)  # wait 3 seconds for load the file

send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()