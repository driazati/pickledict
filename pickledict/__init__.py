import warnings
import dis
import pickle
import json
import os
import atexit
import inspect

from typing import Dict, Any

from pickledict.dict import SerializedDict
from pickledict.list import SerializedList


def frames_up(n):
    # Offset by one to include this function call
    i = -1

    frame = inspect.currentframe()
    while i < n:
        frame = frame.f_back
        i += 1

    return frame


name_index = 0
seen_names = set()


class Loader:
    def __init__(self, save_on_every_write: bool = True, file_name: str = None, serializer_args: Dict[str, Any] = None, *args, **kwargs):
        if not os.path.exists(".pickledict"):
            os.mkdir(".pickledict")
        if file_name is None:
            file_name = os.path.join(".pickledict", self.get_name())
            if file_name in seen_names:
                warnings.warn(
                    f"The auto-generated file name '{file_name}' has already been used "
                    f"for this {self.__class__.__name__}"
                    f", please use {self.__class__.__name__}'s 'file_name' argument or you will get"
                    " incorrect data", stacklevel=2)
            seen_names.add(file_name)
        self.file_name = file_name

        self.save_on_every_write = save_on_every_write
        if serializer_args is None:
            serializer_args = {}
        self.serializer_args = serializer_args
        self.detached = False

        if not self.save_on_every_write:
            def exit_save():
                self.serialize()

            atexit.register(exit_save)

        if os.path.exists(file_name):
            try:
                deserialized = self.deserialize()
                super().__init__(deserialized)
            except:
                super().__init__(*args, **kwargs)
                self.serialize()
        else:
            super().__init__(*args, **kwargs)
            self.serialize()

    def detach(self):
        self.detached = True

    def generate_name(self, extension):
        try:
            f = frames_up(3)
            remaining_instructions = [x for x in dis.get_instructions(
                f.f_code) if x.offset > f.f_lasti]
            if len(remaining_instructions) > 0:
                maybe_store = remaining_instructions[0]
                if maybe_store.opname.startswith("STORE_"):
                    dest_var = maybe_store.argval
                    file_name = os.path.basename(f.f_code.co_filename)
                    if file_name.endswith(".py"):
                        file_name = file_name[:-len(".py")]

                    return f"{file_name}-{f.f_lineno}-{dest_var}.{extension}"
        except Exception as e:
            pass

        global name_index
        name_index += 1
        warnings.warn(
            f"Could not determine a name for this {self.__class__.__name__}"
            f", please use the 'file_name' argument or any changes"
            " to the order of pickledicts in your program will cause"
            " corrupted data", stacklevel=4)
        return f"{self.__class__.__name__}-{name_index}.{extension}"

    def checked_serialize(self):
        if not getattr(self, "detached", False) and \
                getattr(self, "save_on_every_write", False):
            self.serialize()


class PickleSerializer:
    def get_name(self) -> str:
        return Loader.generate_name(self, "pkl")

    def serialize(self) -> None:
        with open(self.file_name, "wb") as f:
            pickle.dump(self, f, **getattr(self, 'serializer_args', {}))

    def deserialize(self) -> Dict[Any, Any]:
        with open(self.file_name, "rb") as f:
            return pickle.load(f)


class JsonSerializer:
    def get_name(self) -> str:
        return Loader.generate_name(self, "json")

    def serialize(self) -> None:
        with open(self.file_name, "w") as f:
            json.dump(self, f, **getattr(self, 'serializer_args', {}))

    def deserialize(self) -> Dict[Any, Any]:
        with open(self.file_name, "r") as f:
            return json.load(f)


class pickledict(Loader, PickleSerializer, SerializedDict):
    pass


class jsondict(Loader, JsonSerializer, SerializedDict):
    pass


class picklelist(Loader, PickleSerializer, SerializedList):
    pass


class jsonlist(Loader, JsonSerializer, SerializedList):
    pass
