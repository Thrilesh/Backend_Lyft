from abc import ABC
from car import Car

class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        """
        Initializes a WilloughbyEngine object.

        Args:
            last_service_date (date): The date of the last engine service.
            current_mileage (int): The current mileage of the engine.
            last_service_mileage (int): The mileage at the last engine service.
        """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        """
        Checks if the engine should be serviced based on mileage.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 60000
