import time

class Recorder:

    def __init__(self):

        self.records = []

    def record(self, power, cadence, speed):

        self.records.append({

            "time": time.time(),
            "power": power,
            "cadence": cadence,
            "speed": speed

        })

    def get(self):

        return self.records
