import srcomapi
import json
import time
import collections
import pathlib

API_KEY = "hab46tiql9czis3f8jsaftw61"

def setup_api(api_key=None):
    return srcomapi.SpeedrunCom(api_key)

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
    "gq7rrnnl":"1.14.4",
    "gq7zrdd1":"1.15",
    "21dor7gq":"1.15.1",
}

level_difficulty_to_name = {
    "4lxg24q2": "Easy", # Easy
    "8149mvqd": "Normal", # Normal
    "z19xe814": "Hard", # Hard
    "p129j4lx": "Hardcore"  # Hardcore
}

level_variable_to_seed_glitch_type = {
    "n2yzmeko": "Set Seed", # Set Seed
    "7kjw7gd3": "Set Seed Glitchless", # Set Seed Glitchless
    "xk979xd0": "Random Seed", # Random Seed
    "zd3re8dn": "Random Seed Glitchless", # Random Seed Glitchless
}

def set_seed_type_simple(level_run, catext_run, conversion_table, catext_category_variable):
    level_category = level_run["category"]
    seed_type_map = generate_seed_type_map(conversion_table)
    catext_category = seed_type_map[level_category]
    set_run_predefined_variable(catext_run, catext_category_variable, catext_category)

def get_all_runs(api, endpoint):
    runs_and_pagination = api.get_request(endpoint, keep_pagination=True)
    runs = runs_and_pagination["data"]
    pagination = runs_and_pagination["pagination"]

    while pagination["size"] == pagination["max"]:
        runs_and_pagination = api.get_request(pagination["links"][-1]["uri"], keep_pagination=True, full_request=True)
        runs.extend(runs_and_pagination["data"])
        pagination = runs_and_pagination["pagination"]
        print(f"pagination: {pagination}")

    return runs

# issues:
# date can be blank
# version can be blank
# difficulty can be blank

# Kill Wither sets "dlo31yel"

class VariableValue:
    __slots__ = ("variable", "value")
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

def archive_runs(api, level_id):
    level_runs = get_all_runs(api, f"runs?level={level_id}&max=200&embed=players") # 5928n796
    # enter_nether_seed_types = ("0135m63q", "0135m63q", "rqveryw1", "rqveryw1")
    archived_runs = []
    category_name = api.get_request(f"levels/{level_id}")["name"]
    category_name = category_name.replace("?", "")
    examiners = {}

    for run in level_runs:
        try:
            run_status = run["status"]["status"]
            if run_status == "new":
                continue

            if run["players"]["data"][0]["rel"] == "guest" and run["players"]["data"][0]["name"] == "N/A":
                continue

            archived_run = {}
            # archived_run["category"] = category_name

            archived_run["seed-glitch-type"] = level_variable_to_seed_glitch_type[run["category"]]

            run_player_obj = run["players"]["data"][0]
            archived_run["player"] = {}
            archived_run["player"]["rel"] = run_player_obj["rel"]

            if run_player_obj["rel"] == "user":
                run_player_name = run_player_obj["names"]["international"]
                archived_run["player"]["id"] = run_player_obj["id"]
            else:
                run_player_name = run_player_obj["name"]

            archived_run["player"]["name"] = run_player_name

            archived_run["times"] = {}
            archived_run["times"]["realtime"] = run["times"]["realtime_t"]
            archived_run["times"]["ingame"] = run["times"]["ingame_t"]
            
            run_values = run["values"]
            # Version
            if "jlzkwql2" in run_values:
                archived_run["version"] = level_lb_versions[run_values["jlzkwql2"]]
            else:
                archived_run["version"] = None

            # Difficulty
            if "9l737pn1" in run_values:
                archived_run["difficulty"] = level_difficulty_to_name[run_values["9l737pn1"]]
            else:
                archived_run["difficulty"] = None

            if "links" in run["videos"]:
                video_links = run["videos"]["links"]
                video_link = video_links[0]["uri"]
                archived_run["video-link"] = video_link
            if "text" in run["videos"]:
                archived_run["video-text"] = run["videos"]["text"]

            archived_run["date"] = run["date"]
            archived_run["submitted-date"] = run["submitted"]

            examiner_id = run["status"]["examiner"]
            if examiner_id in examiners:
                examiner_name = examiners[examiner_id]
            else:
                examiner_name = api.get_request(f"users/{examiner_id}")["names"]["international"]
                examiners[examiner_id] = examiner_name

            archived_run["status"] = {
                "status": run_status,
                "examiner": {"id": examiner_id, "name": examiner_name}
            }

            if run_status == "verified":
                archived_run["status"]["verify-date"] = run["status"]["verify-date"]
            elif run_status == "rejected":
                archived_run["status"]["rejection-reason"] = run["status"]["reason"]
            else:
                raise RuntimeError(f"Impossible status \"{run_status}\"!")

            run_comment = run["comment"]
            if run_comment is None:
                run_comment = ""
            archived_run["comment"] = run_comment

            archived_run["splits"] = run["splits"]
            archived_runs.append(archived_run)

        except:
            raise RuntimeError("Error! run: %s, archived_run: %s" % (run, archived_run))

    with open(f"archive/{category_name}.txt", "w+") as f:
        json.dump(archived_runs, f, sort_keys=True, indent=2)


