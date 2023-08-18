from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        """
        Checks if the Rorschach engine needs servicing.

        Returns:
            bool: True if the engine needs servicing, False otherwise.
        """

        # Calculate the service threshold date by adding 4 years to the last service date
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)

        # Check if the calculated threshold date is in the past or if the engine should be serviced
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
