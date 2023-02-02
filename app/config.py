from pathlib import Path

def take_me_root():
    root_path = Path(__file__).resolve().parent.parent.joinpath()
    return root_path

# print(root)