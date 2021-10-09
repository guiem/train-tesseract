import sys
import pytesseract
from difflib import SequenceMatcher as SQ

try:
    from PIL import Image
except ImportError:
    import Image


lang = sys.argv[1]

img_path = '/app/data/validation/0.tif'
img = Image.open(img_path)
raw_text = pytesseract.image_to_string(img, lang=lang, config='--psm 7')  # make sure to change your `config` if different 
target = "The computers are becoming sentient,"
print(f"Output: {raw_text}\nPercent coincidence: {round(SQ(None, target, raw_text).ratio()*100,2)}%")
