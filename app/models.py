"""All models for Flaskmin project"""
from sqlalchemy import Column, String, Integer

from werkzeug.security import generate_password_hash, check_password_hash


class Admin():
    __tablename__ = 'admin'
    
    id = Column(Integer(10), primary_key=True)
    first_name = Column(String(100), nullable=False, blank=False)
    last_name = Column(String(120), nullable=False, blank=False)
    username = Column(String(20), nullable=False, blank=False, unique=True)
    email = Column(String(100), nullable=False, blank=False, unique=True)