import requests
import json

url = "https://adb-2984943014560952.12.azuredatabricks.net/api/2.0/sql/statements/"

payload = json.dumps({
  "warehouse_id": "ef612f64d5f4c0fc",
  "statement": "SELECT * FROM samples.nyctaxi.trips limit 100",
  "wait_timeout": "30s",
  "on_wait_timeout": "CANCEL"
})
headers = {
  'Authorization': 'Bearer dapi446ae43df502c7bd00269084ae83df75',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
