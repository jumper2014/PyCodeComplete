# coding=utf-8

if __name__ == "__main__":
    items = [{'name': 'Homer', 'age': 39},
             {'name': 'Bart', 'age': 10},
             {"name": 'cater', 'age': 20}]

    items.sort(key=lambda x: x.get("age"))
    print(items)

    items.sort(key=lambda x: x.get("age"), reverse=True)
    print(items)

