from random import Random, random
from dictsave import get


def choiceOne(dic: dict, sum: float) -> str:
    # dic = { key1: 2, key2: 3, key3: 5, '$sum': 10 }
    # chance: key1 - 2/10, key2 - 3/10, key3 - 5/10
    # then, choice one key by chance of each key
    keys = []
    chances = []
    current = 0
    for key, value in dic.items():
        keys.append(key)
        current += value
        chances.append(current)

    rand_num = random() * sum
    idx = 0
    # print(dic)
    # print(sum)
    # print(chances)
    for cur in chances:
        if rand_num < cur:
            break
        idx += 1
    return keys[idx]


def getSaying(data: dict) -> str:
    marks = [".", ",", "!", "?"]
    words = list(data.keys())
    word = words[int(random() * len(words))]
    result = word
    countdown = 10
    while (countdown > 1):
        cur = data[word]['$data']
        next = choiceOne(cur, data[word]['$sum'])
        word = next
        result += f'{"" if next in marks else " "}{next}'
        countdown -= 1
    return result


data = get('data/wordchain.json')
for i in range(10):
    print(getSaying(data))
