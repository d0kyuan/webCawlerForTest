
import requests

# 4.1【男生可承租】且【位於新北】的租屋物件
r = requests.post('http://192.168.0.4:8080/api/product/get', data={
    "region": [3],
    "pSexReq": 1,
})
print(r.text)


# 以【聯絡電話】查詢租屋物件
r = requests.post('http://192.168.0.4:8080/api/product/get', data={
    "sPhone": "0912-534-015",
})
print(r.text)


# 所有【非屋主自行刊登】的租屋物件
r = requests.post('http://192.168.0.4:8080/api/product/get', data={
    "sType": 2,
})
print(r.text)

# 4.4【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件
r = requests.post('http://192.168.0.4:8080/api/product/get', data={
    "region": [1],
    "sSex": 2,
    "sName": "吳"
})
print(r.text)
