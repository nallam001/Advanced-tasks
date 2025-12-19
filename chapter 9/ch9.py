# Problem 1: Fetch a Web Page Title

 import requests
 from bs4 import BeautifulSoup

 url = "https://example.com"
 response = requests.get(url)
 soup = BeautifulSoup(response.text, 'html.parser')
 title = soup.title.string
 print(f"Page Title: {title}")


# Problem 2: Extract All Links

import requests
  from bs4 import BeautifulSoup
   
  url = "https://example.com"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
   
  links = soup.find_all('a', href=True)
  for link in links:
     print(link['href'])
  

# Problem 3: Extract a Table

  from bs4 import BeautifulSoup
   
  html = """
  <table>
      <tr><th>Name</th><th>Age</th></tr>
      <tr><td>Alice</td><td>25</td></tr>
      <tr><td>Bob</td><td>30</td></tr>
  </table>
  """
  
 soup = BeautifulSoup(html, 'html.parser')
 rows = soup.find_all('tr')
  
 for row in rows:
     cells = row.find_all(['th', 'td'])
     row_data = [cell.text.strip() for cell in cells]
     print(row_data)
  


# Problem 4: Automate Google Search

from selenium import webdriver
 from selenium.webdriver.common.keys import Keys
 import time
  
driver = webdriver.Chrome()
 driver.get("https://www.google.com")
  
 search_box = driver.find_element_by_name("q")
 search_box.send_keys("Python Web Scraping")
 search_box.send_keys(Keys.RETURN)
  
 time.sleep(2)
 print(driver.title)
 driver.quit()
  


# Problem 5: Save Scraped Data to CSV

 from bs4 import BeautifulSoup
  import csv
   
  html = """
  <ul>
      <li>Apple</li>
      <li>Banana</li>
      <li>Cherry</li>
  </ul>
 """
 
 soup = BeautifulSoup(html, 'html.parser')
 fruits = [li.text.strip() for li in soup.find_all('li')]
  
 with open('fruits.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Fruit'])
     for fruit in fruits:
         writer.writerow([fruit])
  
