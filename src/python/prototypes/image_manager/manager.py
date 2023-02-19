import inspect
import itertools
import logging
import os
import re

import pygame

import util

"""
how image loading works

images/
  part_something
  # images.part_something

  part_0.png
  part_1.png
  part_2.png
  # images.part[0], part[1], part[2]

  # there is also a tile system support that I made
  # ask me if you need explanation

how sound loading works

audio/
  switch.ogg
  # audio.switch
  click.ogg
  # audio.click

  shout_1.ogg
  shout_2.ogg
  # audio.shout[0], shout[1]

"""

class ResourceManager:
    __organization_regex = re.compile(r"^(.+?)(?:_(\d+))?\.(\w+)$")
    __invalid_index_exception = Exception("Invalid image index")

    def __init__(self, folder=None, fallback=None, loader_func=None):
        if not folder:
            # Blank instance
            return
        if not loader_func:
            raise Exception("loader_func is required")
        if fallback:
            if isinstance(fallback, str):
                fallback = loader_func(os.path.join(folder, fallback))

        gen = None
        try:
            gen = next(os.walk(folder))
        except StopIteration:
            raise Exception(f"This folder does not exist {folder}")
        folders = gen[1]
        files = gen[2]

        for path in folders:
            if path.startswith("__") and path.endswith("__"):
                continue
            self.__setattr__(
                path,
                ResourceManager(
                    os.path.join(folder, path), fallback, loader_func=loader_func
                ),
            )

        file_groups = [
            m
            for name in files
            if (m := re.match(self.__organization_regex, name))
            or logging.warning(f"{folder} -> {name} is invalid. Ignoring...")
        ]

        for key, group in itertools.groupby(file_groups, lambda x: x.group(1)):
            if getattr(self, key, None):
                raise Exception(
                    f"{folder} -> {key} already exists. perhaps there is already a folder named {key} in this directory"
                )

            matches = list(group)
            if "py" in [m.group(3) for m in matches]:
                # There is a python file
                if len(matches) > 2:
                    raise Exception(
                        f'{folder} -> {key} should only be a pair (found multiple files starting with the name "{key}")'
                    )

                resource_file_list = [m.group(0) for m in matches if m.group(3) != "py"]
                if not resource_file_list:
                    logging.info(
                        f"{folder} -> {key} has no resource file (no file of same name that doens't end with .py)"
                    )
                    continue

                resource_file = resource_file_list[0]

                datafile = util.load_module(os.path.join(folder, key + ".py"))

                if datafile.TYPE == "SPRITE":
                    # Deal with sprite logic
                    dimensions = datafile.DIMENSIONS
                    if not dimensions:
                        raise Exception(
                            "{folder} -> {key}.py: Sprite must have dimensions specified"
                        )

                    width, height = dimensions

                    data = datafile.data

                    if not data:
                        raise Exception(
                            "{folder} -> {key}.py: A sprite info file must have a class data"
                        )

                    image = loader_func(os.path.join(folder, resource_file))

                    logging.debug(
                        f"Creating a new {type(self).__name__} for {key} as it was a folder"
                    )
                    store = type(self)()
                    self.__setattr__(key, store)

                    for attr, value in inspect.getmembers(
                        data, lambda a: not inspect.isroutine(a)
                    ):
                        if attr.startswith("__") and attr.endswith("__"):
                            continue

                        if not (isinstance(value, list) or isinstance(value, tuple)):
                            raise Exception(
                                f"{folder} -> {key}.py: {attr} must be a list or tuple"
                            )

                        if len(value) < 2:
                            raise Exception(
                                f"{folder} -> {key}.py: {attr} must have at least 2 elements"
                            )
                        elif len(value) == 2:
                            # tile at location
                            logging.debug(
                                f"{type(self).__name__} loaded image {attr} for {key}.{attr}"
                            )
                            store.__setattr__(
                                attr,
                                util.splice_image(
                                    image, width, height, value[0], value[1]
                                ),
                            )
                        elif len(value) == 4:
                            # tile array
                            idx = 0
                            l = [
                                self.__invalid_index_exception
                                for i in range(
                                    (value[2] - value[0]) * (value[3] - value[1])
                                )
                            ]
                            for x in range(value[0], value[2]):
                                for y in range(value[1], value[3]):
                                    x_loc = x * width
                                    y_loc = y * height
                                    l[idx] = util.splice_image(
                                        image, width, height, x_loc, y_loc
                                    )
                                    idx += 1
                            logging.debug(
                                f"{type(self).__name__} loaded an array of {len(l)} images for {key}.{attr}"
                            )
                            store.__setattr__(
                                attr,
                                l,
                            )
                        else:
                            raise Exception(
                                f"{attr} must have either 2 (single tile) or 4 (array of elements)"
                            )
                else:
                    raise Exception(f"{datafile.TYPE} is not a valid resource type")
                continue

            count = len(matches)
            if count == 0:
                continue
            elif count == 1:
                match = matches[0]
                logging.debug(f"{type(self).__name__} loaded resources for {key}")
                self.__setattr__(key, loader_func(os.path.join(folder, match.group(0))))
            else:
                l = [
                    self.__invalid_index_exception
                    for _ in range(
                        max(int(m.group(2)) for m in matches if m.group(2) is not None)
                        + 1
                    )
                ]
                logging.debug(
                    f"{type(self).__name__} loaded an array of {len(l)} resources for {key}"
                )
                self.__setattr__(key, l)
                for match in matches:
                    l[int(match.group(2))] = loader_func(
                        os.path.join(folder, match.group(0))
                    )


class ImageManager(ResourceManager):
    def __init__(self, folder, fallback=None):
        super().__init__(
            folder, fallback, loader_func=util.debug_arguments(pygame.image.load)
        )


class PygameSoundManager(ResourceManager):
    def __init__(self, folder, fallback=None):
        super().__init__(
            folder, fallback, loader_func=util.debug_arguments(pygame.mixer.Sound)
        )
