import sys

def arguments() -> str:
    try: 
        variants = ["genetic", "greedy"]
        algorithm = str(sys.argv[2]).lower()
        if algorithm not in variants:
            print("Usage:", "\n", "python main.py <file path> <genetic/greedy>")
            exit()
        else:
            return algorithm
    except:
        print("Usage:", "\n", "python main.py <file path> <genetic/greedy>")
        exit()
