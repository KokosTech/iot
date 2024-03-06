from db import DB
from delete import delete_content
from temperature_report import TemperatureReport
from thermometer import Thermometer

if __name__ == "__main__":
    # reset tables

    delete_content("thermometers")
    delete_content("temperature_reports")

    # create a few thermometers

    the1 = Thermometer(None, "Emerson", "Garage").create()
    the1_2 = Thermometer(None, "Emerson2", "Garage").create()
    
    the2 = Thermometer(None, "Spluss", "Bathroom").create()
    the2_2 = Thermometer(None, "Spluss2", "Bathroom").create()

    # create a few temperature reports

    rep1 = TemperatureReport(None, the1.id, None, 24).create()
    rep12 = TemperatureReport(None, the1.id, None, 15).create()
    
    rep1_2 = TemperatureReport(None, the1_2.id, None, 54).create()
    rep1_22 = TemperatureReport(None, the1_2.id, None, 45).create()
    
    rep2 = TemperatureReport(None, the2.id, None, 25).create()
    rep22 = TemperatureReport(None, the2.id, None, 35).create()
    
    rep2_2 = TemperatureReport(None, the2_2.id, None, 15).create()
    rep2_22 = TemperatureReport(None, the2_2.id, None, 25).create()

    # run select queries

    print("Average temperature in Garage:")
    print(Thermometer.avg_by_room("Garage"))
    print("================================")

    print(f"Minimum temperature repoted by thermometer {the1.id}:")
    print(the1.min_by_thermometer());
    print("================================")

    print("Thermometers made by Emerson:")
    print(Thermometer.find_by_manufacturer("Emerson"));
    print("================================")

    # update a thermometer
    
    the1.update("Emerson Updated", "Garage")
    print(f"Thermometer updated. {the1.manufacturer} @ {the1.room}")

    # delete all thermometers and reports
    
    the1.delete()
    the1_2.delete()
    
    the2.delete()
    the2_2.delete()