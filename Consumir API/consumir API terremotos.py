import requests
class USGSEarthquakeClient:
    def __init__(self):
        self.base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    
    def get_earthquakes(self, starttime, endtime, min_magnitude=1.0, max_magnitude=None, format_type="geojson"):
        params = {
            "format": format_type,
            "starttime": starttime,
            "endtime": endtime,
            "minmagnitude": min_magnitude
        }
        
        if max_magnitude:
            params["maxmagnitude"] = max_magnitude
        response = requests.get(self.base_url, params=params)
        
        # Verifica
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

if __name__ == "__main__":
    client = USGSEarthquakeClient()
    starttime = "2024-01-01"
    endtime = "2024-10-01"
    min_magnitude = 5.0
    try:
        data = client.get_earthquakes(starttime=starttime, endtime=endtime, min_magnitude=min_magnitude)
        for event in data["features"]:
            properties = event["properties"]
            print(f"Lugar: {properties['place']}, Magnitud: {properties['mag']}, Tiempo: {properties['time']}")
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
