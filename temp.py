import argparse
from src import utils
from src.utils import OutputType

parser = argparse.ArgumentParser()
parser.add_argument("--log")
args = parser.parse_args()

log = utils.load(args.log)
font = utils.load("resources/fonts/u8g2_5x7")
format_str = "images/text_{}.png"

texts = ["", "9", "a", "b", "c", "ca", "caa", "cab", "cac", "cas", "cat", "wiki_cat"]

screens = [req.values[0] for req in log.requests if req.data_type == OutputType.Screen]

for (screen, text) in zip(screens, texts):
    #text = screen.extract_text(font)
    im = screen.to_image()
    im.save(format_str.format(text))

