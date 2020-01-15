import srcomapi
import json
import time
import collections

API_KEY = "hab46tiql9czis3f8jsaftw61" # don't bother using this key, it's been invalidated

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

def convert_level_lb_version_to_catext_version(level_lb_version):
    version_name = level_lb_versions[level_lb_version]
    version_name_major = version_name.split(".")[1]

    for api_id, catext_version in catext_versions.items():
        if catext_version.split(".")[1] == version_name_major:
            version_id = api_id
            break            
    else:
        raise RuntimeException()

    for api_id, catext_subversion in catext_subversions.items():
        if catext_subversion == version_name:
            subversion_id = api_id
            break
    else:
        raise RuntimeException()

    return version_id, subversion_id

def set_run_predefined_variable(run, variable, value):
    run["variables"][variable] = {"type": "pre-defined", "value": value}

def set_version_subversion(level_run, catext_run):
    if "jlzkwql2" not in level_run["values"]:
        print(f"Note: Run with id {level_run['id']} has no version")
        return

    level_version = level_run["values"]["jlzkwql2"]
    catext_version, catext_subversion = convert_level_lb_version_to_catext_version(level_version)
    set_run_predefined_variable(catext_run, "ylpm5erl", catext_version)
    set_run_predefined_variable(catext_run, "j846z5wl", catext_subversion)

level_difficulty_to_catext_difficulty = {
    "4lxg24q2":"21g22nnl", # Easy
    "8149mvqd":"jqzxxng1", # Normal
    "z19xe814":"klryy3jq", # Hard
    "p129j4lx":"21d33k4q"  # Hardcore
}

def set_run_difficulty(level_run, catext_run):
    if "9l737pn1" not in level_run["values"]:
        print(f"Note: Run with id {level_run['id']} has no difficulty")
        return

    level_difficulty = level_run["values"]["9l737pn1"]
    catext_difficulty = level_difficulty_to_catext_difficulty[level_difficulty]
    set_run_predefined_variable(catext_run, "0nwkeorn", catext_difficulty)

level_seed_type_to_catext_seed_type_template = collections.OrderedDict({
    "n2yzmeko": None, # Set Seed
    "7kjw7gd3": None, # Set Seed Glitchless
    "xk979xd0": None, # Random Seed
    "zd3re8dn": None, # Random Seed Glitchless
})

