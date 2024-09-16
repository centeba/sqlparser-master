from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        if(cls.__name__.lower()=="client"):
          return "c_client_info"
        elif(cls.__name__.lower()=="c_user_info"):
          return "c_user_info"
        elif(cls.__name__.lower()=="account"):
          return "c_accounts"
        elif(cls.__name__.lower()=="securitymaster"):
          return "f_security_master"
        elif(cls.__name__.lower()=="transaction"):
          return "f_transaction_info"
        else:
          return str
        