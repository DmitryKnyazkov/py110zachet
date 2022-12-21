from faker import Faker
import Conf
import random
import json


def model():
    return Conf.model

# def pk():
#     a = random.randint(1,5)
#     return a

# def fields():
#     ...


def title():
    with open("Books.txt", encoding="utf-8") as b:
        # a = b.read()
        # print(a)
        list_t = []
        for line in b:  # файл является итератором, который построчно возвращает свое содержимое
            line = line.strip()
            list_t.append(line)
        a = random.choice(list_t)
    return a

def year():
    a = random.randint(1950, 2022)
    return a

def pages():
    a = random.randint(100, 300)
    return a

def isbn13():
    fake_ru = Faker("ru_RU")
    fake_name = fake_ru.isbn13()
    return fake_name

def rating():
    a = random.uniform(0,5)
    a = round(a, 1)
    return a


def price():
    a = random.uniform(10,20)
    a = round(a, 2)
    return a


def author():
    a = random.randint(1,3)
    if a == 1:
        fake_ru = Faker("ru_RU")
        fake_name = fake_ru.name()
        return fake_name
    elif a == 2:
        fake_ru = Faker("ru_RU")
        fake_name1 = fake_ru.name()
        fake_name2 = fake_ru.name()
        b = f"{fake_name1} и {fake_name2}"
        return b
    elif a == 3:
        fake_ru = Faker("ru_RU")
        fake_name1 = fake_ru.name()
        fake_name2 = fake_ru.name()
        fake_name3 = fake_ru.name()
        b = f"{fake_name1}, {fake_name2} и {fake_name3}"
        return b

def main():
    list_ = []
    schet = 0
    for _ in range(99):
        schet += 1
        dict_ = {"model": model(),
                 "pk": schet,
                 "fields": {"title": title(),
                            "year": year(),
                            "pages": pages(),
                            "isbn13": isbn13(),
                            "rating": rating(),
                            "price": price(),
                            "author": author()}}
        list_.append(dict_)

    print(list_)
    with open("LIST.json", "w", encoding="utf-8") as li:
        json.dump(list_, li, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    main()


