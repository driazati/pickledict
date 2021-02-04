# pickledict

`pickledict`/`jsondict` and `picklelist`/`jsonlist` are auto-saving wrappers around their contained types. Their API is the same as the underlying type, `dict` or `list`, but writes are recorded to a file and are transparently re-loaded on subsequent runs.

```python
from pickledict import jsondict

my_dict = jsondict(some_key="a value")

# Writes and modifications are automatically recorded and saved
my_dict["dog"] = 1
my_dict["dog"] += 1

print(my_dict)
```

```bash
# The first invocation creates a save file for the dict
$ python example.py
{'some_key': 'a value', 'another_key': 1}

# The data is saved to a file named: <filename>-<lineno>-<variable name>.json
$ cat .pickledict/example-3-my_dict.json
{"some_key": "a value", "dog": 2}

# A second invocation reads the saved file on construction
$ python example.py
{'some_key': 'a value', 'another_key': 2}

# As does a third, etc.
$ python example.py
{'some_key': 'a value', 'another_key': 3}
```

## Installation

```bash
# requires Python 3.6+
pip install pickledict
```

## Usage

`dict`s can be saved with either JSON or Python's pickle format (Pickle supports the preservation of certain things JSON does not, such as non-string keys).

All of `pickledict`, `jsondist`, `picklelist`, and `jsonlist` support the same constructor arguments:

- `file_name` (`str`) - explicitly specify the file name to save this object in (if not provided one will be generated from the assigned variable name if possible)
- `save_on_every_write` (`bool`) - save on every modification of the structure. Turning this off saves only on program exit (which may increase performance)
- `serializer_args` (`Dict[str, Any]`) - keyword arguments to pass to the relevant serialization `dump` function

They all each add one method: `detach()` which disconnects the in-memory object from the file on disk so it can be manipulated without worrying about affecting the underlying file.

## Use Cases

Fetch data from a remote source and store it locally automatically without dealing directly with serialization:

Without `pickledict`:

```python
import json
import os

if os.path.exists("db.json"):
    with open("db.json", "r") as f:
        local_db = json.load(f)
else:
    local_db = {}

for i in range(100):
    key, data = fetch_some_data(i)

    local_db[key] = data

    with open("db.json", "w") as f:
        json.dump(local_db, f, indent=2)
```

With `pickledict`:

```python
from pickledict import jsondict

local_db = jsondict(file_name="db.json", serializer_args={"indent": 2})

for i in range(100):
    key, data = fetch_some_data(i)

    # This will automatically persist the data out to disk
    local_db[key] = data
```
