import uuid
import dataclasses
from dataclasses import dataclass, asdict
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional, List, Any

# entities.py
@dataclasses.dataclass
class Workday:
    date: str 

@dataclasses.dataclass
class Artist:
    id: uuid.UUID
    name: str
    daily_rate: float
    workdays: List[Workday]


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
    return basic_gross_pay

def gross_pay_use_case(repo: ArtistRepository, request: ArtistRequest) -> float:
    return basic_pay_use_case(repo, request)


# main.py
#from entities import Artist, Workday
#from use_cases import CalculateGrossPay
#from repositories import InMemoryArtistRepository


workdays: List[Workday] = [
    Workday("2023-03-11"),
    Workday("2023-03-12"),
    Workday("2023-03-13"),
]

artist: Artist = Artist(
    id=uuid.uuid4(),
    name="John Smith", 
    daily_rate=300,
    workdays=workdays
)

artists: List[Artist] = [artist]
artist_request: ArtistRequest = ArtistRequest(artist)
artist_repo: ArtistRepository = InMemoryArtistRepository(artists)
gross_pay_resp: float = gross_pay_use_case(artist_repo, artist_request)

if gross_pay_resp: 
    print(f"Gross pay for {artist.name}: {gross_pay_resp} GBP")

