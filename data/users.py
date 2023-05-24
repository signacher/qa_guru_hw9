import dataclasses
from enum import Enum
from typing import List

class Gender(Enum):
    Female = 'Female'
    Male = 'Male'
    Other = 'Other'

class Month(Enum):
    January = 'January'
    February = 'February'
    March = 'March'
    April = 'April'
    May = 'May'
    June = 'June'
    July = 'July'
    August = 'August'
    September = 'September'
    October  = 'October'
    November = 'November'
    December = 'December'

class Subject(Enum):
    english = 'English'
    maths = 'Maths'
    physics = 'Physics'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    economics = 'Economics'
    arts = 'Arts'
    biology = 'Biology'

class Hobbie(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: List[Gender]
    phone_number: str
    birth_year: str
    birth_month: List[Month]
    birth_day: str
    subject: List[Subject]
    hobbie: List[Hobbie]
    current_address: str
    upload_filename: str
    state: str
    city: str

