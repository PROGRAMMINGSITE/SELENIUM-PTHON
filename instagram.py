from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.get('https://www.instagram.com/')
driver.implicitly_wait(5)
username = driver.find_element_by_name('username').send_keys('a_ahadraza')
password = driver.find_element_by_name('password').send_keys('hellodear')
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
driver.quit()