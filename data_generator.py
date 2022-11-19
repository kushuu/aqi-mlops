import json
import requests


API_TOKEN = "45fea81fd7a1843a90d934ac3a9d9e69411631ea"

if __name__ == '__main__':
    cities = ['bangalore', 'mumbai', 'delhi', 'kolkata', 'london', 'pune']
    
    for c in cities:
        url = f"https://api.waqi.info/feed/{c}/?token={API_TOKEN}"
        response = requests.get(url)
        # print(response.text)
        rel_data = json.loads(response.text)['data']
        # aqi = rel_data['aqi']
        # city = rel_data['city']['name']
        # print(aqi, '\t', city)
        print(json.dumps(rel_data, indent=2))