def generate_seed_type_map(conversion_table):
    return {
        "n2yzmeko": conversion_table[0], # Set Seed
        "7kjw7gd3": conversion_table[1], # Set Seed Glitchless
        "xk979xd0": conversion_table[2], # Random Seed
        "zd3re8dn": conversion_table[3], # Random Seed Glitchless
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

def create_new_run():
    return {"platform": "8gej2n93", "verified": False, "emulated": False, "variables": {}, "times": {}}

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

def transfer_runs_basic(api, level_id, catext_id, seed_type_variable, seed_types, extra_variables=None):
    level_runs = get_all_runs(api, f"runs?level={level_id}&max=200") # 5928n796
    catext_runs = get_all_runs(api, f"runs?category={catext_id}&max=200") # z27lj0gd
    catext_video_links = set()
    # enter_nether_seed_types = ("0135m63q", "0135m63q", "rqveryw1", "rqveryw1")

    for catext_run in catext_runs:
        if catext_run["status"]["status"] == "rejected":
            continue

        if catext_run["players"][0]["rel"] == "guest" and catext_run["players"][0]["name"] == "N/A":
            continue
        
        correct_variable_category = True

        if extra_variables is not None:
            for variable_value in extra_variables:
                if catext_run["values"][variable_value.variable] != variable_value.value:
                    correct_variable_category = False
                    break

        if not correct_variable_category:
            continue

        video_links = catext_run["videos"]["links"]
        #if len(video_links) != 1:
        #    raise RuntimeError(f"Found Category Extensions run with more than one link (run id: {catext_run['id']})")
        video_link = video_links[0]["uri"]
        catext_video_links.add(video_link)

    for run in level_runs:
        try:
            if run["status"]["status"] == "rejected" or run["status"]["status"] == "new":
                continue

            if run["players"][0]["rel"] == "guest" and run["players"][0]["name"] == "N/A":
                continue

            video_links = run["videos"]["links"]
            #if len(video_links) != 1:
            #    raise RuntimeError(f"Found Level run with more than one link (run id: {run['id']})")

            video_link = video_links[0]["uri"]

            if video_link in catext_video_links:
                print("Run with id %s already submitted" % run["id"])
                continue

            #print(f"Video link: {video_link}")

            run_date = run["date"]
            # fallback to submitted date, then verified date if a run has no date
            if run_date is None:
                run_date = run["submitted"]
                if run_date is None:
                    run_date = run["status"]["verify-date"]
                    if run_date is None:
                        raise RuntimeError(f"Run with id {run['id']} has no possible date to attach!")
                run_date = run_date.split("T")[0]

            run_to_submit = create_new_run()
            run_to_submit["category"] = catext_id # "z27lj0gd" # catext enter nether
            run_to_submit["date"] = run_date
            run_to_submit["video"] = video_link
    
            run_to_submit["times"]["realtime"] = run["times"]["realtime_t"]
            run_to_submit["times"]["ingame"] = run["times"]["ingame_t"]

            run_comment = run["comment"]
            if run_comment is None:
                run_comment = ""

            run_player_obj = run["players"][0]
            if run_player_obj["rel"] == "user":
                run_player_name = api.get_request(f"users/{run_player_obj['id']}")["names"]["international"]
            else:
                run_player_name = run_player_obj["name"]

            run_comment = run_player_name + "$" + run_comment

            run_to_submit["comment"] = run_comment

            set_version_subversion(run, run_to_submit)
            set_run_difficulty(run, run_to_submit)
            set_seed_type_simple(run, run_to_submit, seed_types, seed_type_variable) # "9l71q7ql"
            if extra_variables is not None:
                for variable_value in extra_variables:
                    set_run_predefined_variable(run_to_submit, variable_value.variable, variable_value.value)

            #set_run_predefined_variable(run_to_submit, "ylqkjo3l", "zqorkv5q")

            """
            allow_submit = False
            if run_player_obj["rel"] == "user" and not submitted_player:
                allow_submit = True
                submitted_player = True
            elif run_player_obj["rel"] == "guest" and not submitted_guest:
                allow_submit = True
                submitted_guest = True
            """

            run_to_submit = {"run": run_to_submit}
            response = api.post("runs", run_to_submit)
            if response.status_code != 201:
                print(response.json())
                raise RuntimeError()
        except:
            raise RuntimeError("Error! run: %s, run_to_submit: %s" % (run, run_to_submit))



def main():
    output = ""
    api = setup_api(api_key=API_KEY)
    # Enter Nether
    #transfer_runs_basic(api, level_id="5928n796", catext_id="z27lj0gd", seed_type_variable="9l71q7ql", seed_types=("0135m63q", "0135m63q", "rqveryw1", "rqveryw1"))

    """
    # All Swords
    transfer_runs_basic(api, level_id="n93nm2w0", catext_id="7dg4popd", seed_type_variable="yn21z528", seed_types=("5lem4xz1", "5lem4xz1", "0q5g53nl", "0q5g53nl"))
    # All Wood Logs
    transfer_runs_basic(api, level_id="ldyegrkw", catext_id="mkeqm06k", seed_type_variable="6njqg4jl", seed_types=("4lxe86r1", "4lxe86r1", "8147vwj1", "8147vwj1"))
    # Full Armor and 15 Levels
    transfer_runs_basic(api, level_id="ldy53pw3", catext_id="wk6vy5xd", seed_type_variable="ql64j7k8", seed_types=("gq7r4xyl", "jqzx53m1", "21g24pml", "klry022q"))
    # All Wool
    transfer_runs_basic(api, level_id="z98zmr9l", catext_id="5dw7zllk", seed_type_variable="kn0zqjo8", seed_types=("z1989pkq", "81pd05k1", "p12xw0kl", "xqkm4nyl"))
    # HDWGH
    transfer_runs_basic(api, level_id="gdrqzoz9", catext_id="xk987oy2", seed_type_variable="onv23j0l", seed_types=("gq7rrvvl", "jqzxxrg1", "21g22wnl", "klryyejq"))

    # Kill Wither
    transfer_runs_basic(api, level_id="5d7p1qdy", catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        extra_variables=(VariableValue(variable="dlo31yel", value="mlnz0odl"),))
    # Kill Elder Guardian
    transfer_runs_basic(api, level_id="kwj0g0dg", catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        extra_variables=(VariableValue(variable="dlo31yel", value="810wmd5q"),))
    # All Bosses
    transfer_runs_basic(api, level_id="owo8jjd6", catext_id="7kj1wexk", seed_type_variable="jlz51w0l", seed_types=("jq6zxe7l", "5lmg4m4l", "81w5d051", "zqor3v2q"),
        extra_variables=(VariableValue(variable="dlo31yel", value="9qjx48gl"),))

    # "e8mmkrq8" = item, "ylqkvm3l" = Structures option
    # Obtain Cake
    transfer_runs_basic(api, level_id="rw6lepw7", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        extra_variables=(VariableValue(variable="e8mmkrq8", value="gq7r46yl"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Golden Apple
    transfer_runs_basic(api, level_id="rdnlq5wm", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        extra_variables=(VariableValue(variable="e8mmkrq8", value="21g243ml"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Emerald
    transfer_runs_basic(api, level_id="xd023m9q", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        extra_variables=(VariableValue(variable="e8mmkrq8", value="jqzx5mm1"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    # Obtain Diamond
    transfer_runs_basic(api, level_id="29vl5qwv", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
        extra_variables=(VariableValue(variable="e8mmkrq8", value="xqkm4xyl"), VariableValue(variable="ylqkvm3l", value="klry0r2q")))
    """

    # Obtain Diamond (No Structures)
    #transfer_runs_basic(api, level_id="xd4yrqdm", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
    #    extra_variables=(VariableValue(variable="e8mmkrq8", value="xqkm4xyl"), VariableValue(variable="ylqkvm3l", value="21d3yejq")))

    players = {
        "players": [{
            "rel": "user", "id": "18ql617j"
        }]
    }

    response = api.put("runs/y816q7dz/players", players)
    print(response.json())

    # Obtain Emerald (No Structures)
    #transfer_runs_basic(api, level_id="ldyx1k93", catext_id="vdom79v2", seed_type_variable="gnxrkv6n", seed_types=("5q8d09kl", "5q8d09kl", "4qyjyw7q", "4qyjyw7q"),
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
