from robocorp.tasks import task
import Utilities as DAO
from robocorp import browser

"""@task
def minimal_task():
    message = "Hello"
    message = message + " World!"""


@task
def taksConsulting():
    browser.configure(
        slowmo=1000,
        browser_engine="chromium", 
        screenshot="only-on-failure", 
        headless=True
    )

    DAO.MainAutomation()