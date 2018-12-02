# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:48:23 2018

@author: Rodrigo
"""

import csv
import parameters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field


# defining new  variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'w'))

# writerow() method to the write to the file object
writer.writerow(['Nome', 'endereço', 'telefone'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com.br/maps/search/'+ parameters.search)


i=0
while True:
  # locate all elements

  elements = driver.find_elements_by_xpath('//*[contains(@class, "section-result-title-container")]')
  if len(elements) > i:
      elements[i].click() # click on the i-th element in the list
      sleep(5)
          # assigning the source code for the web page to variable sel
      sel = Selector(text=driver.page_source)

      # xpath to extract the text from the class containing the name
      nome = sel.xpath('//*[contains(@class, "section-hero-header-title")]/text()').extract_first()

      # if name exists
      if nome:
        # .strip() will remove the new line /n and white spaces
          nome = nome.strip()

      # xpath to extract the text from the class containing the job title
      endereço = sel.xpath('//*[@id="pane"]/div/div[1]/div/div/div[6]/div/div[1]/span[3]/span[3]/text()').extract_first()

      if endereço:
          endereço = endereço.strip()

      # xpath to extract the text from the class containing the company
      telefone = sel.xpath('//*[@id="pane"]/div/div[1]/div/div/div[9]/div/div[1]/span[3]/span[3]/text()').extract_first()

      if telefone:
          telefone = telefone.strip()
          
      nome = validate_field(nome)
      endereço = validate_field(endereço)
      telefone = validate_field(telefone)
      
      print('\n')
      print('Nome: ' + nome)
      print('endereço: ' + endereço)
      print('telefone: ' + telefone)
      
      writer.writerow([nome.encode('utf-8'),
                     endereço.encode('utf-8'),
                     telefone.encode('utf-8')])
      
      driver.get('https://www.google.com.br/maps/search/'+ parameters.search)
      
      sleep(1) 

                
      i += 1 # increment i
      sleep(1) # wait until list will be updated
      continue
  break 

  

