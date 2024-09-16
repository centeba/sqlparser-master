

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_programs_invInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                prog_code : str
            
         
    
        
            
                prog_name : str
            
         
    
        
            
                prog_desc : str
            
         
    
        
            
                prog_status : int
            
        
    
        
    


class p_i_programs_invInfoCreate(p_i_programs_invInfoBase):
    pass

class p_i_programs_invInfoUpdate(p_i_programs_invInfoBase):
    pass

class p_i_programs_invInfoInDBBase(p_i_programs_invInfoBase):
    class Config:
        orm_mode = True

class p_i_programs_invInfo(p_i_programs_invInfoInDBBase):
    pass

