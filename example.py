from env import ENDPOINT, ACCESS_ID, USERNAME, DEVICE_ID
from secret_env import ACCESS_KEY, PASSWORD
from tuya_iot import (
    TuyaOpenAPI,
    AuthType,
)

openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
print("Connecting...")
response = openapi.connect(USERNAME, PASSWORD)
print(response)
print("API connection status:", openapi.is_connect())

def cmdPost():
    commands = {'commands': [{'code': 'switch', 'value': True}]}
    result = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)
    return result

result = cmdPost()
