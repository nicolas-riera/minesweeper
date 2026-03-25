import json
import os

from src.gamedata_path import get_gamedata_path

path = get_gamedata_path("scores.json")

class JsonManager:

    @staticmethod
    def read_scores():
        
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)
            return []

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    @staticmethod  
    def write_score(score):
        """
        score -> dict:{datetime, difficulty, timer}
        """

        data = JsonManager.read_scores()

        data.append(score)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def clear_scores():
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)