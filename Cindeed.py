import requests
from bs4 import BeautifulSoup
import json
import csv

BASE_URL = "https://www.indeed.com/jobs"
SEARCH_TERMS = "Robot OR Software"
LOCATION = "United States"  # Adjust as needed

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    job_cards = soup.find_all("div", class_="job_seen_beacon")
    jobs = []

    for job_card in job_cards:
        title = job_card.find("h2").text.strip()
        company = job_card.find("span", class_="companyName").text.strip()
        location = job_card.find("div", class_="companyLocation").text.strip()
        salary = job_card.find("span", class_="salary-snippet")
        salary = salary.text.strip() if salary else None

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "salary": salary
        })

    return jobs

def main():
    all_jobs = []
    page = 0

    while True:
        url = f"{BASE_URL}?q={SEARCH_TERMS}&l={LOCATION}&start={page * 10}"
        jobs = scrape_jobs(url)

        if not jobs:
            break

        all_jobs.extend(jobs)
        page += 1

    with open("indeed_jobs.json", "w") as f:
        json.dump(all_jobs, f, indent=2)

    with open("indeed_jobs.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "salary"])
        writer.writeheader()
        writer.writerows(all_jobs)

if __name__ == "__main__":
    main()