def main():
    output = ""
    api = setup_api(api_key=API_KEY)
    pathlib.Path("archive/").mkdir(parents=True, exist_ok=True)

    """
    # Enter Nether
    archive_runs(api, level_id="5928n796")#, catext_id="z27lj0gd", seed_type_variable="9l71q7ql", seed_types=("0135m63q", "0135m63q", "rqveryw1", "rqveryw1"))

    # All Swords
    archive_runs(api, level_id="n93nm2w0")#, catext_id="7dg4popd", seed_type_variable="yn21z528", seed_types=("5lem4xz1", "5lem4xz1", "0q5g53nl", "0q5g53nl"))
    # All Wood Logs
    archive_runs(api, level_id="ldyegrkw")#, catext_id="mkeqm06k", seed_type_variable="6njqg4jl", seed_types=("4lxe86r1", "4lxe86r1", "8147vwj1", "8147vwj1"))
    # Full Armor and 15 Levels
    archive_runs(api, level_id="ldy53pw3")#, catext_id="wk6vy5xd", seed_type_variable="ql64j7k8", seed_types=("gq7r4xyl", "jqzx53m1", "21g24pml", "klry022q"))
    # All Wool
    archive_runs(api, level_id="z98zmr9l")#, catext_id="5dw7zllk", seed_type_variable="kn0zqjo8", seed_types=("z1989pkq", "81pd05k1", "p12xw0kl", "xqkm4nyl"))
    # HDWGH
    archive_runs(api, level_id="gdrqzoz9")#, catext_id="xk987oy2", seed_type_variable="onv23j0l", seed_types=("gq7rrvvl", "jqzxxrg1", "21g22wnl", "klryyejq"))

    # Kill Wither
    archive_runs(api, level_id="5d7p1qdy")#, catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        #extra_variables=(VariableValue(variable="dlo31yel", value="mlnz0odl"),))
    # Kill Elder Guardian
    archive_runs(api, level_id="kwj0g0dg")#, catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        #extra_variables=(VariableValue(variable="dlo31yel", value="810wmd5q"),))
    # All Bosses
    archive_runs(api, level_id="owo8jjd6")#, catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        #extra_variables=(VariableValue(variable="dlo31yel", value="9qjx48gl"),))

    # "e8mmkrq8" = item, "ylqkvm3l" = Structures option
    # Obtain Cake
    archive_runs(api, level_id="rw6lepw7")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        #extra_variables=(VariableValue(variable="e8mmkrq8", value="gq7r46yl"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Golden Apple
    archive_runs(api, level_id="rdnlq5wm")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        #extra_variables=(VariableValue(variable="e8mmkrq8", value="21g243ml"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Emerald
    archive_runs(api, level_id="xd023m9q")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        #extra_variables=(VariableValue(variable="e8mmkrq8", value="jqzx5mm1"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Diamond
    archive_runs(api, level_id="29vl5qwv")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        #extra_variables=(VariableValue(variable="e8mmkrq8", value="xqkm4xyl"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    """

    # Obtain Diamond (No Structures)
    archive_runs(api, level_id="xd4yrqdm")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
    #    extra_variables=(VariableValue(variable="e8mmkrq8", value="xqkm4xyl"), VariableValue(variable="ylqkvm3l", value="21d3yejq")))

    # players = {
        # "players": [{
            # "rel": "user", "id": "18ql617j"
        # }]
    # }

    # response = api.put("runs/y816q7dz/players", players)
    # print(response.json())

    # Obtain Emerald (No Structures)
    archive_runs(api, level_id="ldyx1k93")#, catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
    #    extra_variables=(VariableValue(variable="e8mmkrq8", value="jqzx5mm1"), VariableValue(variable="ylqkvm3l", value="21d3yejq")))
    
    """
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
    """

    #mc_levels = api.get_request("games/mc/levels")
    #mcce_categories = 

    # enter_nether_runs = api.get_request("runs?level=5928n796")
    # for enter_nether_run in enter_nether_runs:
        # if enter_nether_run["status"]["status"] == "new":
            # print(enter_nether_run)

    #for mc_level in mc_levels[:1]:
    #    print(f"Name: {mc_level['name']}, Id: {mc_level['id']}")

    #old_time = time.time()

if __name__ == "__main__":
    main()
