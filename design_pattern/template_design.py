from abc import ABC, abstractmethod

class DiningExperience(ABC):
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverages()
        print('Completed the four course meal')
    
    @abstractmethod
    def serve_appetizer(self) -> None:
        "Abstract method for defining the functionality for serving appetizer"
        pass

    @abstractmethod
    def serve_main_course(self) -> None:
        "Abstract method for defining the functionality for serving the main course"
        pass
    
    @abstractmethod
    def serve_dessert(self) -> None:
        "Abstract method for defining the functionality for serving the dessert"
        pass

    @abstractmethod
    def serve_beverages(self) -> None:
        "Abstract method for defining the functionality for serving the beverages"
        pass
    

class ItalianDinner(DiningExperience):

    def serve_appetizer(self) -> None:
        print('Serving bruschetta as appetizer...')

    def serve_main_course(self) -> None:
        print('Serving pasta as the main course')

    def serve_dessert(self) -> None:
        print('Serving the tiramisu as the dessert...')

    def serve_beverages(self) -> None:
        print('Serving wine as the beverage...')


class ChineseDinner(DiningExperience):

    def serve_appetizer(self) -> None:
        print('Serving spring rolls as appetizers')

    def serve_main_course(self) -> None:
        print('Serving stir-fried noddles as the main course')

    def serve_dessert(self) -> None:
        print('Serving fortune cookies as the dessert')

    def serve_beverages(self) -> None:
        print('Serving tea as a beverage')


if __name__ == '__main__':
    print("Welcome to XYZ restaurant")
    print('(1) Italian Dinner Experience')
    print('(2) Chinese Dinner Experience')
    print('(3) Leave')
    c = int(input('Choose Your Dining Experince: \n'))
    if c == 1:
        italian_dinner =ItalianDinner()
        italian_dinner.serve_dinner()
    elif c == 2:
        chinese_dinner = ChineseDinner()
        chinese_dinner.serve_dinner()
    else:
        print('BYE!')