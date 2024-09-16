

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_accountsInfoBase(BaseModel):

    
        
            
                office: Optional[str]
            
         
    
        
            
                account_no: Optional[str]
            
         
    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
            
                user_id: Optional[int]
            
        
    
        
            
                client_id: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
             
                acct_close_date : date
             
        
    
        
            
                is_external_acct: Optional[int]
            
        
    
        
            
                external_custodian_id : int
            
        
    
        
            
                account_type_classification: Optional[int]
            
        
    
        
    
        
    


class c_accountsInfoCreate(c_accountsInfoBase):
    pass

class c_accountsInfoUpdate(c_accountsInfoBase):
    pass

class c_accountsInfoInDBBase(c_accountsInfoBase):
    class Config:
        orm_mode = True

class c_accountsInfo(c_accountsInfoInDBBase):
    pass

