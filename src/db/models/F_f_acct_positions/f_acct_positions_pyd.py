

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_acct_positionsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                security_id : str
            
         
    
        
    
        
             
                maturity_date : date
             
        
    
        
    
        
    
        
            
                custodian : int
            
        
    
        
    
        
             
                date_acquired : date
             
        
    
        
            
                is_annuity : int
            
        
    
        
    
        
    
        
    
        
    
        
    


class f_acct_positionsInfoCreate(f_acct_positionsInfoBase):
    pass

class f_acct_positionsInfoUpdate(f_acct_positionsInfoBase):
    pass

class f_acct_positionsInfoInDBBase(f_acct_positionsInfoBase):
    class Config:
        orm_mode = True

class f_acct_positionsInfo(f_acct_positionsInfoInDBBase):
    pass

