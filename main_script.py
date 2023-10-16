import multiprocessing

import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from undetected_chromedriver import ChromeOptions
import yaml

with open("configuration.yaml", "r") as file:
    config = yaml.safe_load(file)


class GoogleSearchScrape:
    urls = []

    def __init__(self):
        self.uc_options = ChromeOptions()
        self.uc_options.add_argument('--headless')
        self.uc_options.add_argument('--no-sandbox')
        self.uc_options.add_argument('--disable-dev-shm-usage')
        self.driver = uc.Chrome(options=self.uc_options)

    def get_company_urls(self):
        df = pd.read_csv(config["INPUT_PATH"])
        for comp in df["Name"]:
            company = comp.replace("&", "and")
            url = "https://www.google.com/search?q=" + company
            self.driver.get(url)
            element = self.driver.find_element(By.CLASS_NAME, "yuRUbf")
            self.urls.append(element.text.split("\n")[2].split(" ")[0])
        return self.urls

    def get_company_names(self):
        comp_names = []
        df = pd.read_csv(config["INPUT_PATH"])
        for comp in df["Name"]:
            company = comp.replace("&", "and")
            url = "https://www.google.com/search?q=" + company
            self.driver.get(url)
            element = self.driver.find_element(By.CLASS_NAME, "yuRUbf")
            comp_names.append(element.text.split("\n")[1].split(".")[0])
        return comp_names

    def get_linkedin_handler(self):
        linkedin_handler = []
        for link in self.urls:
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_links = soup.find_all('a')
            found_link = [str(f_link.get('href')) for f_link in all_links]
            for l_link in found_link:
                if l_link.startswith("https://www.linkedin.com/company/"):
                    linkedin_handler.append(l_link)
                    break
            else:
                linkedin_handler.append("NA")
        return linkedin_handler

    def get_instagram_handler(self):
        linkedin_handler = []
        for link in self.urls:
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_links = soup.find_all('a')
            found_link = [str(f_link.get('href')) for f_link in all_links]
            for l_link in found_link:
                if l_link.startswith("https://www.instagram.com/"):
                    linkedin_handler.append(l_link)
                    break
            else:
                linkedin_handler.append("NA")
        return linkedin_handler

    def get_youtube_handler(self):
        youtube_handler = []
        for link in self.urls:
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_links = soup.find_all('a')
            found_link = [str(f_link.get('href')) for f_link in all_links]
            for l_link in found_link:
                if l_link.startswith("https://www.youtube.com/"):
                    youtube_handler.append(l_link)
                    break
            else:
                youtube_handler.append("NA")
        return youtube_handler

    def get_twitter_handler(self):
        twitter_handler = []
        for link in self.urls:
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_links = soup.find_all('a')
            found_link = [str(f_link.get('href')) for f_link in all_links]
            for l_link in found_link:
                if l_link.startswith("https://twitter.com/"):
                    twitter_handler.append(l_link)
                    break
            else:
                twitter_handler.append("NA")
        return twitter_handler

    def get_facebook_handler(self):
        facebook_handler = []
        for link in self.urls:
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_links = soup.find_all('a')
            found_link = [str(f_link.get('href')) for f_link in all_links]
            for l_link in found_link:
                if l_link.startswith("https://www.facebook.com/"):
                    facebook_handler.append(l_link)
                    break
            else:
                facebook_handler.append("NA")
        return facebook_handler

if __name__ == "__main__":
    obj = GoogleSearchScrape()
    company_links = obj.get_company_urls()
    print(company_links)
    print(len(company_links))
    company_names = obj.get_company_names()
    print(company_names)
    print(len(company_names))
    linkedin_handler = obj.get_linkedin_handler()
    print(linkedin_handler)
    print(len(linkedin_handler))
    instagram_handler = obj.get_instagram_handler()
    print(instagram_handler)
    print(len(instagram_handler))
    facebook_handler = obj.get_facebook_handler()
    print(facebook_handler)
    print(len(facebook_handler))
    twitter_handler = obj.get_twitter_handler()
    print(twitter_handler)
    print(len(twitter_handler))
    youtube_handler = obj.get_youtube_handler()
    print(youtube_handler)
    print(len(youtube_handler))
