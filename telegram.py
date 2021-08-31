from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.get('https://www.google.com/search?q=telegram&oq=tele&aqs=chrome.0.69i59j69i57j69i60l2.1894j0j7&sourceid=chrome&ie=UTF-8')
driver.find_element_by_xpath('//*[@id="rso"]/div[9]/div/div/div[1]/a/h3').click()
driver.find_element_by_xpath('//*[@id="detail-download-button"]').click()