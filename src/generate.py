import json, os, requests, sys

def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    descriptions = []
    left = count
    while left > 0:
        descriptions += requests.get('https://baconipsum.com/api/?type=meat-and-filler&paras=' + str(left)).json()
        left = count - len(descriptions)
    for i in range(0, count):
        index = i + 1
        item = {
            'name': 'Blockie #' + str(index),
            'description': descriptions[i],
            'image': 'https://picsum.photos/id/' + str(index % 1000) + '/500',
        }
        folder = os.path.join(base, str(index))
        filename = os.path.join(folder, 'index.json')
        if not os.path.exists(folder): os.makedirs(folder)
        with open(filename, 'w') as outfile:
            json.dump(item, outfile, separators=(',', ':'))

if __name__ == '__main__': main()
