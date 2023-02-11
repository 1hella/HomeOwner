class House:
    def __init__(self):
        self.windows = 2
        self.door = "closed"
        self.heating = "off"
        self.temp = 20

    def open_door(self):
        self.door = "open"

    def close_door(self):
        self.door = "closed"

    def start_heating(self):
        self.heating = "on"

    def stop_heating(self):
        self.heating = "off"

    def process_moment(self):
        if self.heating == "on":
            self.temp += 1
        elif self.heating == "off":
            self.temp -= 1

    def is_door_closed(self):
        return self.door == "closed"

    def is_door_open(self):
        return self.door == "open"

    def is_heating_on(self):
        return self.heating == 'on'

    def is_heating_off(self):
        return self.heating == 'off'

    def print_stats(self):
        print(f"the door is {self.door}")
        print(f"the heating is {self.heating}")
        print(f"the temp is {self.temp}C")