# coding=utf-8

if __name__ == "__main__":
    items = [{'name': 'Homer', 'age': 39},
             {'name': 'Bart', 'age': 10},
             {"name": 'cater', 'age': 20}]

    new_items = sorted(items, key=lambda x: x.get('age'))
    print(new_items)

    new_items = sorted(items, key=lambda x: x.get('age'), reverse=True)
    print(new_items)


