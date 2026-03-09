import asyncio
from bleak import BleakClient
from pycycling.ftms import FitnessMachineService

class Trainer:

    def __init__(self, address):

        self.address = address
        self.client = None
        self.ftms = None

    async def connect(self):

        self.client = BleakClient(self.address)

        await self.client.connect()

        self.ftms = FitnessMachineService(self.client)

        await self.ftms.request_control()

    async def set_grade(self, grade):

        await self.ftms.set_simulation_parameters(
            grade=grade,
            wind_speed=0,
            rolling_resistance=0.004,
            wind_resistance=0.5
        )
