from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.get('https://www.google.com/search?q=telegram&oq=telg&aqs=chrome.1.69i57j0i10i433j0i10i512j0i10i433l3j0i10i512j0i10i433l3.2111j0j7&sourceid=chrome&ie=UTF-8&google_abuse=GOOGLE_ABUSE_EXEMPTION%3DID%3D75b92c3730a0cbd4:TM%3D1630396596:C%3Dr:IP%3D58.65.173.170-:S%3DoBrzttTwWbdHFhY5FgIxLdM%3B+path%3D/%3B+domain%3Dgoogle.com%3B+expires%3DTue,+31-Aug-2021+10:56:36+GMT')
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()