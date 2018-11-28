import json
from pprint import pprint

# this script checks:
# 1. if every cube has a neighbour
# 2. if all Y coordinates are POSITIVE

# examples of calls at the end of file


def check_limits(limits):
    if limits["min_y"] < 0:
        print("You have a cube with negative y value: ", limits["min_y"])
        return False
    return True


def init_limits(limits, model):
    limits["min_x"] = model["cubes"][0]["x"]
    limits["max_x"] = model["cubes"][0]["x"]
    limits["min_y"] = model["cubes"][0]["y"]
    limits["max_y"] = model["cubes"][0]["y"]
    limits["min_z"] = model["cubes"][0]["z"]
    limits["max_z"] = model["cubes"][0]["z"]


def put_limits(limits, model):
    for cube in model["cubes"]:
        if cube["x"] > limits["max_x"]:
            limits["max_x"] = cube["x"]
        if cube["x"] < limits["min_x"]:
            limits["min_x"] = cube["x"]
        if cube["y"] > limits["max_y"]:
            limits["max_y"] = cube["y"]
        if cube["y"] < limits["min_y"]:
            limits["min_y"] = cube["y"]
        if cube["z"] > limits["max_z"]:
            limits["max_z"] = cube["z"]
        if cube["z"] < limits["min_z"]:
            limits["min_z"] = cube["z"]


def check_neighbour(model, i, j):
    # to be neighbour, it has to be only on one plane moved, only by 1 block.
    x_sub = abs(model["cubes"][i]["x"] - model["cubes"][j]["x"])
    y_sub = abs(model["cubes"][i]["y"] - model["cubes"][j]["y"])
    z_sub = abs(model["cubes"][i]["z"] - model["cubes"][j]["z"])
    # print("i",i,"j", j,"x_sub + y_sub + z_sub", x_sub + y_sub + z_sub)
    if 1 == x_sub + y_sub + z_sub:
        print("cube", i, "has cube", j, "as neighbour")
        return True
    return False


def lego_model_validator(path=None):
    print("this is lego model validator")
    if path is None:
        path = "figuriAI/figura2.json"
    limits = dict(min_x=None, min_y=None, min_z=None, max_x=None, max_y=None, max_z=None)
    try:
        with open(path) as f:
            model = json.load(f)
            init_limits(limits, model)
        pprint(model)
    except Exception as e:
        print(e)

    put_limits(limits, model)

    if check_limits(limits)== False:
        print("wtf")
        return False

    if len(model["cubes"]) == 1: return True

    for i in range(0, len(model["cubes"])):
        has_neighbour = False
        for j in range(0, len(model["cubes"])):
            if check_neighbour(model, i, j):
                has_neighbour = True
                # i = i+2
                break

        if not has_neighbour:
            print("cube on line ", i, "has no neighbours")
            return False
    print("check complete, shape is valid")
    return True
# call it like this
# lego_model_validator()

# or like this
# lego_model_validator("figura10.json")


#or with absolute path
lego_model_validator("C:\\Users\\Catalin\\Desktop\\figuriAI\\figura15.json")
