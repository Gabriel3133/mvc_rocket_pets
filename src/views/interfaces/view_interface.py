from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):

    @abstractmethod
    def handel(self,http_request: HttpResquest) -> HttpResponse:
        pass
