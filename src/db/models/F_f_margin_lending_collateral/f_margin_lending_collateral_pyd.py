

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_margin_lending_collateralInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
            
                mkt_val_security_id: Optional[int]
            
        
    
        
            
                acct_type : int
            
        
    
        
            
                security_type : int
            
        
    
        
            
                option_sym_code : str
            
         
    
        
             
                option_exp_date : date
             
        
    
        
            
                is_principal_protected : int
            
        
    
        
            
                structured_product : int
            
        
    
        
    
        
    
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class f_margin_lending_collateralInfoCreate(f_margin_lending_collateralInfoBase):
    pass

class f_margin_lending_collateralInfoUpdate(f_margin_lending_collateralInfoBase):
    pass

class f_margin_lending_collateralInfoInDBBase(f_margin_lending_collateralInfoBase):
    class Config:
        orm_mode = True

class f_margin_lending_collateralInfo(f_margin_lending_collateralInfoInDBBase):
    pass

