dtype_mappings = [
    {"PostgreSQL": "INTEGER", "SQLAlchemy": "Integer", "Python": "int"},
    {"PostgreSQL": "INT", "SQLAlchemy": "Integer", "Python": "int"},
    {"PostgreSQL": "VARCHAR", "SQLAlchemy": "String", "Python": "string"},
    {"PostgreSQL": "BOOLEAN", "SQLAlchemy": "Boolean", "Python": "bool"},
    {"PostgreSQL": "FLOAT", "SQLAlchemy": "Decimal", "Python": "float"},
    {"PostgreSQL": "DATE", "SQLAlchemy": "Date", "Python": "date"},
    {"PostgreSQL": "TIMESTAMP", "SQLAlchemy": "DateTime", "Python": "date"},
    {"PostgreSQL": "TIME", "SQLAlchemy": "Time", "Python": "date"},
    {"PostgreSQL": "JSONB", "SQLAlchemy": "JSON", "Python": "json"},
    {"PostgreSQL": "ENUM", "SQLAlchemy": "Enum", "Python": "enum"},
    {"PostgreSQL": "BYTEA", "SQLAlchemy": "LargeBinary", "Python": "binary"},
    {"PostgreSQL": "INTERVAL", "SQLAlchemy": "Interval", "Python": "interval"},
]


# Function to get data type mappings based on key

def get_dict_key(dict, key, value):
    found_dict = {}
    for dtype_mapping in dict:
        if dtype_mapping[key] in value:
            found_dict = dtype_mapping
            break

    return found_dict

# eg get_dict_key("SQLAlchemy", "JSON") or get_dict_key("PostgreSQL", "DATE")
#a = get_dict_key(dtype_mappings, "PostgreSQL", "DATE")
#print("a ", a)
#b = a.get("Python")
#print("b ", b)

