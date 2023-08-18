from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        """
        Initializes a Car object.

        Args:
            last_service_date (date): The date of the last service for the car.
        """
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        """
        Abstract method to check if the car needs servicing.

        Subclasses must implement this method.

        Returns:
            bool: True if the car needs servicing, False otherwise.
        """
        pass
