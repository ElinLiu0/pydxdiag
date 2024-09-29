import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from pydxdiag.DxdiagParser import DxdiagParser

parser = DxdiagParser()

print(parser.model_dump_json("./output.json"))