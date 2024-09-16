

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_retirement_rmd_infoInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
    
        
             
                rmd_dist_date : date
             
        
    
        
             
                rmd_distr_begin_date : date
             
        
    
        
             
                rmd_distr_end_date : date
             
        
    
        
             
                rmd_distr_end_prioryr_date : date
             
        
    
        
    
        
    
        
    
        
    


class f_retirement_rmd_infoInfoCreate(f_retirement_rmd_infoInfoBase):
    pass

class f_retirement_rmd_infoInfoUpdate(f_retirement_rmd_infoInfoBase):
    pass

class f_retirement_rmd_infoInfoInDBBase(f_retirement_rmd_infoInfoBase):
    class Config:
        orm_mode = True

class f_retirement_rmd_infoInfo(f_retirement_rmd_infoInfoInDBBase):
    pass

