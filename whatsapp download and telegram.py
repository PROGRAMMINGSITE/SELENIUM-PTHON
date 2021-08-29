from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.get('https://www.google.com/search?q=whatsapp&oq=whatsapp&aqs=chrome..69i57j0i131i433i512l4j0i433i512l2j0i131i433i512l2.2581j0j7&sourceid=chrome&ie=UTF-8')
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/div').click()
driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[1]/div/div[1]/div[3]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[3]/div[1]/div[2]/a').click()
