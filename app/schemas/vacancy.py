from datetime import datetime
from pydantic import BaseModel, ConfigDict

class VacancyResponse(BaseModel):
    id: int 
    hh_vacancy_id: str
    title: str
    company_name: str
    url: str    
    description: str | None
    location: str | None
    salary_from: int | None
    salary_to: int | None
    published_at: datetime | None
    is_remote: bool
    is_active: bool
    direction_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)