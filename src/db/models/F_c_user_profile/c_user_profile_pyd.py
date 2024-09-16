

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_user_profileInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                alternate_email : str
            
         
    
        
             
                anticipated_retirement_date : date
             
        
    
        
            
                birthplace : str
            
         
    
        
             
                birthdate : date
             
        
    
        
            
                country_of_cit : str
            
         
    
        
            
                country_of_origin : str
            
         
    
        
            
                country_of_residence : str
            
         
    
        
             
                date_of_death : date
             
        
    
        
             
                date_of_marriage : date
             
        
    
        
    
        
            
                drivers_license : str
            
         
    
        
            
                edu_level : str
            
         
    
        
            
                primary_email : str
            
         
    
        
            
                employer : str
            
         
    
        
            
                employer_address : str
            
         
    
        
            
                employment_status : str
            
         
    
        
            
                govt_id_doc : str
            
         
    
        
            
                state_of_residence : str
            
         
    
        
            
                govt_id_doc_num : str
            
         
    
        
            
                gender : str
            
         
    
        
            
                user_id: Optional[int]
            
        
    
        
    
        
    


class c_user_profileInfoCreate(c_user_profileInfoBase):
    pass

class c_user_profileInfoUpdate(c_user_profileInfoBase):
    pass

class c_user_profileInfoInDBBase(c_user_profileInfoBase):
    class Config:
        orm_mode = True

class c_user_profileInfo(c_user_profileInfoInDBBase):
    pass

