import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
#print(parse_json)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in Amethi:", active_case)