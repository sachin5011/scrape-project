import multiprocessing
import time
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
import yaml

with open("configuration.yaml", "r") as file:
    config = yaml.safe_load(file)

def get_company_urls():
    global new_df
    domain_url = []
    driver = webdriver.Chrome()
    df = pd.read_csv(config["INPUT_PATH"])
    for comp in df["Name"]:
        company = comp.replace("&", "and")
        url = "https://www.google.com/search?q="+company
        driver.get(url)
        element = driver.find_element(By.CLASS_NAME, "yuRUbf")
        domain_url.append(element.text.split("\n")[2].split(" ")[0])
    return domain_url

def get_company_names():
    comp_names = []
    driver = webdriver.Chrome()
    df = pd.read_csv(config["INPUT_PATH"])
    for comp in df["Name"]:
        company = comp.replace("&", "and")
        url = "https://www.google.com/search?q="+company
        driver.get(url)
        element = driver.find_element(By.CLASS_NAME, "yuRUbf")
        comp_names.append(element.text.split("\n")[1].split(".")[0])

    return comp_names

def get_linkedin_handler(urls):
    linkedin_handler = []
    driver = webdriver.Chrome()
    for link in urls:
        driver.get(urls)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_links = soup.find_all('a')
        found_link = [str(f_link.get('href')) for f_link in all_links]
        for l_link in found_link:
            if l_link.startswith("https://www.linkedin.com/company/"):
                linkedin_handler.append(l_link)
                break
        else:
            linkedin_handler.append("NA")
    return linkedin_handler

def get_instagram_handler(urls):
    linkedin_handler = []
    driver = webdriver.Chrome()
    for link in urls:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_links = soup.find_all('a')
        found_link = [str(f_link.get('href')) for f_link in all_links]
        for l_link in found_link:
            if l_link.startswith("https://www.instagram.com/"):
                linkedin_handler.append(l_link)
                break
        else:
            linkedin_handler.append("NA")
    return linkedin_handler

def get_youtube_handler(urls):
    youtube_handler = []
    driver = webdriver.Chrome()
    for link in urls:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_links = soup.find_all('a')
        found_link = [str(f_link.get('href')) for f_link in all_links]
        for l_link in found_link:
            if l_link.startswith("https://www.youtube.com/"):
                youtube_handler.append(l_link)
                break
        else:
            youtube_handler.append("NA")
    return youtube_handler

def get_twitter_handlert(urls):
    twitter_handler = []
    driver = webdriver.Chrome()
    for link in urls:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_links = soup.find_all('a')
        found_link = [str(f_link.get('href')) for f_link in all_links]
        for l_link in found_link:
            if l_link.startswith("https://twitter.com/"):
                twitter_handler.append(l_link)
                break
        else:
            twitter_handler.append("NA")
    return twitter_handler

def get_facebook_handler(urls):
    facebook_handler = []
    driver = webdriver.Chrome()
    for link in urls:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_links = soup.find_all('a')
        found_link = [str(f_link.get('href')) for f_link in all_links]
        for l_link in found_link:
            if l_link.startswith("https://www.facebook.com/"):
                facebook_handler.append(l_link)
                break
        else:
            facebook_handler.append("NA")
    return facebook_handler
def main():
    # url = []
    # url.append(urls)
    # print(url)
    # print(len(url))
    url = get_company_urls()
    names = get_company_names()
    print(names)
    linkedin_handler = get_linkedin_handler(url)
    print(linkedin_handler)
    print(len(linkedin_handler))
    twitter_handler = get_twitter_handlert(url)
    print(twitter_handler)
    facebook_handler = get_facebook_handler(url)
    print(facebook_handler)
    instagram_handler = get_instagram_handler(url)
    print(instagram_handler)
    youtube_handler = get_youtube_handler(url)
    print(youtube_handler)

    results = {
        "company Urls" : urls,
        "Company Name" : names,
        "Linkedin Handler": linkedin_handler,
        "Twitter Handler": twitter_handler,
        "Facebook Handler": facebook_handler,
        "Instagram Handler": instagram_handler,
        "Youtube Handler": youtube_handler
    }
    print(results)
    df = pd.DataFrame(results)
    df.to_csv(config["OUTPUT_PATH"]+"results.csv", index=False)
    print("Your File has been created please check your output folder.....")


if __name__ == "__main__":

    main()
