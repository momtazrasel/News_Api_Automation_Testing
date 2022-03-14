from test_data.api_end_point import *
from test_data.common_data import data_from_server
from test_data.headers import headers_post


# from test_data.payloads import *


def response_get_apple_all_articles():
    res = data_from_server("GET", apple_all_articles)
    return res.json(), res.status_code


def response_get_tesla_all_articles():
    res = data_from_server("GET", tesla_all_articles)
    return res.json(), res.status_code


def response_get_us_business_headlines():
    res = data_from_server("GET", us_business_headlines)
    return res.json(), res.status_code


def response_get_tech_crunch_headlines():
    res = data_from_server("GET", tech_crunch_headlines)
    return res.json(), res.status_code


def response_get_wall_street_all_articles():
    res = data_from_server("GET", wall_street_all_articles)
    return res.json(), res.status_code
