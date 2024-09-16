
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
true="True"
false="False"

def make_jinja_objects(table_name, columns):

    context = {
        "columns": columns,
        "table_name": table_name,
        "true": true,
        "false": false,
    }

    env = Environment(loader=FileSystemLoader("./templates/"))
    template = env.get_template("build_alchemy.csv")

    filename = Path(f"./db/models/F_{table_name}/{table_name}.py")
    filename.parent.mkdir(exist_ok=True, parents=True)

    with open(filename, mode="w", encoding="utf-8") as output:
        output.write(template.render(context))



    template = env.get_template("build_pydantic.csv")
    filename.parent.mkdir(exist_ok=True, parents=True)
    filename = Path(f"./db/models/F_{table_name}/{table_name}_pyd.py")

    with open(filename, mode="w", encoding="utf-8") as output:
        output.write(template.render(context))

    item_id = table_name + "_id"
    # context dictionary
    context = {
        "table_name": table_name,
        "item_id": item_id
    }

    template = env.get_template("build_fastapi.csv")
    filename.parent.mkdir(exist_ok=True, parents=True)
    filename = Path(f"./db/models/F_{table_name}/{table_name}_fapi.py")

    with open(filename, mode="w", encoding="utf-8") as output:
        output.write(template.render(context))
    
    template = env.get_template("build_base.csv")
    filename.parent.mkdir(exist_ok=True, parents=True)
    filename = Path(f"./db/models/base2.py")

    with open(filename, mode="a", encoding="utf-8") as output:
        output.write(template.render(context))

