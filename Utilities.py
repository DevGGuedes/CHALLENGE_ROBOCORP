#file for generic methods for the entire project

from robocorp.tasks import task
from robocorp import browser
import json
import accessLA as LA

def openBrower():
    browser.goto(GetParameters("UrlSite"))

    return browser

def SendClick(browser, element):
    page = browser.page()
    page.click(element)

def SendText(browser, element, text):
    page = browser.page()
    page.fill(element, text)

def GetParameters(parameter):
    # Open the configuration file (.json) in read-only mode
    with open('config.json', 'r', encoding="utf-8") as file_config:
        config = json.load(file_config)

    return config[parameter]

def MainAutomation():
    try:
        LA.searchLA("teste")
    except Exception as e:
        print(f'Erro on system {e}')