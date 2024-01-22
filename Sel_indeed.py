from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Initialize a Firefox webdriver (you need to have geckodriver installed)
driver = webdriver.Firefox()

# Navigate to the webpage
webpage = "https://www.indeed.com/jobs?q=Robotics+Software+Engineer&l=United+States&vjk=d5b6fddaa4613e8a&advn=3622365089007378"
driver.get(webpage)

# Wait for the dynamic content to load (adjust the timeout as needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.css-zu9cdh')))

# Get the page source after the content has loaded
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the <ul> element
ul_element = soup.find('ul', class_='css-zu9cdh')
job_details_list = []

allData = ul_element.find_all("div",{'class':"cardOutline"})

# Initialize a list to store all job details dictionaries
all_job_details = []

# Iterate over each div element
for data in allData:
    # Initialize a dictionary to store job details for the current listing
    job_details = {}

    # Company Name
    try:
        job_details['company_name'] = data.find("span", class_="companyName").text
    except:
        job_details['company_name'] = None

    # Rating
    try:
        job_details['rating'] = data.find("span", class_="ratingsDisplay").text
    except:
        job_details['rating'] = None

    # Timing Attribute
    try:
        job_details['timing_attribute'] = data.find("div", {"data-testid": "timing-attribute"}).text
    except:
        job_details['timing_attribute'] = None

    # Location
    try:
        job_details['location'] = data.find("div", class_="css-t4u72d").text
    except:
        job_details['location'] = None

    # Job Title
    try:
        job_details['job_title'] = data.find("div", class_="css-1m4cuuf").find("a", class_="jcs-JobTitle").text
    except:
        job_details['job_title'] = None

    # Salary
    try:
        job_details['salary'] = data.find("div", class_="heading6 salaryOnly").find("div", class_="css-1ihavw2").text
    except:
        job_details['salary'] = None

    # Append the dictionary to the list
    all_job_details.append(job_details)

# Print the list of all job details
print(all_job_details)

# Save the data to a CSV file
csv_filename = 'all_job_details.csv'
header = all_job_details[0].keys() if all_job_details else []

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Write the header to the CSV file
    writer.writeheader()

    # Write all job details to the CSV file
    writer.writerows(all_job_details)

print(f'Data saved to {csv_filename}')
# Close the webdriver
driver.quit()

'''
CLASS jcs-JobTitle css-jspxzf eu4oa1w0

Commpany name= 
data-testid="timing-attribute"
class="css-1x7z1ps eu4oa1w0"


div elementtiming="significant-render"
span class="css-1x7z1ps eu4oa1w0"

Location div  
class="company_location css-12lvszk e37uo190"

class="css-t4u72d eu4oa1w0"


JOb Title 
div class="css-1m4cuuf e37uo190"
a id="job_e202e6cff4236166"
span id="jobTitle-e202e6cff4236166"

Salary 
div class="heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"
div class="css-1ihavw2 eu4oa1w0"

'''