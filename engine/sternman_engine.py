from abc import ABC
from car import Car

class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        """
        Initializes a SternmanEngine object.

        Args:
            last_service_date (date): The date of the last engine service.
            warning_light_is_on (bool): Whether the warning light is on.
        """
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        """
        Checks if the engine should be serviced based on the warning light.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.warning_light_is_on
