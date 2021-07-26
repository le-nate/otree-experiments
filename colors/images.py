"""
Utilities to generate and manipulate images
"""
from pathlib import Path
from io import BytesIO
from base64 import b64encode

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import sys

    sys.tracebacklimit = 0
    raise SystemExit(
        f"FAILURE: Missing imaging library required in `{__name__}`\nYou need to install it using `pip install Pillow`"
    )


TEXT_SIZE = 32
IMAGE_WIDTH = 32 * 8
IMAGE_HEIGHT = 32 * 2
TEXT_PADDING = TEXT_SIZE
TEXT_FONT = Path(__file__).parent / "FreeSansBold.otf"


def generate_image(text, color):
    dumb = Image.new("RGB", (0, 0))
    font = ImageFont.truetype(str(TEXT_FONT), TEXT_SIZE)
    # take maximal size to keep all images same
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))
    draw = ImageDraw.Draw(image)
    draw.text(
        (IMAGE_WIDTH / 2, IMAGE_HEIGHT / 2), text, font=font, anchor="mm", fill=color
    )
    return image


def encode_image(image):
    buf = BytesIO()
    image.save(buf, "PNG")
    buf64 = b64encode(buf.getvalue())
    datauri = b"data:text/plain;base64," + buf64
    return datauri.decode("ascii")
