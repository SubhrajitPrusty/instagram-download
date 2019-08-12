#! /usr/bin/env python3

import os
import click
from splinter import Browser
from bs4 import BeautifulSoup as bs4

URL = "https://www.instagram.com/"
GECKODRIVER_PATH = "./geckodriver/geckodriver" if os.name == "posix" else "./geckodriver/geckodriver.exe"

@click.command()
@click.argument("username", type=click.STRING)
@click.option("--gecko_path", "-gp", default=GECKODRIVER_PATH, help="Enter path of gecko driver", type=click.Path())
def insta(username, gecko_path):
    """
    Download images from instagram
    """
    
    link = URL + username
    print("Downloading images {}...".format(username))

    with Browser("firefox", headless=True, executable_path=gecko_path) as browser:
        browser.visit(link)
        html = browser.html
        soup = bs4(html, "html.parser")

    data = soup.findAll("img")

    for x in data:
        x = x.get("src")
        os.system(f"wget --no-check-certificate -c -N -P Images/{username} {x}")
        print("Downloaded {}".format(x))

    def rename_image_dir(foldername):
        i = 1
        dirName = os.path.join("./Images/", foldername)
        path = os.getcwd() + dirName
        for filename in os.listdir(dirName):
            if not filename.endswith(".jpg"):
                os.rename(os.path.join(path, filename), os.path.join(path, foldername + '_' + str(i) + ".jpg"))
            i += 1

    rename_image_dir(username)

    print("\nFiles downloaded into Images/{}".format(username))
    
if __name__ == "__main__":
    insta()
