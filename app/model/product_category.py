from app.model.base_model import BaseModel

class ProductCategory(BaseModel):

    def __init__(self, name: str, description: str, id: int = 0):
        self.__name = name
        self.__description = description
        super().__init__(id = id)

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, description:str):
        self.__description = description
