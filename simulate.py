import multiprocessing as mp
import requests

#pool = mp.Pool(mp.cpu_count())

# result = [pool.apply(requests
#            .post('http://localhost:3000/'),
#            data={"query": "{getCitiesByPostCode(postCode: \"12107\"){cityName}}"}) for i in range(2)]

#pool.close()

result = requests.post('http://localhost:3000/', json={'query': '{getCitiesByPostCode(postCode: "12107"){cityName}}'})

print(result)