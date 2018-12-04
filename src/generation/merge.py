from operator import itemgetter
import src.input_output.model as model
import src.input_output.cubedata as cube

SHAPES = [
    {
        'id': 0,
        'name': '1x1',
        'like': [(0, 0, 0)]
    },
    {
        'id': 1,
        'name': '1x2',
        'like': [(0, 0, 0), (0, 0, 1)]
    },
    {
        'id': 2,
        'name': '1x3',
        'like': [(0, 0, 0), (0, 0, 1), (0, 0, 2)]
    },
    {
        'id': 3,
        'name': '1x4',
        'like': [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3)]
    },
    {
        'id': 4,
        'name': '2x2',
        'like': [(0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1)]
    },
    {
        'id': 5,
        'name': '2x3',
        'like': [(0, 0, 0), (0, 0, 1), (0, 0, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2)]
    },
    {
        'id': 6,
        'name': '2x4',
        'like': [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3)]
    }
]

def search(voxels, x, y, z):
    tuple_to_compare_to = (x, y, z)
    return next((x for x in voxels if x["position"] == tuple_to_compare_to and x["shape"] is None), None)

def classify(voxels, x, y, z):
    rotations = ["0 deg", "90 deg", "180 deg", "270 deg"]
    for shape in SHAPES[::-1]:
        max_x = max(shape["like"], key=lambda x: x[0])[0]
        max_y = max(shape["like"], key=lambda x: x[1])[1]
        max_z = max(shape["like"], key=lambda x: x[2])[2]
        variations = [
            [
                [search(voxels, x + position[0] - xprime, y + position[1] - yprime, z + position[2] - zprime) for position in shape["like"]],
                [search(voxels, x + position[2] - xprime, y + position[1] - yprime, z + position[0] - zprime) for position in shape["like"]],
                [search(voxels, x - position[0] - xprime, y + position[1] - yprime, z - position[2] - zprime) for position in shape["like"]],
                [search(voxels, x - position[2] - xprime, y + position[1] - yprime, z - position[0] - zprime) for position in shape["like"]]
            ]
            for xprime in range(0, max_x + 1) for yprime in range(0, max_y + 1) for zprime in range(0, max_z + 1)
        ]
        result = next(
            ((shape, rotations[variation.index(solution)], solution)
                for variation in variations for solution in variation if None not in solution),
            None
        )
        if result is not None:
            return result

def merge_cubes(model: model):
    voxels = []
    for x in model.cubes:
        for y in model.cubes[x]:
            for z in model.cubes[x][y]:
                voxels.append({
                    "id": model.cubes[x][y][z].id,
                    "color": model.cubes[x][y][z].color,
                    "shape": None,
                    "position": (x, y, z),
                    "reference": model.cubes[x][y][z]
                })

    voxels.sort(key=itemgetter("position"))
    recognisedShapes = []
    for voxel in voxels:
        if voxel["shape"] is None:
            result = classify(voxels, voxel["position"][0], voxel["position"][1], voxel["position"][2])
            if result is not None:
                for recognisedVoxel in result[2]:
                    recognisedVoxel["shape"] = result[0]["id"]
                recognisedShapes.append(result)

    return recognisedShapes
