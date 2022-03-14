import allure
from test_data.user_api.news_api_data import *


@allure.step('wall_street_all_articles')
def test_o4_wall_street_all_articles():
    response_body, status_code = response_get_wall_street_all_articles()
    print(response_body)
    assert status_code == 200
    print(response_body["articles"][0]["source"])
    print(response_body["articles"][2]["source"])
    assert type(response_body["articles"][0]["source"]) is dict
    # assert type(response_body["articles"][0]["source"]["id"]) is str
    # # assert response_body["articles"][0] == response_body
    # # assert response_body["articles"][0]["id"] == "engadget"
    for i in range(9):
        assert type(response_body["articles"][i]["source"]["name"]) is str
        assert type(response_body["articles"][i]["title"]) is str
        assert type(response_body["articles"][i]["description"]) is str
        assert type(response_body["articles"][i]["publishedAt"]) is str




