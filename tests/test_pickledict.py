import pickle
import os
import unittest
import json
import shutil
from pickledict import pickledict, jsondict  # , picklelist, jsondict, jsonlist


class TestPickleDict(unittest.TestCase):
    def setUp(self) -> None:
        # Clear out any previously existing files so the test is fresh every
        # time
        if os.path.exists(".pickledict"):
            shutil.rmtree(".pickledict")

        # other_files = [
        #     "test.pkl"
        # ]

        # [os.remove(f) for f in other_files if os.path.exists(f)]

        return super().setUp()

    def explicit_name_test(self, cls, mode, serializer):
        some_value = cls(file_name="test.pkl")

        # Check that the explicit file name was used
        expected_name = "test.pkl"
        self.assertTrue(os.path.exists(expected_name))

        # Write a value and expect it to be in the file
        some_value["meow"] = "woof"
        with open(expected_name, mode) as f:
            self.assertEqual(f.read(), serializer.dumps(some_value))

        # Check that the data is correctly re-loaded
        some_value = cls(file_name="test.pkl")
        self.assertEqual(some_value, {"meow": "woof"})

    def test_jsondict_explicit_name(self):
        self.explicit_name_test(jsondict, "r", json)

    def test_pickledict_explicit_name(self):
        self.explicit_name_test(pickledict, "rb", pickle)

    def atexit_test(self, cls, mode, serializer, extension):
        some_value = cls(save_on_every_write=False)

        # Check that the name 'some_value' was correctly extracted and the file
        # was actually saved
        expected_name = os.path.join(
            ".pickledict", f"test_pickledict-47-some_value.{extension}")
        self.assertTrue(os.path.exists(expected_name))

        # Write a value and expect it to be in the file
        some_value["meow"] = "woof"
        with open(expected_name, mode) as f:
            self.assertNotEqual(f.read(), serializer.dumps(some_value))

    def test_jsondict_atexit(self):
        self.atexit_test(jsondict, "r", json, "json")

    def test_pickledict_atexit(self):
        self.atexit_test(pickledict, "rb", pickle, "pkl")


if __name__ == "__main__":
    unittest.main()
