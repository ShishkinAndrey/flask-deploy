from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import validates

from app import db


class SuperHeroes(db.Model):
    __tablename__ = "super_heroes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    power = Column(Integer)
    is_villain = Column(Boolean, nullable=False)
    deceased_date = Column(Date, nullable=True)

    @validates('power')
    def validate_power(self, key, power):
        if not 1 <= power <= 10:
            raise ValueError("Power should be greater than 1 and less then 10")
        return power

    def __repr__(self):
        return f"{self.name}"


class Chronicles(db.Model):
    __tablename__ = "chronicles"

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('super_heroes.id', ondelete="CASCADE"))
    year = Column(Integer)
    text = Column(String)

    @validates('year')
    def validate_year(self, key, year):
        if int(year) not in range(2000, 2101):
            raise ValueError("Year not in range (2000, 2100)")
        return year
