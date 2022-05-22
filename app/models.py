"""All models for Flaskmin project"""

from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from werkzeug.security import (generate_password_hash,
    check_password_hash
    )

from db.engine import Base


class Admin(Base):
    __tablename__ = 'admins'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(100))
    
    def __init__(self, firstname, lastname, username, email) -> None:
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.email = email

    def __str__(self) -> str:
        return self.username


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow())

    def __str__(self) -> str:
        return self.first_name