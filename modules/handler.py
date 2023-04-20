from .formatter import Colorate, Colors

def log(log):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"""{log}"""))