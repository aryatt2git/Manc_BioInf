import requests
import json

gene = 'NM_002112.4'
url = 'https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Frest.variantvalidator.org%2F&data=05%7C02%7Carjun.ryatt%40ouh.nhs.uk%7C01a43330511a45d0864308de0649c33f%7C25d273c3a8514cfba239e9048f989669%7C0%7C0%7C638955112102636801%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=OBIzXux8khG0UHbDYjQTc3tNGWJ1%2F5iCXFX1Jbz6u4I%3D&reserved=0'
request = f'/VariantValidator/tools/gene2transcripts/{gene}'
response = requests.get(f'{url}{request}')

print(response.text)

resp_dict = json.loads(response.text)
print(resp_dict.keys())

for keys, values in resp_dict.items():
print(f'{keys}: {values}')