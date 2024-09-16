

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_security_masterInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                ticker_symbol: Optional[str]
            
         
    
        
            
                cash_equiv: Optional[int]
            
        
    
        
    
        
             
                close_price_as_of_date: Optional[date]
            
        
    
        
    
        
            
                isin: Optional[str]
            
         
    
        
            
                cusip: Optional[str]
            
         
    
        
            
                ticker: Optional[str]
            
         
    
        
            
                sedol: Optional[str]
            
         
    
        
            
                institution_id: Optional[str]
            
         
    
        
            
                institution_sec_id: Optional[str]
            
         
    
        
            
                proxy_security_id: Optional[str]
            
         
    
        
    


class f_security_masterInfoCreate(f_security_masterInfoBase):
    pass

class f_security_masterInfoUpdate(f_security_masterInfoBase):
    pass

class f_security_masterInfoInDBBase(f_security_masterInfoBase):
    class Config:
        orm_mode = True

class f_security_masterInfo(f_security_masterInfoInDBBase):
    pass

