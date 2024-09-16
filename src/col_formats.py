import re

def build_one_col(cur_cols, col_key, col_val):
    if len(cur_cols) == 0:
        d1 = {}
        c1 = [(col_key, col_val)]
        d1 = dict(c1)
        return d1
    else:
        d1 = {}
        c1 = [(col_key, col_val)]
        d1 = dict(c1)
        cur_cols.update(d1)
        return cur_cols


def build_col_jinja_dict(cur_list, new_list):
    if len(cur_list) == 0:
        cur_list.append(new_list)
    else:
        cur_list.extend(new_list)

    return cur_list

def build_col_dict(columns):

    col_labels = ["colname", "coltype", "dim", "nullable", "default", "pkey"]
    col_labels_constraint = ["colname", "constraint", "dim", "nullable", "default"]

    col_list = []
    i = 0
    const=''
    for c in columns:
        if(c[0] == 'PRIMARY'):
           const = c[2]
           pkey_tokens = const.split(",")
           print( "const<<<>>>", const)

    for col in columns:
        k=0
        col_temp = []
        temp_list = {}
        
        print(" build_col_dict ", col[0])
        temp_list = build_one_col(temp_list, col_labels[0], col[0])
         
        print(" PKey>>>>: ", col[0])  
        
        
        if col[0]!='CONSTRAINT' and col[0]!='PRIMARY' and  col[0]!='fkeys':
            print(" nullable>>>>: ", col[3])
            temp_list = build_one_col(temp_list, col_labels[1], col[1])
            temp_list = build_one_col(temp_list, col_labels[2], col[2])
            temp_list = build_one_col(temp_list, col_labels[3], col[3])
            temp_list = build_one_col(temp_list, col_labels[4], col[4])
            print(" IN Col Format temp list ", col[0] + " : "+col[5])
            if(col[0] in pkey_tokens):
              temp_list = build_one_col(temp_list, col_labels[5], 'True')
            else:
              temp_list = build_one_col(temp_list, col_labels[5], 'False')
        else:
            temp_list = build_one_col(temp_list, col_labels_constraint[1], col[1])
            if(col[0]=='fkeys'):
                temp_list = build_one_col(temp_list, "Reference", col[2])
            else:
                temp_list = build_one_col(temp_list, "pKey", col[2]) 

        print(" temp list>>>>: ", temp_list)

        if i == 0:
            col_temp = build_col_jinja_dict(col_temp, temp_list)
            col_list = col_temp
            print("get_cols_from_tokens: build columns: i = ", i, col_temp, col_list)
            i += 1
        else:
            col_temp = build_col_jinja_dict(col_temp, temp_list)
            col_list = build_col_jinja_dict(col_list, col_temp)
            print("get_cols_from_tokens: build columns: i = ", i, col_temp, col_list)

            temp_list = {}

    return col_list

