import requests



url = 'http://localhost:5000/chat'
while True:
    question = input("How can I help you? ")
    data = {'question': question}
    response = requests.post(url, data=data)
    print(response.text)
