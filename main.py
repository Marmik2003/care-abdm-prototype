import os
from dotenv import load_dotenv
from fastapi import FastAPI
from response_types import FacilityURL, FacilityData
from core import HIPIntegration

load_dotenv()

app = FastAPI()

CLIENT_ID = os.environ('CLIENT_ID')
CLIENT_SECRET = os.environ('CLIENT_SECRET')

messenger = HIPIntegration(CLIENT_ID, CLIENT_SECRET)


@app.post('/add-hip-url/')
def add_hip_url(data: FacilityURL):
    url = data.url
    return messenger.set_hip_url(url)


@app.post('/add-facility')
def add_facility(data: FacilityData):
    data_json = {
        "id": data.facility_id,
        "name": data.name,
        "type": data.facility_type,
        "active": data.active,
        "alias": data.alias
    }
    return messenger.register_facility(data_json)
