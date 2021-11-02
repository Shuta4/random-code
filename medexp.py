#!/usr/bin/python

"""
Converts .ods table like:
| Дата         | Часть дня   | Лекарство | Сделано |
|--------------|-------------|-----------|---------|
| <yyyy-mm-dd> | <date_part> | <name>    | <1/0>   |

to 'BASE_DIR/<yyyy-mm-dd>.md' files with following structure:
# <yyyy-mm-dd>
## <date_part>
- [<if 1: "x" else: " ">] <name>
- [<if 1: "x" else: " ">] <name>
...

## <date_part>
- [<if 1: "x" else: " ">] <name>
- [<if 1: "x" else: " ">] <name>
...

...

"""

import os
from pandas_ods_reader import read_ods

path_in = "/path/to/file.ods"
path_out = "/path/for/md/files"

df = read_ods(path_in, "list")

files_data = {}

for el in df.iterrows():
    data = el[1]

    date = data["Дата"]
    part = data["Часть дня"]
    name = data["Лекарство"]
    done = data["Сделано"] == 1

    if files_data.get(date) is None:
        files_data[date] = {}

    if files_data[date].get(part) is None:
        files_data[date][part] = []

    files_data[date][part].append({
        "name": name,
        "done": done
    })

for date in files_data:
    f = open(os.path.join(path_out, f"{date}.md"), "w")

    content = f"# {date}"

    for part in files_data[date]:
        content = f"{content}\n## {part}"

        for med in files_data[date][part]:
            check = " "
            if med["done"]:
                check = "x"
            content = f"{content}\n- [{check}] {med['name']}"

        content = f"{content}\n"

    f.write(content)
    f.close()
