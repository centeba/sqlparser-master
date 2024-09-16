import re
import os


SQL_REG_EX = r'CREATE\s+TABLE\s+[\w\W]+?\);'

ifile  = open("wma0_1 schema.sql", "r")
sql_text = ifile.read()
ifile.close()

create_table_regex = re.compile(SQL_REG_EX, re.DOTALL | re.IGNORECASE | re.MULTILINE)

create_table_statements = create_table_regex.findall(sql_text)

if create_table_statements:
    for statement in create_table_statements:
        print("\n============\n")
        print(statement.strip())
        print(f"\n============\n")
else:
    print("No CREATE TABLE statements found.")