import asyncio

from gpx_parser import GPXRoute
from trainer_control import Trainer
from activity_recorder import Recorder
from fit_exporter import FitExporter

async def main():

    route = GPXRoute("gpx/ruta.gpx")

    route.load()

    slopes = route.calculate_slopes()

    trainer = Trainer("YOUR_TRAINER_MAC")

    await trainer.connect()

    recorder = Recorder()

    for slope in slopes:

        await trainer.set_grade(slope)

        print("Slope:", slope)

        await asyncio.sleep(3)

    exporter = FitExporter("activity.fit")

    exporter.export(recorder.get())

asyncio.run(main())
