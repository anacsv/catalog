#id, score, status, person_id, product_id
from app.model.base_model import BaseModel

class ProductRating(BaseModel):

    def __init__(self, score: str, status: str, id: int = 0):
        self.__score = score
        self.__status = status
        super().__init__(id = id)

    @property
    def score(self) -> str:
        return self.__score

    @score.setter
    def score(self, score:str):
        self.__score = score

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status:str):
        self.__status = status