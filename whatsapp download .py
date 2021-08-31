from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.google.com/search?q=whatsapp&oq=whatsapp&aqs=chrome..69i57j0i131i433i512l4j0i433i512l2j0i131i433i512l2.2581j0j7&sourceid=chrome&ie=UTF-8&google_abuse=GOOGLE_ABUSE_EXEMPTION%3DID%3D400c4766f2922d4f:TM%3D1630395620:C%3Dr:IP%3D58.65.173.170-:S%3D61AqUkUu8J-RecX1X7lpv9o%3B+path%3D/%3B+domain%3Dgoogle.com%3B+expires%3DTue,+31-Aug-2021+10:40:20+GMT')
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/div').click()
driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[1]/div/div[1]/div[3]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[3]/div[1]/div[2]/a').click()
