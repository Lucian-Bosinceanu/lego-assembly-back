import json
import src.input_output.model as model
import src.input_output.cubedata as cube

def read_shapes() -> dict:
    """
    Reads shapes from the provided shape dictionary
    """
    with open("scLego.json", "r") as file:
        data = file.read()
        return json.loads(data)["pieces"]

def build_convenient_input(model: model) -> list:
    """
    Builds a structure that can easily be used by the merge algorithm
    """
    voxels = []
    for x in model.cubes:
        for y in model.cubes[x]:
            for z in model.cubes[x][y]:
                voxels.append({
                    "classified": False,
                    "position": (x, y, z),
                    "reference": model.cubes[x][y][z]
                })

    voxels.sort(key=lambda x: (x["position"][0], x["position"][1], x["position"][2]))
    return voxels

def search(voxels: dict, x: int, y: int, z: int) -> tuple:
    """
    Checks if the voxel at position x, y, z was classified or not.
    """
    tuple_to_compare_to = (x, y, z)
    return next((x for x in voxels if x["position"] == tuple_to_compare_to and x["classified"] is False), None)

def classify(SHAPES: list, voxels: list, x: int, y: int, z: int) -> tuple:
    """
    Idea:
    
    This algorithm does the following:
    1. Pick the largest shape from the provided shape dictionary (usually 2x8)
    2. Tries to match the picked shape with with the voxels provided
    3. If the shape is not matched by any combination (position, rotation), try the next largest shape from the dictionary
       Else, return the given shape and the voxels that matched the pattern from the picked shape
    """
    for shape in SHAPES[::-1]:
        max_x = max(shape["structure"], key=lambda x: x["x"])["x"]
        max_y = max(shape["structure"], key=lambda x: x["y"])["y"]
        max_z = max(shape["structure"], key=lambda x: x["z"])["z"]
        variations = [
            [
                [search(voxels, x + position["x"] - xprime, y + position["y"] - yprime, z + position["z"] - zprime) for position in shape["structure"]],
                [search(voxels, x + position["z"] - xprime, y + position["y"] - yprime, z + position["x"] - zprime) for position in shape["structure"]],
                [search(voxels, x - position["x"] - xprime, y + position["y"] - yprime, z - position["z"] - zprime) for position in shape["structure"]],
                [search(voxels, x - position["z"] - xprime, y + position["y"] - yprime, z - position["x"] - zprime) for position in shape["structure"]]
            ]
            for xprime in range(0, max_x + 1) for yprime in range(0, max_y + 1) for zprime in range(0, max_z + 1)
        ]
        result = next(
            ((shape, solution)
                for variation in variations for solution in variation if None not in solution),
            None
        )
        if result is not None:
            return result
    return None

def merge_pieces(SHAPES: dict, voxels: list) -> list:
    """
    Merges the cubes
    """
    recognised_shapes = []
    for voxel in voxels:
        if voxel["classified"] is False:
            result = classify(SHAPES, voxels, voxel["position"][0], voxel["position"][1], voxel["position"][2])
            if result is not None:
                for recognised_voxel in result[1]:
                    recognised_voxel["classified"] = True
                    recognised_voxel["reference"].id = len(recognised_shapes)
                recognised_shapes.append(result)

    return recognised_shapes

def merge_cubes(model: model) -> dict:
    """
    Entry point for this module. Does the following:
    1. Read the shapes from a dictionary
    2. Builds a list of voxels, with their position included, and sets the classified variable to false
    3. Applies the classification algorithm on all the 'available' voxels
    3.1 Sets the id shape of the voxel to the id of the discovered shape
    4. Returns the result
    """
    SHAPES = read_shapes()
    voxels = build_convenient_input(model)
    result = merge_pieces(SHAPES, voxels)

    return result
