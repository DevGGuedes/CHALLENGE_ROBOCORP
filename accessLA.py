# file for manipulation and access to the site

import Utilities as DAO
from robocorp import browser

def searchLA(text):

    try:
        
        browser = DAO.openBrower()
        page = browser.page

        DAO.SendClick(page, "/html/body/ps-header/header/div[2]/button")


    except Exception as e:
        print(f'Erro on system {e}')