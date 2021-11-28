import requests
product = 'discord'
headers = {
    'Accept': 'application/json',
}
params = (
    ('product', product),
)
response = requests.get('https://5sim.net/v1/guest/prices', headers=headers, params=params)
response = response.json()['discord']
countrylist = []
for i in response:
    countrylist.append(i)

costs = []
for i in countrylist:
    operators = []
    for f in response[i]:
        operators.append(f)
    for z in operators:
        if float(response[i][z]['cost']) < 5 and int(response[i][z]['count']) > 200 and i != "usa" and i != "canada":
            costs.append(float(response[i][z]['cost']))
costs.sort()
for i in countrylist:
    operators = []
    for f in response[i]:
        operators.append(f)
    for z in operators:
        if float(response[i][z]['cost']) == costs[0] and int(response[i][z]['count']) > 200 and i != "usa" and i != "canada":
            country = i
            operator = z

print(f"country: {country}")
print(f"operator: {operator}")
input('Press enter to exit')