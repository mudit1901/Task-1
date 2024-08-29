from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class name_location(Base):
    __tablename__ = "uri"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    location = Column(String)
