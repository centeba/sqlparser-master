

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_currency_codes_iso4217InfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                entity : str
            
         
    
        
            
                currency_name : str
            
         
    
        
            
                currency_code : str
            
         
    
        
            
                NUMERIC_code : int
            
        
    
        
    


class m_currency_codes_iso4217InfoCreate(m_currency_codes_iso4217InfoBase):
    pass

class m_currency_codes_iso4217InfoUpdate(m_currency_codes_iso4217InfoBase):
    pass

class m_currency_codes_iso4217InfoInDBBase(m_currency_codes_iso4217InfoBase):
    class Config:
        orm_mode = True

class m_currency_codes_iso4217Info(m_currency_codes_iso4217InfoInDBBase):
    pass

