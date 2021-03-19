from selenium import webdriver
import pytest
from sqlalchemy import create_engine
from sqlalchemy import insert, delete
from sqlalchemy import table, column
from helpers.general_helpers import generate_string
from helpers.db_helper import clear_db_user_not_admin, clear_db_user_groups_table


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--maxim')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1980, 1024)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def create_group():
    name = generate_string(8)
    # engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    engine = create_engine('postgresql+psycopg2://postgres:postgres@172.18.0.4/postgres')
    auth_group_table = table("auth_group",
                             column("id"),
                             column("name")
                             )
    stmt = (
        insert(auth_group_table).values(name=name)
    )
    engine.execute(stmt)
    yield name
    clear_db_user_groups_table()
    clear_db_user_not_admin()
    stmt = (
        delete(auth_group_table).where(auth_group_table.c.name == name)
    )
    engine.execute(stmt)
