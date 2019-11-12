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

class Run:
    __slots__ = (,)
    
    def __init__(self):
        pass


"""
Enter Nether


"""

level_lb_category_to_catext_category = {
    "5928n796", 
}

level_lb_version_to_catext_version_subversion = {

# set run version
# set run difficulty

level_lb_versions = {
     "rqvx06l6":"1.0",
     "5len0klo":"1.1",
     "0q54m2lp":"1.2.1", "4lxgk4q2":"1.2.2", "81496vqd":"1.2.3", "z19xv814":"1.2.4", "p129k4lx":"1.2.5",
     "81pez8l7":"1.3.1", "xqko3k19":"1.3.2",
     "gq72od1p":"1.4.2", "21g968qz":"1.4.4", "jqzgw8lp":"1.4.5", "klrxdmlp":"1.4.6", "21d6n5qe":"1.4.7",
     "5q8433ld":"1.5.1", "4qy7m2q7":"1.5.2",
     "mlne7jlp":"1.6.1", "8106y21v":"1.6.2", "9qj2o314":"1.6.4",
     "jq6vwj1m":"1.7.2",
     "21d43441":"1.7.3",
     "5lm2emqv":"1.7.4",
     "81w72vq4":"1.7.5",
     "814o96vq":"1.7.6",
     "z192xv8q":"1.7.7",
     "p12v9k4q":"1.7.8",
     "zqojex1y":"1.7.9",
     "013xkx15":"1.7.10",
     "rqvx26l6":"1.8",
     "5lenyklo":"1.8.1",
     "21dv7g1e":"1.8.2",
     "5q8276qd":"1.8.3",
     "5le86mlo":"1.8.4",
     "01340kl5":"1.8.5",
     "rqvz7516":"1.8.6",
     "5levop1o":"1.8.7",
     "gq7zyr1p":"1.8.8",
     "4lx5gk41":"1.8.9",
     "81pyez81":"1.9",
     "xqkeo3kq":"1.9.1",
     "gq752od1":"1.9.2",
     "21gn968l":"1.9.3",
     "jqzngw8q":"1.9.4",
     "klr3xdml":"1.10",
     "jq678gv1":"1.10.2",
     "0q54o3nl":"1.11",
     "4lxgvw4q":"1.11.2",
     "xqkonxn1":"1.12",
     "5q8270kq":"1.12.1",
     "p12ongvl":"1.12.2",
     "8142pg0l":"1.13",
     "z19rz201":"1.13.1",
     "z19ryv41":"1.13.2",
     "9qj49koq":"1.14",
     "814vn2v1":"1.14.2",
     "jqzx69m1":"1.14.3",
     "gq7rrnnl":"1.14.4"
 }

catext_versions = {
     "mlnzz40l":"1.0",
     "810wwowq":"1.1",
     "9qjxx6el":"1.2",
     "81w55vo1":"1.3",
     "zqorr8pq":"1.4",
     "01355odq":"1.5",
     "rqveek71":"1.6",
     "5lemm651":"1.7",
     "0q5gg9ml":"1.8",
     "4lxeev21":"1.9",
     "81477501":"1.10",
     "z1988j0q":"1.11",
     "p12xx67l":"1.12",
     "81pdd3g1":"1.13",
     "xqkmmgnl":"1.14"
}

catext_subversions = {
     "81w5zz61":"1.0",
     "21d3wjpq":"1.1",
     "klr6xe0l":"1.2.1",
     "21do6j3q":"1.2.2",
     "5q8r4xr1":"1.2.3",
     "4qy87v31":"1.2.4",
     "mlnke46l":"1.2.5",
     "jq6gv9n1":"1.3.1",
     "5lmw2ryq":"1.3.2",
     "81wr7v9l":"1.4.2",
     "zqo2j8gl":"1.4.4",
     "0134xokl":"1.4.5",
     "rqvzxk51":"1.4.6",
     "5levn6p1":"1.4.7",
     "xqk6oe91":"1.5.1",
     "21g2v6ol":"1.5.2",
     "jqzygn4l":"1.6.1",
     "klr6x30l":"1.6.2",
     "gq7z25r1":"1.6.4",
     "rqveg7y1":"1.7.2",
     "21go9noq":"1.7.4",
     "jqzygnkl":"1.7.5",
     "klr6x3wl":"1.7.6",
     "21do6kgq":"1.7.7",
     "5q8r4k61":"1.7.8",
     "4qyj9x7q":"1.7.9",
     "9qje2601":"1.7.10",
     "xqkm234l":"1.8",
     "4qy87zd1":"1.8.1",
     "mlnke8nl":"1.8.2",
     "81096vp1":"1.8.3",
     "9qje27o1":"1.8.4",
     "jq6gv5o1":"1.8.5",
     "5lmw2o0q":"1.8.6",
     "81wr746l":"1.8.7",
     "0q5gywvl":"1.8.8",
     "0q5gy6vl":"1.8.9",
     "0134x9yl":"1.9",
     "rqvzxvy1":"1.9.1",
     "5levnn61":"1.9.2",
     "0q5744vl":"1.9.3",
     "4lxdgggq":"1.9.4",
     "814499k1":"1.10",
     "z19dxx4l":"1.10.1",
     "p124992q":"1.10.2",
     "klrymeoq":"1.11",
     "81p6eenq":"1.11.1",
     "xqk6oo41":"1.11.2",
     "81w5zg61":"1.12",
     "gq7z22r1":"1.12.1",
     "4qyjdrdq":"1.12.2",
     "21go99oq":"1.13",
     "jqzyggkl":"1.13.1",
     "814786k1":"1.13.2",
     "gq7r0orl":"1.14",
     "klr6xxwl":"1.14.1",
     "mlnzpnnl":"1.14.2",
     "4lxerkg1":"1.14.3",
     "rqveg9y1":"1.14.4"
}

def convert_level_lb_version_to_catext_version(api, level_lb_version):
    version_name = level_lb_versions[level_lb_version]
    version_name_major = version_name.split(".")[1]

    for api_id, catext_version in catext_versions.values():
        if catext_version.split(".")[1] == version_name_major:
            version_id = api_id
            break            
    else:
        raise RuntimeException()

    for api_id, catext_subversion in catext_subversions.values():
        if catext_subversion == version_name:
            subversion_id = api_id
            break
    else:
        raise RuntimeException()

    return version_id, subversion_id

def create_new_run():
    return {"platform": "8gej2n93", "verified": False, "emulated": False}

def get_all_runs(api, endpoint):
    runs_and_pagination = api.get_request(endpoint, keep_pagination=True)
    runs = runs_and_pagination["data"]
    pagination = runs_and_pagination["pagination"]

    while pagination["size"] == pagination["max"]:
        runs_and_pagination = api.get_request(pagination["links"][0]["uri"], keep_pagination=True, full_request=True)
        runs.extend(runs_and_pagination["data"])
        pagination = runs_and_pagination["pagination"]

    return runs

def transfer_enter_nether_runs(api):
    enter_nether_level_runs = get_all_runs("runs?level=5928n796&max=200")
    enter_nether_catext_runs = api.get_request("runs?category=z27lj0gd&max=200")
    
    enter_nether_catext_video_links = set()

    for enter_nether_catext_run in enter_nether_catext_runs:
        video_links = enter_nether_catext_run["videos"]["links"]
        if len(video_links) != 1:
            raise RuntimeException(f"Found Enter Nether Category Extensions run with more than one link (run id: {enter_nether_catext_run['id']})")
        video_link = video_links[0]
        enter_nether_catext_video_links.add(video_link)

    for run in enter_nether_level_runs:
        if run["status"]["status"] == "rejected":
            continue

        video_links = run["videos"]["links"]
        if len(video_links) != 1:
            raise RuntimeException(f"Found Enter Nether Level run with more than one link (run id: {run['id']})")

        video_link = video_links[0]

        if video_link in enter_nether_catext_video_links:
            print("Run with id %s already submitted" % run["id"])
            continue

        run_to_submit = create_new_run()
        run_to_submit["category"] = "z27lj0gd" # catext enter nether
        run_to_submit["date"] = run["date"]
        run_to_submit["video"] = video_link

        run_to_submit["times"]["realtime"] = run["times"]["realtime_t"]
        run_to_submit["times"]["ingame"] = run["times"]["ingame_t"]

        run_comment = run["comment"]
        if run_comment is None:
            run_comment = ""

        run_to_submit["comment"] = run_comment

        

def main():
    output = ""

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
        "emulated":False,
        "video":"https://www.youtube.com/watch?v=JFeYaodeNbA",
        "comment":"",
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
