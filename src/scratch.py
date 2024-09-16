from jinja2 import Environment, FileSystemLoader

table_name = "account"

columns = [
    {"colname": "col_f1", "coltype": "int", "dim": "null", "nullable": "False", "unique": "True", "pkey": "True"},
    {"colname": "col_f2", "coltype": "varchar", "dim": 256, "nullable": "True", "unique": "False", "pkey": "False"},
    {"colname": "col_f3", "coltype": "text", "dim": "null", "nullable": "True", "unique": "False", "pkey": "False"},
    {"colname": "col_f4", "coltype": "date", "dim": "null", "nullable": "True", "unique": "False", "pkey": "False"},
    {"colname": "col_f5", "coltype": "boolean", "dim": "null", "nullable": "False", "unique": "False", "pkey": "False"},
    {"colname": "col_f6", "coltype": "float", "dim": "null", "nullable": "True", "unique": "False", "pkey": "False"},
    {"colname": "col_f7", "coltype": "timestamp", "dim": "null", "nullable": "False", "unique": "False",
     "pkey": "False"},
    {"colname": "col_f8", "coltype": "time", "dim": "null", "nullable": "False", "unique": "False", "pkey": "False"},
    {"colname": "col_f9", "coltype": "json", "dim": "null", "nullable": "False", "unique": "False", "pkey": "False"},
]

#context dictionary
context = {
    "True": "True",
    "False": False,
    "table_name": table_name,
    "columns": columns
}

env = Environment(loader=FileSystemLoader("./templates/"),
                  trim_blocks=True,
                  lstrip_blocks=True)

template = env.get_template("build_alchemy.csv")
filename = f"./models/db/{table_name}_sqla.py"

with open(filename, mode="w", encoding="utf-8") as output:
    output.write(template.render(context))

template = env.get_template("build_pydantic.csv")
filename = f"./models/db/{table_name}_pyd.py"

with open(filename, mode="w", encoding="utf-8") as output:
    output.write(template.render(context))

item_id=table_name + "_id"
print("item id: ", item_id)
#context dictionary
context = {
    "table_name": table_name,
    "item_id": item_id
}

template = env.get_template("build_fastapi.csv")
filename = f"./models/db/{table_name}_fapi.py"

with open(filename, mode="w", encoding="utf-8") as output:
    output.write(template.render(context))