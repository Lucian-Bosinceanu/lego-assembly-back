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

voxels = [
    {
        "id": 0,
        "shape": None,
        "position": (0, 0, 0)
    },
    {
        "id": 1,
        "shape": None,
        "position": (1, 0, 0)
    },
    {
        "id": 2,
        "shape": None,
        "position": (0, 0, 2)
    }, 
    {
        "id": 3,
        "shape": None,
        "position": (0, 0, 5)
    },
    {
        "id": 4,
        "shape": None,
        "position": (2, 0, 1)
    }
]

def search(x, y, z):
    tuple_to_compare_to = (x, y, z)
    return next((x for x in voxels if x["position"] == tuple_to_compare_to), None)

def classify(x, y, z):
    rotations = ["0 deg", "90 deg", "180 deg", "270 deg"]
    for shape in SHAPES[::-1]:
        max_x = max(shape["like"], key=lambda x: x[0])[0]
        max_y = max(shape["like"], key=lambda x: x[1])[1]
        max_z = max(shape["like"], key=lambda x: x[2])[2]
        variations = [
            [
                [search(x + position[0] - xprime, y + position[1] - yprime, z + position[2] - zprime) for position in shape["like"]],
                [search(x + position[2] - xprime, y + position[1] - yprime, z + position[0] - zprime) for position in shape["like"]],
                [search(x - position[0] - xprime, y + position[1] - yprime, z - position[2] - zprime) for position in shape["like"]],
                [search(x - position[2] - xprime, y + position[1] - yprime, z - position[0] - zprime) for position in shape["like"]]
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
