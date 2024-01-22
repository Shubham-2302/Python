from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import os

'''This is a python file used to scrape Jobs,  Location, Salary, company name '''

list_of_jobs = []
job_info= {}

target_url = "https://www.indeed.com/jobs?q=Robotics+Software+Engineer&l=United+States&vjk=d5b6fddaa4613e8a"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}

response = requests.get(target_url,headers=header)

soup = BeautifulSoup(response.text,'html.parser')

# Find any <ul> element on the page
ul_element = soup.find_all('ul')
# Check if the <ul> element is found
if ul_element:
    # Extract the text content inside the <ul> element
    ul_content = ul_element.get_text(strip=True, separator='\n')
    print(ul_content)
else:
    print("UL element not found.")


    