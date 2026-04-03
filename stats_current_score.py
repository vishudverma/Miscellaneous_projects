"""
So figured it out how this work now it's just a job of calling the apis which are stored in the json and being used as lists in the program from here on out this is just a list comprehension tutorial
I need to find an alternative to making this project because the method that TIM is using is rendered mostly useless.
Yeah what I am doing here in one go TIM is doing it in multiple steps using many functions, I think this is fine.
"""

from requests import get
import requests

BASE_URL = "https://cdn.nba.com"
ALL_JSON = "/static/json/liveData/scoreboard/todaysScoreboard_00.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}


def main():
    try:
        response = get(BASE_URL + ALL_JSON, headers=headers)
        response.raise_for_status()  # checking for success

        data = response.json()
        scoreboard = data["scoreboard"]
        games = scoreboard["games"]
        for game in games:
            home_team = game["homeTeam"]["teamName"]
            away_team = game["awayTeam"]["teamName"]
            home_team_score = game["homeTeam"]["score"]
            away_team_score = game["awayTeam"]["score"]

            print("----------------------------------------------")
            print(f"{home_team} vs {away_team}")
            print(f"{home_team_score} - {away_team_score}")

    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
