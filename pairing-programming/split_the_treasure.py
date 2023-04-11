import uuid
import pytest
import dataclasses
from abc import abstractmethod, ABC
from typing import List, Dict, Any, Any

# entities.py

@dataclasses.dataclass
class Treasure:
    id: uuid.UUID
    gems: List[int]

    def split_treasure(self, num_seekers):
        # check if total gems
        total_value = sum(self.gems)
        if total_value % num_seekers != 0:
            return False

        equal_split = total_value // num_seekers
        self.gems.sort(reverse=True)
        counts = [0] * num_seekers

        for gem in self.gems:
            for i in range(num_seekers):
                if counts[i] + gem <= equal_split:
                    counts[i] += gem
                    break
            else:
                return False

        return counts


class TreasureRepository(ABC):

    @abstractmethod
    def add(self, treasure: Treasure):
        pass

    @abstractmethod
    def get_by_id(self, treasure_id: uuid.UUID) -> Treasure:
        pass

class InMemoryTreasureRepository(TreasureRepository):

    def __init__(self):
        self.treasures = []

    def add(self, treasure: Treasure):
        self.treasures.append(treasure)

    def get_by_id(self, treasure_id: uuid.UUID) -> Treasure:
        for t in self.treasures:
            if t.id == treasure_id:
                return t
        raise ValueError("treasure {treasure_id} does not exist")

# requests.py
@dataclasses.dataclass
class CreateTreasureRequest:
    treasures: List[Dict[str, List[int]]]

@dataclasses.dataclass
class CheckSplitableRequest:
    treasure_id: uuid.UUID

# responses.py
@dataclasses.dataclass
class CheckSplitableResponse:
    treasure_id: uuid.UUID
    is_splitable: bool
    crew_size: int


# use cases
def create_treasure_use_case(repo: TreasureRepository, request: CreateTreasureRequest):
    for treasure_dict in request.treasures:
        treasure = Treasure(id=treasure_dict["id"], gems=treasure_dict["gems"])
        repo.add(treasure)

def check_treasure_splitable_use_case(repo: TreasureRepository, request: CheckSplitableRequest):
    treasure: Treasure = repo.get_by_id(request.treasure_id)
    resp = CheckSplitableResponse(treasure_id=request.treasure_id, is_splitable=False, crew_size=0)

    for crew_size in range(2, len(treasure.gems)+1):
        ret = treasure.split_treasure(crew_size)
        if ret:
            resp.crew_size = crew_size
            resp.is_splitable = True

    return resp

@pytest.fixture
def treasure_data():
    return [
        { "id": uuid.uuid4(), "gems": [4, 4, 4] },
        { "id": uuid.uuid4(), "gems": [27, 7, 20] },
        { "id": uuid.uuid4(), "gems": [6, 3, 2, 4, 1] },
        { "id": uuid.uuid4(), "gems": [3,3,3,3,2,2,2,2,2,2,2,2]},
        { "id": uuid.uuid4(), "gems": [27, 7, 21] },
    ]

# tests
def test_create_treasure_use_case(treasure_data):

    request = CreateTreasureRequest(treasure_data)
    repo = InMemoryTreasureRepository()

    create_treasure_use_case(repo, request)

    assert len(repo.treasures) == 5
    assert repo.treasures[0].gems == treasure_data[0]["gems"]
    assert repo.treasures[0].id == treasure_data[0]["id"]

@pytest.mark.parametrize(
    "index,expected_is_splittable,expected_crew_size",
    [
        (0, True, 3),
        (1, True, 2),
        (2, True, 2),
        (3, True, 2),
        (4, False, 0),
    ]
)
def test_split_the_treasure_use_case(treasure_data, index, expected_is_splittable, expected_crew_size):

    request = CreateTreasureRequest(treasure_data)
    repo = InMemoryTreasureRepository()

    create_treasure_use_case(repo, request)
    check_split_resp: CheckSplitableResponse = check_treasure_splitable_use_case(repo, CheckSplitableRequest(treasure_id=treasure_data[index]["id"]))

    assert check_split_resp.treasure_id == treasure_data[index]["id"]
    assert check_split_resp.is_splitable == expected_is_splittable
    assert check_split_resp.crew_size == expected_crew_size
