from Assets.Pages.Utils import pytest
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'C'


@pytest.fixture
def driver(selection):
    url = 'https://www.saucedemo.com/inventory.html'
    if selection == 'F':
        driver = U.Firefox()
    elif selection == 'C':
        driver = U.Chrome()
    elif selection == 'E':
        driver = U.Edge()
    else:
        print('invalid selection ---- selecting default:: Firefox')
        driver = U.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
