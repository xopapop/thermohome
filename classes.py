from datetime import datetime
class weather():
    def __init__(self, weather_dict):
        self.dt = ''
        self.temp_k = float()
        self.rh = int()
        self.description = ''
        self.wind_speed = float()
        self.wind_angle = float()

        # save everything in the weather dict as an attribute
        # remove this once this data structures is nailed down
        for attr_name in weather_dict:
            setattr(self, attr_name, weather_dict[attr_name])

        # calculated attributes
        self.temp_c = float()  # convert from farenheit
        self.temp_f = float()  # convert from celsius
        self.wind_angle_compass = ''  # convert wind angle in degrees to the closest 8-point compass direction
