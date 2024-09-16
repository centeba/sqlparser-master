

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_propertyInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
    
        
    
        
            
                property_use : int
            
        
    
        
             
                purchase_date : date
             
        
    
        
             
                sale_date : date
             
        
    
        
            
                address : str
            
         
    
        
    
        
    
        
    
        
    
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class l_propertyInfoCreate(l_propertyInfoBase):
    pass

class l_propertyInfoUpdate(l_propertyInfoBase):
    pass

class l_propertyInfoInDBBase(l_propertyInfoBase):
    class Config:
        orm_mode = True

class l_propertyInfo(l_propertyInfoInDBBase):
    pass

