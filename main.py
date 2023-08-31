import requests

# Замініть 'YOUR_ACCESS_TOKEN' на ваш реальний токен доступу API з Wit.ai
access_token = 'RUL4T6H5GHIPS53XYEERISO2C7JOLLR4'

def get_intent_and_entities(text):
    url = f'https://api.wit.ai/message?v=2022-09-01&q={text}'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)
    data = response.json()

    intent = data['intents'][0]['name'] if 'intents' in data else None
    entities = data['entities'] if 'entities' in data else {}

    return intent, entities

# Приклад вхідного тексту
input_text = "I'd like to order two cups of dark roast coffee with extra milk."

intent, entities = get_intent_and_entities(input_text)

print("Intent:", intent)
print("Entities:", entities)
