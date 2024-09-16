import re

import col_formats as cf
from clexer import lexer1 as lexer

# Parser
class cParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        #self.advance()
        self.current_token = self.tokens[self.index]

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = "None"
        print("in advance", self.current_token, self.index)
    def match(self, expected_token):
        if self.current_token[0] == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Syntax error: Expected {expected_token}, found {self.current_token[0]}")

    def parse_column_list(self):
        columns = []
        const = ""
        const_type = 'pkey'
        pkey = "false"
        while self.current_token[0] != "SEMICOLON":
            print("parse_column_list:::>> current token", self.current_token[0])
            if self.current_token[0] == "RPAREN" :
                self.match('RPAREN')
                if self.current_token[0]== "SEMICOLON" :
                    print("parse_column_list 3::: current token", self.current_token)
                    break
            if columns:
                self.match('COMMA')
            column_name = self.current_token[1]
            if (self.current_token[0] == ('PRIMARY')):
                    column_name = self.current_token[0]
                    const = self.parse_constraint()
                    print("parse_column_list:s:s:s PRIMARY loop", const + " "+ column_name)
                    if self.current_token[0] == 'RPAREN' :
                        self.match('RPAREN')
                        print("parse_column_list::: PRIMARY loop", self.current_token)
                        if self.current_token[0]== "SEMICOLON" :
                            print("parse_column_list::: current token", self.current_token)
                       
            if self.current_token[0] == ('SEMICOLON') : 
                 print("parse_column_list::: current token2", self.current_token)
            elif self.current_token[0] != ('CONSTRAINT') and column_name !='PRIMARY': 
                 self.match('IDENTIFIER')
            
            if self.current_token[0] == ('CONSTRAINT'):
               key_id, const = self.parse_fkey_constraint()
               print('parse_column_list :<<:key_id:>>', key_id)
               if(key_id!= ""):
                    const_type='fkey'
                    column_name = "FOREIGN KEY"
               else:
                    column_name ='PRIMARY'

                
            print('parse_column_list :<<:const:>>', const)
            if self.current_token[0] != ('SEMICOLON') and column_name !='PRIMARY' and column_name != 'FOREIGN KEY' :      
                data_type, size = self.parse_data_type()
                nullable, default_value = self.parse_column_options()
                    
            print('parse_column_list', column_name, data_type, size, nullable, default_value,const)
          
            if column_name =='PRIMARY':
                columns.append((column_name,const_type, const))
                pkey = column_name
                print('parse_column_list :<<:PRIMARY:>>', const +" : "+ column_name)
            elif column_name != 'FOREIGN KEY' and column_name !='PRIMARY':
                columns.append((column_name, data_type.lower(), size, nullable, default_value,const))
            else:
                columns.append(("fkeys",key_id, const))

        
        return columns

    def parse_data_type(self):
        size = ""
        pkey = "false"
        data_type = self.current_token[1]
        print("parse_data_type", self.current_token[0], "data type", data_type)
        self.match(self.current_token[0])
        if self.current_token[0] == 'LPAREN':
            self.match('LPAREN')
            size = self.current_token[1]
            print("current tok 1", self.current_token[0], "data type", data_type, "size", size)
            self.advance()
        if data_type == 'NUMERIC':
            self.match('COMMA')
            size = size+ '.' +self.current_token[1]
            print("current tok 2", self.current_token[0], "data type", data_type, "size", size)
            self.advance()  
        if self.current_token[0] == "RPAREN":
            self.match('RPAREN')
        if self.current_token[0] == 'CONSTRAINT':
            data_type = self.parse_constraint()
           
        return data_type, size

    def parse_column_options(self):
        nullable = True
        default_value = None
        while self.current_token[0] in ['NOT', 'NULL', 'DEFAULT']:
            if self.current_token[0] == 'NOT':
                self.match('NOT')
                self.match('NULL')
                nullable = False
            elif self.current_token[0] == 'NULL':
                self.match('NULL')
                nullable = True
            elif self.current_token[0] == 'DEFAULT':
                self.match('DEFAULT')
                default_value = self.current_token[1]
                self.advance()
        return nullable, default_value

    def parse_constraint(self):
        constrain_str =""
        constraint = ""
        if self.current_token[0] == 'PRIMARY':
            constraint += ' ' + self.current_token[1]
            self.match('PRIMARY')
            constraint += ' ' + self.current_token[1]
            self.match('KEY')
            self.match('LPAREN')
            constrain_str = self.current_token[1]
            self.match('IDENTIFIER')
            self.match('RPAREN')
       
        return constrain_str

    def parse_prime_constraint(self):
        constrain_str =""
       # constraint = self.current_token[1]
       # self.match('CONSTRAINT')
        constraint =""
        #self.match('IDENTIFIER')
        if self.current_token[0] == 'PRIMARY':
            constraint += ' ' + self.current_token[1]
            self.match('PRIMARY')
            constraint += ' ' + self.current_token[1]
            self.match('KEY')
            self.match('LPAREN')
            constrain_str = self.current_token[1]
            self.match('IDENTIFIER')
            if(self.current_token[0] == 'COMMA'):
              self.match('COMMA')
              constrain_str+= ','+self.current_token[1]
            
            print("parse_constraint >>><<<<", constrain_str)
        return constrain_str


    def parse_fkey_constraint(self):
        key_id =""
        constrain_str =""
        constraint = self.current_token[1]
        self.match('CONSTRAINT')
        self.match('IDENTIFIER')
       
        if self.current_token[0] != 'PRIMARY':
            #self.match('IDENTIFIER')
            constraint = self.current_token[1]
            self.match('FOREIGN')
            self.match('KEY')
            self.match('LPAREN')
            key_id = ':'+ self.current_token[1]
            print("parse_fkey_constraint1 >>><<<<", self.current_token[1])
            self.match('IDENTIFIER')
            self.match('RPAREN')
            self.match('REFERENCES')
            constrain_str+= ':'+self.current_token[1]+ '.'
            self.match('IDENTIFIER')
            self.match('LPAREN')
            constrain_str+= self.current_token[1]
            self.match('IDENTIFIER')
            self.match('RPAREN')
            self.match('RPAREN')
        else:
            constraint = self.current_token[1]
            #self.match('CONSTRAINT')
            # constraint += ' ' + self.current_token[1]
            #self.match('IDENTIFIER')
            if self.current_token[0] == 'PRIMARY':
                constraint += ' ' + self.current_token[1]
                self.match('PRIMARY')
                constraint += ' ' + self.current_token[1]
                self.match('KEY')
                self.match('LPAREN')
                constrain_str = self.current_token[1]
                self.match('IDENTIFIER')
                while (self.current_token[0] == 'COMMA'):
                    self.match('COMMA')
                    constrain_str+= ','+self.current_token[1]
                    self.match('IDENTIFIER')
                    print("parse_fkey_constraint2 >>><<<<", constrain_str)
                self.match('RPAREN')    
             # const[0] = constrain_str
            
        return key_id,constrain_str
   
    def parse(self):
        print("cur token", self.current_token)

        self.match('CREATE')
        self.match('TABLE')
        table_name = self.current_token[1]
        self.match('IDENTIFIER')
        self.match('LPAREN')
        columns = self.parse_column_list()
        #self.match('RPAREN')
        self.match('SEMICOLON')
        return table_name, columns





