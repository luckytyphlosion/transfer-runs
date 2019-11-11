import srcomapi
import json
import time

API_KEY = "hab46tiql9czis3f8jsaftw61"

def setup_api(api_key=None):
    return srcomapi.SpeedrunCom(api_key)

def test_search_for_game():
    api = setup_api()
    game = api.search(srcomapi.datatypes.Game, {"name": "super mario sunshine"})[0]
    assert(game.name == "Super Mario Sunshine")

def test_world_record():
    api = setup_api()
    game = srcomapi.datatypes.Game(api, id="v1pxjz68")
    record = game.categories[0].records[0]
    assert( isinstance(record.runs[0]["run"], srcomapi.datatypes.Run) )

def main():
    output = ""
    mc_level_names_to_mcce_category_names = {
        "Enter Nether": "Enter Nether",
        "All Swords": "All Swords",
    }

    api = setup_api(api_key=API_KEY)
    run_to_submit = {
      "run":{
        "category":"vdom79v2",
        "date":"2016-08-14",
        "platform":"8gej2n93",
        "verified":False,
        "times": {
          "realtime": 4.590,
          "ingame": 4.590
        },
        "players": [
          {
            "rel":"guest",
            "name":"kj9247r8"
          },
        ],
        "emulated":False,
        "video":"https://www.youtube.com/watch?v=JFeYaodeNbA",
        "comment":"2",
        "variables":{
          "e8mmkrq8":{
            "type":"pre-defined",
            "value":"xqkm4xyl"
          },
          "gnxrkv6n":{
            "type":"pre-defined",
            "value":"4qyjyw7q"
          },
          "ylqkvm3l":{
            "type":"pre-defined",
            "value":"klry0r2q"
          },
          "ylpm5erl":{
            "type":"pre-defined",
            "value":"5lemm651"
          },
          "j846z5wl":{
            "type":"pre-defined",
            "value":"rqveg7y1"
          },
          "0nwkeorn":{
            "type":"pre-defined",
            "value":"klryy3jq"
          },
          "ylqkjo3l":{
            "type":"pre-defined",
            "value":"zqorkv5q",
          }
        }
      }
    }

    response = api.post("runs", run_to_submit)
    print(response)

    #mc_levels = api.get_request("games/mc/levels")
    #mcce_categories = 

    # enter_nether_runs = api.get_request("runs?level=5928n796")
    # for enter_nether_run in enter_nether_runs:
        # if enter_nether_run["status"]["status"] == "new":
            # print(enter_nether_run)

    #for mc_level in mc_levels[:1]:
    #    print(f"Name: {mc_level['name']}, Id: {mc_level['id']}")

    #old_time = time.time()

"""
    for i, webgame in enumerate(webgames):
        zero_run_boards = []
        id = webgame["id"]
        print(id)
        if i % 99 == 0 and i != 0:
            print("Waiting to pass rate limit")
            while (time.time() - old_time < 60):
                time.sleep(1)
            old_time = time.time()
        webgame_records = api.get_request("games/" + id + "/records?top=1&embed=category")
        for board in webgame_records:
            if len(board["runs"]) == 0 and board["level"] is None:
                zero_run_boards.append(board)
                total_categories_with_misc += 1
        if len(zero_run_boards) > 0:
            total_games += 1
            temp_output = ""
            temp_output += "=== Game: %s (%s) ===\n" % (webgame["names"]["international"], webgame["weblink"])
            for board in zero_run_boards:
                temp_output += "Category: %s" % board["category"]["data"]["name"]
                if board["category"]["data"]["miscellaneous"]:
                    temp_output += " [Misc.]"
                else:
                    total_categories += 1
                temp_output += "\n"
            print(temp_output)
            output += temp_output + "\n"
    
    output = "Total Games: %s\nTotal Categories: %s\nTotal Categories With Misc: %s\n\n%s" % (total_games, total_categories, total_categories_with_misc, output)
    with open("zero_run_categories_nes.txt", "w+") as f:
        f.write(output)
        #ids.append(webgames["id"])
"""

if __name__ == "__main__":
    main()
