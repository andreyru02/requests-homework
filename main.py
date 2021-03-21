import requests


def find_intelligence(token, names):
    data = {}
    for name in names:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        res = requests.get(url).json()

        for results_list in res['results']:
            results_name = results_list['name']
            intelligence = results_list['powerstats']['intelligence']

            if name == results_name:
                data[results_name] = int(intelligence)

    hero_list = list(data.items())
    hero_list.sort(key=lambda i: i[1])

    print(f'Самый умный: {hero_list[-1][0]}. Его интеллект равен {hero_list[-1][1]}.')


if __name__ == '__main__':
    find_intelligence(2619421814940190, ['Hulk', 'Captain America', 'Thanos'])
