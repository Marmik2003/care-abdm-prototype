import requests
import json
from pydantic import HttpUrl, Json


class HIPIntegration:

    def __init__(self, client_id, client_secret):
        self.base_url = "https://dev.ndhm.gov.in/devservice/v1"

        # Get Auth Token
        request_url = "https://dev.abdm.gov.in/gateway/v0.5/sessions"
        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "clientId": client_id,
            "clientSecret": client_secret
        }

        resp = requests.post(request_url, data=json.dumps(payload), headers=headers)
        resp_json = resp.json()
        print(resp_json)
        access_token = resp_json["accessToken"]
        headers["Accept"] = "application/json"
        headers["Authorization"] = f"Bearer {access_token}"
        self.headers = headers

    def set_hip_url(self, url: HttpUrl):
        request_url = self.base_url + '/bridges'
        payload = {"url": url}
        response = requests.patch(request_url, data=json.dumps(payload), headers=self.headers)
        return response
    
    def register_facility(self, facility_json: Json):
        request_url = self.base_url + '/bridges/services'
        return requests.put(request_url, data=json.dumps(facility_json), headers=self.headers)

