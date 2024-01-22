# https://note.nkmk.me/en/python-pip-install-requirements/

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


load_dotenv()

# Get email and password from environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

driver = webdriver.Firefox()

driver.get('https://www.linkedin.com/login')

driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)

driver.find_element(By.CSS_SELECTOR, "[data-litms-control-urn='login-submit']").click()


page_url = "https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3630229206&f_E=2&geoId=103644278&keywords=%22Robotics%20Engineer%22&location=United%20States&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
profile_url = "https://www.linkedin.com/in/omkar-bharambe-76885a190/"

driver.get(page_url)
page_source = driver.page_source

# Extract job profile, company, and location using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

job_title_element = soup.select_one('h1.text-heading-xlarge')
job_profile = job_title_element.text.strip() if job_title_element else "Job Title not found"


# Print the extracted job title
print(job_profile)

# Quit the browser
driver.quit()

'''
<h1 class="text-heading-xlarge inline t-24 v-align-middle break-words">Shubham Malhotra</h1>



Job Profile: <a data-control-id="eqYYz3SXrU+ZIYBXhwW6ng==" tabindex="0" href="/jobs/view/3630229206/?eBP=CwEAAAGMUgNw4yoqbXbQMBvwda9q019SwnJ6x-9uOYSMQxsUF8OM4jMl5oFeDTTlBvwQX_BRhTAuWSVy1r6MpPA-pS8IZH8V7KBePkWONAuNtq_qu56QjC2PkNggP9v4ebt-PVv1-dKHlpjfJmHGWVLvfydqxKntWP2mgvVw4hE2-i7DVLGEU6M96Byk8IBsPfN0AZU6HQAHjGsaJM-_y4NBdYZNAan6zLSVa8sDlXFfNibvrsFfbCHFpU6JfauTFmgsti9hdr1Jav32fi2u38gidXEmcjP8KZ_JeJPCeUdxan7EvYdY0cDxg-iQpcb-5jmx9HACGlsQ1VCSeHuSxbUZSJtvV1ug3fOXb28adHBJayn5AZwgbvVjbpyMKZ8uk3YrDfwXiQ&amp;refId=ppmtmgNWMCdzzF6JMeVIBw%3D%3D&amp;trackingId=eqYYz3SXrU%2BZIYBXhwW6ng%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember1966" class="disabled ember-view job-card-container__link job-card-list__title" aria-label="Robotics Engineer">
                    Robotics Engineer
                </a>
Company: <span class="job-card-container__primary-description ">
                Magna International
              </span>
Location: class="job-card-container__metadata-item "       


1) click 
job name
company name
Location 
click 

<a data-control-id="9d28oMI5koJLB62trRkJPw==" tabindex="0" href="/jobs/view/3775182302/?eBP=CwEAAAGMUgNw4zRSqAYkzIwaSJtpMHvM6VK_DORKB9oDL5NL_5n_oFLt3LuWr3rCniVRGSrFg7MpY8yOlzGz3NJrW3fCBrMDjnEzRxIXB570GiRreE3vcxsdKIGw8O-P63LxET7w6xOpP-4E-Ie7u4B1GR30Aufn8yeM64-e_WtBhPeygdwC6oPukQXxzl84--SvEhKdwKiwy_rAhSuLPVLIO4RXfEOI70Y7qLROoZygTDDvqwmKZ34McGOorcaFUjTVt5IWxOzYrcA4Z_4q1_gi3PgpSGaaxFS8tZFeICul8v8J9pM-iqnl38FKyzhZEx8hL9Z-SwHzNAm5XVaaL6qoVbcMplBk-sN5LEsE3EJlFe1HNexKeSfbnlUTT5bD-vJqE_t9mw&amp;refId=ppmtmgNWMCdzzF6JMeVIBw%3D%3D&amp;trackingId=9d28oMI5koJLB62trRkJPw%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember1977" class="disabled ember-view job-card-container__link job-card-list__title" aria-label="Robotics Engineer">
                    Robotics Engineer
                </a>
'''