import os
from typing import Iterable
from app import app


class ImageLoader(Iterable):
    def __init__(self, debug=True) -> None:
        self.debug = debug

    def __iter__(self):
        if self.debug:
            file_list = os.listdir(app.config["RAWIMAGES"])
            for filename in file_list:
                yield os.path.join(app.config["RAWIMAGES"], filename)
