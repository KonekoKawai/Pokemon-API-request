import requests;
pokemonName = input("Enter the pokemon name: "); #������ ����� ��������
req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName}'); #GET-������ �� ���� � ������ ��������
if req.text != "Not Found": #���� �������� ���������� �������
    print("-------------------------------------\n")
    print('name: ', req.json()['name']);
    print('id:', req.json()['id']);
    print('order_id:', req.json()['order']);
    print('height:', req.json()['height']);
    print('weight:', req.json()['weight']);
else:
    print("Not Found pokemon");
req.close();

req = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemonName}') #GET-������ �� ���� � ������ ��������
if req.text != "Not Found": #���� �������� ���������� �������
    print('base_happiness:', req.json()['base_happiness']);
    print('capture_rate:', req.json()['capture_rate']);
    print('color.name:',req.json()['color']['name']);
    print('shape:', req.json()['shape']['name']);
    print('is_legendary:', req.json()['is_legendary']);
    print('is_mythical:', req.json()['is_mythical']);
    print("\n-------------------------------------")
else:
    print("Not Found pokemon-species");
req.close();

input();