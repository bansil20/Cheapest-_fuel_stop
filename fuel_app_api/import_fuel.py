import pandas as pd
from fuel_app_api.models import FuelStation

def run():
    df = pd.read_csv("fuel-prices-ass.csv")

    for _, row in df.iterrows():
        FuelStation.objects.create(
            opis_id=row["OPIS Truckstop ID"],
            name=row["Truckstop Name"],
            address=row["Address"],
            city=row["City"],
            state=row["State"],
            rack_id=row["Rack ID"],
            price=row["Retail Price"]
        )

    print("Fuel stations imported successfully!")

