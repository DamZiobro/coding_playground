import math
import uuid
import dataclasses
from dataclasses import dataclass, asdict
from datetime import datetime, time, date
from abc import ABC, abstractmethod
from typing import Optional, List, Any

# entities.py
@dataclasses.dataclass
class Workday:
    date: str 
    start_work_time: datetime.time
    end_work_time: datetime.time

    def __post_init__(self):
        today = date.today();
        self.start_work_time = datetime.combine(today, self.start_work_time)
        self.end_work_time = datetime.combine(today, self.end_work_time)


@dataclasses.dataclass
class Artist:
    id: uuid.UUID
    name: str
    daily_rate: float
    overtime_rate: float
    overtime_unit_mins: int
    workdays: List[Workday]
    daily_agreed_mins: Optional[int] = 8


# repositories.py
class ArtistRepository(ABC):

    def __init__(self, artists: List[Artist] = None):
        if artists == None:
            self.artists = []
        self.artists: List[Artist] = artists

    @abstractmethod
    def get(self, name: str):
        pass


class InMemoryArtistRepository(ArtistRepository):

    def get(self, id):
        for artist in self.artists:
            if artist.id == id:
                return artist
        raise ValueError(f"No artist found with name {name}")

# requests.py
class ArtistRequest():
    def __init__(self, artist: Artist):
        self.artist = artist


# use_cases.py
def basic_pay_use_case(repo: ArtistRepository, request: ArtistRequest) -> float:

    SIGNIFICANT_DIGITS = 6
    artist = repo.get(request.artist.id)
    basic_gross_pay: float = 0 
    for workday in request.artist.workdays:
        basic_gross_pay += round(request.artist.daily_rate, SIGNIFICANT_DIGITS)
    print(f"basic_gross_pay: {basic_gross_pay}")
    return basic_gross_pay

def overtime_pay_use_case(repo: ArtistRepository, request: ArtistRequest) -> float:
    artist = repo.get(request.artist.id)
    overtime_gross_pay: float = 0 
    for workday in request.artist.workdays:
        overtime_minutes = int((workday.end_work_time - workday.start_work_time).seconds/60) - request.artist.daily_agreed_mins
        overtime_units = max(math.ceil(overtime_minutes / request.artist.overtime_unit_mins), 0)
        overtime_gross_pay += round(request.artist.overtime_rate * overtime_units)
    print(f"overtime_gross_pay: {overtime_gross_pay}")
    return overtime_gross_pay

def gross_pay_use_case(repo: ArtistRepository, request: ArtistRequest) -> float:
    gross_pay = basic_pay_use_case(repo, request)
    gross_pay += overtime_pay_use_case(repo, request)
    return gross_pay


# main.py
#from entities import Artist, Workday
#from use_cases import CalculateGrossPay
#from repositories import InMemoryArtistRepository


workdays: List[Workday] = [
    Workday("2023-03-11", time(10,00), time(18,00)),
    Workday("2023-03-12", time(10,00), time(19,00)),
    Workday("2023-03-13", time(10,00), time(20,00)),
]

artist: Artist = Artist(
    id=uuid.uuid4(),
    name="John Smith", 
    daily_rate=300,
    overtime_rate=10,
    overtime_unit_mins=15,
    daily_agreed_mins=8*60,
    workdays=workdays
)

artists: List[Artist] = [artist]
artist_request: ArtistRequest = ArtistRequest(artist)
artist_repo: ArtistRepository = InMemoryArtistRepository(artists)
gross_pay_resp: float = gross_pay_use_case(artist_repo, artist_request)

if gross_pay_resp: 
    print(f"Gross pay for {artist.name}: {gross_pay_resp} GBP")

