

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class custodian_sc_accounts_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_acct : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_types : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class custodian_sc_accounts_extInfoCreate(custodian_sc_accounts_extInfoBase):
    pass

class custodian_sc_accounts_extInfoUpdate(custodian_sc_accounts_extInfoBase):
    pass

class custodian_sc_accounts_extInfoInDBBase(custodian_sc_accounts_extInfoBase):
    class Config:
        orm_mode = True

class custodian_sc_accounts_extInfo(custodian_sc_accounts_extInfoInDBBase):
    pass

