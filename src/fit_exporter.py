from fitencode import FitEncoder

class FitExporter:

    def __init__(self, filename):

        self.filename = filename

    def export(self, records):

        encoder = FitEncoder(self.filename)

        for r in records:

            encoder.write_message(

                "record",

                power=r["power"],
                cadence=r["cadence"],
                speed=r["speed"]

            )

        encoder.close()
