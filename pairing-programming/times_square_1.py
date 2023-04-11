import uuid
import dataclasses
from abc import ABC, abstractmethod
from typing import Optional, List, Any, Dict

# entities.py

@dataclasses.dataclass
class Display(ABC):
    id: uuid.UUID
    message: str
    width: int

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass

class ScrollableDisplay(Display):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_index = 0
        self.end_index = self.width
        self.orig_message = self.message
        self.full_str = " " * (self.width - 1) + self.orig_message + " " * (self.width - 1)

    def _scroll(self):
        if len(self.orig_message) <= self.width:
            self.end_index = len(self.full_str) + 1
            return self.message

        self.message = self.full_str[self.start_index:self.end_index] 
        self.start_index += 1
        self.end_index += 1

    def __next__(self):
        if self.end_index > len(self.full_str):
            raise StopIteration
        self._scroll()
        return self.message

class InfiniteScrollableDisplay(ScrollableDisplay):

    def __next__(self):
        if self.end_index > len(self.full_str):
            self.start_index = 0
            self.end_index = self.width

        self._scroll()
        return self.message
       

#class Display:

    #def __init__(self, message: str, width: int = 10):
        #self.width = width
        #self.message = message

    #def scroll_and_display(self):
        #if len(self.message) <= self.width:
            #print(self.message)

        #full_message = " " * (self.width -1) + self.message + " " * (self.width - 1)
        #start_index = 0
        #end_index = self.width
        #while end_index <= len(full_message):
            #visible_message = full_message[start_index:end_index] 
            #print(visible_message)
            #start_index += 1
            #end_index += 1

# repositories.py
class DisplayRepository(ABC):

    @abstractmethod
    def add(self, display: Display):
        pass

    @abstractmethod
    def get_by_id(self, id: uuid.UUID) -> Display:
        pass

class InMemoryDisplayRepository(DisplayRepository):

    def __init__(self):
        self.displays = []

    def add(self, display: Display):
        self.displays.append(display)

    def get_by_id(self, id: uuid.UUID) -> Display:
        for display in self.displays:
            if display.id == id:
                return display
        raise ValueError(f"display with id {id} not found")

## requests.py
@dataclasses.dataclass
class GetDisplayRequest:
    id: uuid.UUID

@dataclasses.dataclass
class CreateDisplayRequest:
    displays: List[Dict[Any, Any]]

## use cases

def create_displays_use_case(repo: DisplayRepository, request: CreateDisplayRequest):
    for display_dict in request.displays:
        display = display_dict["type"](
            id=display_dict["id"],
            message=display_dict["message"],
            width=display_dict["width"],
        )
        repo.add(display)

def run_display_scrolling_use_case(repo: DisplayRepository, request: GetDisplayRequest):
    display: Display = repo.get_by_id(request.id)
    for message in display:
        print(message)


if __name__ == "__main__":    

    message: str = "Hello world!"
    display_width = 10

    infinite_display = {
        "id": uuid.uuid4(),
        "message": message,
        "width": display_width,
        "type": InfiniteScrollableDisplay,
    }

    scrollable_display = {
        "id": uuid.uuid4(),
        "message": message,
        "width": display_width,
        "type": ScrollableDisplay,
    }

    scrollable_const_display = {
        "id": uuid.uuid4(),
        "message": "Hello",
        "width": display_width,
        "type": ScrollableDisplay,
    }

    displays = [
        scrollable_const_display,
        scrollable_display,
        infinite_display
    ]

    display_repo: DisplayRepository = InMemoryDisplayRepository()

    create_req = CreateDisplayRequest(displays)
    create_displays_use_case(display_repo, create_req)

    scroll_req = GetDisplayRequest(scrollable_display["id"])
    run_display_scrolling_use_case(display_repo, scroll_req)
