import srcomapi
import json
import time

def setup_api():
    return srcomapi.SpeedrunCom()

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
    api = setup_api()
    webgames = api.get_request("games?platform=jm95z9ol&_bulk=yes&max=1000")
    old_time = time.time()
    total_games = 0
    total_categories = 0
    total_categories_with_misc = 0
    
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

if __name__ == "__main__":
    main()
