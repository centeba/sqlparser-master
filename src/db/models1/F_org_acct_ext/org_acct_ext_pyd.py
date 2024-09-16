

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class org_acct_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_acct : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_types : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class org_acct_extInfoCreate(org_acct_extInfoBase):
    pass

class org_acct_extInfoUpdate(org_acct_extInfoBase):
    pass

class org_acct_extInfoInDBBase(org_acct_extInfoBase):
    class Config:
        orm_mode = True

class org_acct_extInfo(org_acct_extInfoInDBBase):
    pass

