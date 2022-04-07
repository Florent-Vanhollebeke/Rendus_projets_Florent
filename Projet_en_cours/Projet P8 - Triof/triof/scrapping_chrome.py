from selenium import Webdriver 
from selenium.webdriver.common.keys import Keys
import time


# Fumction for scrolling to the bottom of Google
# Images results
def scroll_to_bottom():
  
    last_height = driver.execute_script('\
    return document.body.scrollHeight')
  
    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')
  
        # waiting for the results to load
        # Increase the sleep time if your internet is slow
        time.sleep(3)
  
        new_height = driver.execute_script('\
        return document.body.scrollHeight')
  
        # click on "Show more results" (if exists)
        try:
            driver.find_element_by_css_selector(".YstHxe input").click()
  
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)
  
        except:
            pass
  
        # checking if we have reached the bottom of the page
        if new_height == last_height:
            break
  
        last_height = new_height




query = "dirty bottle"

driver = Webdriver.chrome(r"C:\Users\flore\OneDrive\Documents\Simplon\Rendus_projets_Florent\Projet_en_cours\Projet P8 - Triof\triof")
driver.maximize_window()

driver.get('https://images.google.com/')

box = driver.find_element_by_xpath('//*[@id="REsRA"]')

driver.find_element_by_name('q').send_keys('dirty bottle')
driver.find_element_by_name('q').send_keys(Keys.Enter )

box.send_keys(query)

box.send_keys(Keys.ENTER)

scroll_to_bottom()


for i in range(1, 50):
    
    # range(1, 50) will capture images 1 to 49 of the search results
    # You can change the range as per your need.
    try:
  
      # XPath of each image
        img = driver.find_element_by_xpath(
            '//*[@id="islrg"]/div[1]/div[' +
          str(i) + ']/a[1]/div[1]/img')
  
        # Enter the location of folder in which
        # the images will be saved
        img.screenshot('Download-Location' +  
                       query + ' (' + str(i) + ').png')
        # Each new screenshot will automatically
        # have its name updated
  
        # Just to avoid unwanted errors
        time.sleep(0.2)
  
    except:
          
        # if we can't find the XPath of an image,
        # we skip to the next image
        continue
  


driver.close()