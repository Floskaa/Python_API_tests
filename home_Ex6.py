import requests


response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

response_1 = response.history[0]
response_2 = response.history[1]
response_3 = response.history[2]

end_response = response

print(response_1.url)
print(response_2.url)
print(response_3.url)
print(end_response.url)