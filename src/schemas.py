from pydantic import BaseModel
from datetime import datetime
import schemas


# User Schemas
class UserBase(BaseModel):
    email: str
    