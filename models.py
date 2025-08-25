from typing import List, Optional

from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    full_name: Optional[str] = Field(None, description="Full name of the candidate")
    email: Optional[str] = Field(None, description="Professional email address")
    location: Optional[str] = Field(None, description="Current location (city, state/country)")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")


class Experience(BaseModel):
    job_title: Optional[str] = Field(None, description="Job title or role name")
    company_or_product: Optional[str] = Field(None, description="Company name or product worked on")
    start_date: Optional[str] = Field(None, description="Start date (MM/YYYY format)")
    end_date: Optional[str] = Field(None, description="End date (MM/YYYY format)")
    is_current: bool = Field(False, description="Whether this is the current position")
    bullets: List[str] = Field(default_factory=list, description="Achievement bullets and responsibilities")


class Education(BaseModel):
    degree: Optional[str] = Field(None, description="Degree type and field of study")
    institution: Optional[str] = Field(None, description="University or educational institution name")
    graduation_date: Optional[str] = Field(None, description="Graduation date (MM/YYYY format)")


class ProfessionalProfile(BaseModel):
    contact_info: ContactInfo = Field(default_factory=ContactInfo, description="Personal contact information")
    professional_summary: Optional[str] = Field(None, description="Brief professional overview and value proposition")
    experience: List[Experience] = Field(default_factory=list, description="Work experience history")
    education: List[Education] = Field(default_factory=list, description="Educational background")
    technical_skills: List[str] = Field(default_factory=list, description="Technical skills and technologies")
    certifications: List[str] = Field(default_factory=list, description="Professional certifications and licenses")
    languages: List[str] = Field(default_factory=list, description="Spoken languages and proficiency levels")
