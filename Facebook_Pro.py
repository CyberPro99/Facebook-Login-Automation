from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path= r'D:\geckodriver') # I Use FirFox Webdrvier You Cna Install Any Webdrvier 
driver.get('https://www.facebook.com') # The Website Of Facebook 
driver.maximize_window() # To Make The window full Secreen 

with open('password.txt','r') as myfile: # Store The Passowrd Temprority In File Password.txt 
    password = myfile.read().replace('\n','')

    driver.find_element_by_xpath('//*[@id="email"]').send_keys('Your Facebook Email') # xpath of the Email edit text & You Email 
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Your Facebook Password') # xpath of the Password edit text & You Password 
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]').click() # xpath of The Login Button

    sleep(40) # If You Have Low Internet Connication leave it 40 Seconed if Not make it lowset 
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[3]').click() #Click The Vido Button in Fcebook