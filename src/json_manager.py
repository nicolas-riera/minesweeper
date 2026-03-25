import json

from src.gamedata_path import get_gamedata_path

def read_scores():
    with open(get_gamedata_path("scores.json"), "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_score(score):
    """
    score -> dict:{datetime, difficulty, timer}
    """

    data = read_scores()

    for k, v in score:
        data[k] = v

    with open(get_gamedata_path("scores.json"), "w", encoding="utf-8") as f:
        json.dump(data, f)

def clear_scores():
    with open(get_gamedata_path("scores.json"), "w", encoding="utf-8") as f:
        json.dump({}, f)