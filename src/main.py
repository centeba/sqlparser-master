from cparser import cParser as cp
from clexer import lexer1 as lx
import col_formats as cf

import makejinja2
import re
import os



    

    #input_string = "CREATE TABLE Account (system_id  int NOT NULL, f1 varchar (256), f2 char (256), f3 date, f4 INT(12), f5 boolean DEFAULT TRUE, CONSTRAINT pk_client_info PRIMARY KEY (system_id), CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ) ) ; "
input_string = "CREATE  TABLE c_user_info ( system_id   int  NOT NULL  , first_name  varchar(256)  NOT NULL  , last_name varchar(256)  NOT NULL  , 	mobile_number  varchar(24) , mobile_country_code  INTEGER , 	CONSTRAINT pk_user_info PRIMARY KEY ( system_id ) ) ; "

print("\n============\n"+input_string)
   # input_string= "CREATE TABLE c_client_info (client_id  int NOT NULL, client_name varchar(100), PRIMARY KEY (client_id), CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id) )) ; "
   # input_string= "CREATE TABLE c_client_info (client_id  INTEGER NOT NULL, client_name varchar(100), PRIMARY KEY (client_id), CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ) ) ; "

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

                tokens = lx(statement.strip())
                print("tokens", tokens)
                parser = cp(tokens)
                columns = []
                table_name, columns = parser.parse()

                print("Table Name:", table_name)
                print("Columns:", columns, len(columns))
                col_list = []
                col_list = cf.build_col_dict(columns)
                print("final list", col_list)
                makejinja2.make_jinja_objects(table_name, col_list)

                print(f"\n============\n")
else:
        print("No CREATE TABLE statements found.")

