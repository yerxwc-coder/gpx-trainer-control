import gpxpy
import gpxpy.geo

class GPXRoute:

    def __init__(self, file):
        self.file = file
        self.points = []

    def load(self):

        with open(self.file) as f:
            gpx = gpxpy.parse(f)

        for track in gpx.tracks:
            for seg in track.segments:
                for p in seg.points:
                    self.points.append(
                        (p.latitude, p.longitude, p.elevation)
                    )

        return self.points

    def calculate_slopes(self):

        slopes = []

        for i in range(1, len(self.points)):

            p1 = self.points[i-1]
            p2 = self.points[i]

            dist = gpxpy.geo.haversine_distance(
                p1[0], p1[1], p2[0], p2[1]
            )

            elev = p2[2] - p1[2]

            slope = elev/dist if dist > 0 else 0

            slopes.append(slope)

        return slopes
