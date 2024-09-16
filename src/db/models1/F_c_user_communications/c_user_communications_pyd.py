

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_user_communicationsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                user_id: Optional[int]
            
        
    
        
            
                allow_bulk_emails : int
            
        
    
        
            
                allow_mail : int
            
        
    
        
            
                allow_email: Optional[int]
            
        
    
        
            
                do_not_call : int
            
        
    
        
            
                fax_opt_out : int
            
        
    
        
            
                allow_marketing_materials : int
            
        
    
        
             
                best_call_time_start : date
             
        
    
        
             
                best_call_time_end : date
             
        
    
        
            
                do_not_track : int
            
        
    
        
            
                dont_solicit : int
            
        
    
        
            
                dont_geo_track : int
            
        
    
        
    
        
    


class c_user_communicationsInfoCreate(c_user_communicationsInfoBase):
    pass

class c_user_communicationsInfoUpdate(c_user_communicationsInfoBase):
    pass

class c_user_communicationsInfoInDBBase(c_user_communicationsInfoBase):
    class Config:
        orm_mode = True

class c_user_communicationsInfo(c_user_communicationsInfoInDBBase):
    pass

