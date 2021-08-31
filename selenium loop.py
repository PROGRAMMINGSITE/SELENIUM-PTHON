from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
for i in range(5):
    loop=driver.get('https://www.youtube.com/')
    driver.implicitly_wait(4)