import requests
import json


status = 'available'

New_Pet = {
    'id': 666666,
    'category': {
      'id': 666,
        'name': 'Loken'
    },
    'name': 'Dog',
    'photoUrls': [
        'string'
    ],
    'tags': [
        {
            'id': 0,
            'name': 'string'
        }
    ],
    'status': 'available'
}

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(New_Pet))

print(res.status_code)
print(res.json())

res_2 = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers = {'accept': 'application/json'})
print(res_2.status_code)
print(res_2.json())

New_name = {
    'id': 666666,
    'category': {
      'id': 666,
        'name': 'Maffin'
    },
    'name': 'Dog',
    'photoUrls': [
        'string'
    ],
    'tags': [
        {
            'id': 0,
            'name': 'string'
        }
    ],
    'status': 'available'
}

res_3 = requests.put(f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(New_name))
print(res_3.status_code)
print(res_3.json())


res_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/666666',headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(res_4.status_code)
print(res_4.json())




