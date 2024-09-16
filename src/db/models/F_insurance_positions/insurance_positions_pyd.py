

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class insurance_positionsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id : int
            
        
    
        
            
                carrier : str
            
         
    
        
            
                policy_num : str
            
         
    
        
            
                policy_type : str
            
         
    
        
    
        
    
        
    
        
    
        
            
                policy_status : int
            
        
    
        
            
                carrier_code : str
            
         
    
        
            
                policy_code : str
            
         
    
        
             
                issue_date : date
             
        
    
        
             
                renewal_date_fixed : date
             
        
    
        
    
        
    
        
    
        
            
                policy_role : int
            
        
    
        
    


class insurance_positionsInfoCreate(insurance_positionsInfoBase):
    pass

class insurance_positionsInfoUpdate(insurance_positionsInfoBase):
    pass

class insurance_positionsInfoInDBBase(insurance_positionsInfoBase):
    class Config:
        orm_mode = True

class insurance_positionsInfo(insurance_positionsInfoInDBBase):
    pass

