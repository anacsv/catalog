from app.model.base_model import BaseModel

class ProductRating(BaseModel):

    def __init__(self, score: str = '', status: str = '', person_id: int = 0, product_id: int = 0, id: int = 0):
        self.__score = score
        self.__status = status
        self.__person_id = person_id
        self.__product_id = product_id
        super().__init__(id)

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
    
    @property
    def person_id(self) -> int:
        return self.__person_id

    @person_id.setter
    def person_id(self, person_id:int):
        self.__person_id = person_id
    
    @property
    def product_id(self) -> int:
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id:int):
        self.__product_id = product_id
    
    def __str__(self):
        return f'{self.id};{self.score};{self.status};{self.person_id};{self.product_id}'
    
    def __dict__(self):
        return {
                'id':self.id,
                'score':self.score,
                'status':self.status,
                'person_id':self.person_id,
                'product_id':self.product_id
        }
