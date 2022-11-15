from fastapi import APIRouter
from ..data.connection import confirmed_global
# from data.connection import deaths_global
# from data.connection import recovered_global
from bson import json_util
from json import loads

router = APIRouter()

# endpoints
@router.get("/confirmed/{country}")
def get_confirmed_by_country(country:str):
    filt = {"Country/Region":country}
    project = {"Country/Region":0, "Province/State":0, "Lat":0, "Long":0, "_id":0}
    dates = confirmed_global.find(filt, project)
    dates = list(dates)[0]
    if len(dates) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(dates))


@router.get("/deaths/{country}")
def get_deaths_by_country(country:str):
    filt = {"Country/Region":country}
    project = {"Country/Region":0, "Province/State":0,  "Lat":0, "Long":0, "_id":0}
    dates = deaths_global.find(filt, project)
    dates = list(dates)[0]
    if len(dates) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(dates))


@router.get("/recovered/{country}")
def get_recovered_by_country(country:str):
    filt = {"Country/Region":country}
    project = {"Country/Region":0, "Province/State":0, "Lat":0, "Long":0, "_id":0}
    dates = recovered_global.find(filt, project)
    dates = list(dates)[0]
    if len(dates) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(dates))


@router.get("/coordinates/{country}")
def get_coordinates(country:str):
    filt = {"Country/Region":country}
    project = {"Lat":1, "Long":1, "_id":0}
    coords = confirmed_global.find(filt, project)
    coords = list(coords)[0]
    if len(coords) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(coords))