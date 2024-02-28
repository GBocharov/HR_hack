from typing import List, Optional
from pydantic import BaseModel, field_validator
import datetime

class Vacancy(BaseModel):
    uuid : str
    name : Optional[str] = None
    keywords : Optional[str] = None
    description : Optional[str] = None
    comment : Optional[str] = None

class ExperienceItem(BaseModel):
    starts: Optional[datetime.date] = None
    ends: Optional[datetime.date] = None
    employer: Optional[str] = None
    city: Optional[str] = None
    position: Optional[str] = None
    description : Optional[str] = None

class EducationItem(BaseModel):
    year : Optional[int] = None
    organization : Optional[str] = None
    faculty : Optional[str] = None
    specialty : Optional[str] = None
    result : Optional[str] = None
    education_type : Optional[str] = None
    education_level : Optional[str] = None

class Resume(BaseModel):
     uuid: str
     first_name: str
     last_name: str
     birth_date: Optional[datetime.date] = None
     country: Optional[str] = None
     city: Optional[str] = None
     about: Optional[str] = None
     key_skills: Optional[str] = None
     experienceItem :Optional[List[ExperienceItem]] = None
     educationItem : Optional[List[EducationItem]] = None
     languageItems : Optional[List[str]] = None

class DodikSet(BaseModel):
    vacancy : Vacancy
    failed_resumes : Optional[List[Resume]]
    confirmed_resumes : Optional[List[Resume]]

