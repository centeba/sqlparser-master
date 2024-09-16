

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_tax_lotsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_no : str
            
         
    
        
             
                lot_date : date
             
        
    
        
    
        
            
                security_id: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                custodian_code : int
            
        
    
        
            
                security_id_external : str
            
         
    
        
    
        
            
                currency_local : str
            
         
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
             
                wash_purchase_date : date
             
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    


class f_tax_lotsInfoCreate(f_tax_lotsInfoBase):
    pass

class f_tax_lotsInfoUpdate(f_tax_lotsInfoBase):
    pass

class f_tax_lotsInfoInDBBase(f_tax_lotsInfoBase):
    class Config:
        orm_mode = True

class f_tax_lotsInfo(f_tax_lotsInfoInDBBase):
    pass

