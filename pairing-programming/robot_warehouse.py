import pytest
from unittest import mock
import uuid
from abc import ABC, abstractmethod
import dataclasses
from enum import Enum
from typing import List, Dict, Any

class RobotCommands(str, Enum):
    N = "N"
    E = "E"
    W = "W"
    S = "S"


@dataclasses.dataclass
class Warehouse:
    id: uuid.UUID = uuid.uuid4()
    width: int = 10
    height: int = 10

# entities
@dataclasses.dataclass
class Robot:
    id: uuid.UUID = uuid.uuid4()
    loc_x: int = 0
    loc_y: int = 0
    warehouse: Warehouse = None

    def move(self, command: RobotCommands):
        if not self.warehouse:
            raise ValueError("robot cannot move as it is not in the warehouse")

        if command == RobotCommands.N:
            if self.loc_y >= self.warehouse.height:
                raise ValueError("robot tried to move out of warehouse: N")
            self.loc_y += 1
        elif command == RobotCommands.E:
            if self.loc_x >= self.warehouse.width:
                raise ValueError("robot tried to move out of warehouse: E")
            self.loc_x += 1
        elif command == RobotCommands.S:
            if self.loc_y <= 0:
                raise ValueError("robot tried to move out of warehouse: S")
            self.loc_y -= 1
        elif command == RobotCommands.W:
            if self.loc_x <= 0:
                raise ValueError("robot tried to move out of warehouse: W")
            self.loc_x -= 1


# repositories
class WarehouseRepository:
    @abstractmethod
    def add(self, warehouse: Warehouse):
        pass

    @abstractmethod
    def get_by_id(self, warehouse_id) -> Warehouse:
        pass

class InMemoryWarehouseRepository:
    def __init__(self):
        self.warehouses = []

    def add(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def get_by_id(self, warehouse_id) -> Warehouse:
        for w in self.warehouses:
            if w.id == warehouse_id:
                return w
        raise ValueError(f"warehouse {warehouse_id} does not exists")


class RobotRepository:
    @abstractmethod
    def add(self, robot: Robot):
        pass

    @abstractmethod
    def get_by_id(self, robot_id) -> Robot:
        pass


class InMemoryRobotRepository:
    def __init__(self):
        self.robots = []

    def add(self, robot: Robot):
        for w in self.robots:
            if w.id == robot.id:
                raise ValueError(f"robot {w.id} already exists")
        self.robots.append(robot)

    def get_by_id(self, robot_id) -> Robot:
        for w in self.robots:
            if w.id == robot_id:
                return w
        raise ValueError(f"robot {robot_id} does not exists")


@dataclasses.dataclass
class CreateWarehouseRequest:
    warehouses: List[Dict[Any, Any]]


@dataclasses.dataclass
class CreateRobotRequest:
    robots: List[Dict[Any, Any]]

@dataclasses.dataclass
class ControlRobotCommandsRequest:
    robot_id: uuid.UUID
    commands: str

# use cases
def create_warehouse_use_case(repo: WarehouseRepository, request: CreateWarehouseRequest):
    for warehouse_dict in request.warehouses:
        warehouse = Warehouse(
            id = warehouse_dict["id"],
            loc_x=warehouse_dict["x"],
            loc_y=warehouse_dict["y"],
        )
        repo.add(warehouse)


def create_robot_use_case(
    repo: RobotRepository, request: CreateRobotRequest
):
    for robot_dict in request.robots:
        robot = Robot(
            id = robot_dict["id"],
            width=robot_dict["width"],
            height=robot_dict["height"],
            warehouse=robot_dict["warehouse"],
        )
        repo.add(robot)


def control_robot_use_case(repo: RobotRepository, request: ControlRobotCommandsRequest):

    robot: Robot = repo.get_by_id(request.robot_id)
    commands_list = request.commands.split(" ")
    for command in commands_list:
        robot.move(command)


# tests


def test_robot_creation_with_defaults():
    robot = Robot()
    assert robot.loc_y == 0
    assert robot.loc_y == 0


def test_warehouse_creation_with_defaults():
    w = Warehouse()
    assert w.width == 10
    assert w.height == 10


def test_robot_create_with_warehouse():
    w = Warehouse()
    robot = Robot(warehouse=w)
    assert robot.warehouse.width == 10
    assert robot.warehouse.height == 10
    assert robot.loc_y == 0
    assert robot.loc_x == 0


def test_inmemorywarehouse_repository_initialized_empty():
    repo = InMemoryWarehouseRepository()
    assert repo.warehouses == []

def test_inmemorywarehouse_adds_new_warehouse_to_list():
    repo = InMemoryWarehouseRepository()
    w = Warehouse()
    repo.add(w)
    assert w in repo.warehouses


def test_inmemoryrobot_raises_exception_if_robot_already_exists():
    repo = InMemoryRobotRepository()
    robot = Robot()
    repo.add(robot)
    with pytest.raises(ValueError) as exc:
        repo.add(robot)
    assert "already exists" in str(exc.value)


def test_inmemorywarehouse_returns_warehouse_if_exists():
    repo = InMemoryWarehouseRepository()
    w = Warehouse()
    repo.warehouses = [w]
    ret_warehouse = repo.get_by_id(w.id)
    assert w.id == ret_warehouse.id


def test_inmemorywarehouse_raises_exception_if_warehouse_does_not_exist():
    repo = InMemoryWarehouseRepository()
    w = Warehouse()
    with pytest.raises(ValueError) as exc:
        _ = repo.get_by_id(w.id)
    assert "does not exists" in str(exc.value)

def test_robot_reacts_on_control_commands_properly():
    repo = mock.Mock()
    robot = Robot(
        id = uuid.uuid4(),
        loc_x = 0,
        loc_y = 0,
        warehouse = Warehouse(id=uuid.uuid4(), width= 10, height= 10),
    )
    repo.get_by_id.return_value = robot
    request = ControlRobotCommandsRequest(
        robot_id=robot.id,
        commands="N E N E N E N E",
    )

    control_robot_use_case(repo, request)

    assert robot.loc_x == 4
    assert robot.loc_y == 4

def test_robot_reacts_on_control_commands_properly():
    repo = mock.Mock()
    robot = Robot(
        id = uuid.uuid4(),
        loc_x = 0,
        loc_y = 0,
        warehouse = Warehouse(id=uuid.uuid4(), width= 5, height= 5),
    )
    repo.get_by_id.return_value = robot
    request = ControlRobotCommandsRequest(
        robot_id=robot.id,
        commands="N N N N N N N",
    )

    with pytest.raises(ValueError) as exc:
        control_robot_use_case(repo, request)

    assert "robot tried to move out of warehouse" in str(exc.value)

def test_robot_move_raise_error():
    robot = Robot()

    with pytest.raises(ValueError) as exc:
        robot.move("N")

    assert "robot cannot move" in str(exc.value)

