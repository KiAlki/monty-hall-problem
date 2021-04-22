import json


def test_game_keep_choice(client):
    headers = {'Content-Type': "application/json"}
    data = {
        "choose_option": "keep",
        "attempts": 100000
    }
    response = client.post('/play', data=json.dumps(data), headers=headers)
    json_data = response.get_json()
    wins_percent = round(json_data["wins"] / data["attempts"], 2)
    assert 0.32 < wins_percent < 0.35


def test_game_change_choice(client):
    headers = {'Content-Type': "application/json"}
    data = {
        "choose_option": "change",
        "attempts": 100000
    }
    response = client.post('/play', data=json.dumps(data), headers=headers)
    json_data = response.get_json()
    wins_percent = round(json_data["wins"] / data["attempts"], 2)
    print(wins_percent)
    assert 0.65 < wins_percent < 0.68

