#мебель, и ее продажа
# список мебели и ее цены
import sqlite3
from time import sleep
fora_1 = {
    'Кровать 1сп':71910,
    'Кровть спальняя':55400,
    'Кровать прямоуг':22260,
    'Кровать Cayenne':37510,
    'Кровать двух ярус.':28010,
    'Кровать Premier':85560,
    'Кровать 2сп. Maxx':53220,
    'Кровать-Диван':46620,
    'Кровать-диван, мягкая накладка Ultra Ivory':41040,
    'Кровать 1 сп':38920,
    'Кровать 2 сп':59450,
    'Кровать 2сп. Cayenne 6':43180,
    'Кровать 2 сп., мягк.изг.шоко':28870,
    'Светильник лен.светодиод для основ.кровати 1200 AR8':6400,
    'Комплект из двух подушек для дивана-кровати А61':9500,
    'Ящик выкатной только для дивана A61':4250,
    'Ящик подкроватный для 1,5сп.кровати':6640,
    'Панель прикроватная':None,
    'Усиленный газлифт для кроватей':3000,
    'Светильник для кровати на гибкой ножке':4100,
    'Комплект подушек 5шт. для дивана-кровати A61':8500,
    'Ящик подкроватный для 1, 2сп.кроватей':7120,
    'Ящик подкроватный для 1, 2 сп. кроватей':5940,
    'Комплект подушек 2шт. для дивана-кровати A61; A6B':4400,
    'Светильник лен.светодиод для основ.кровати 900 AR9':6600
}
database = sqlite3.connect('fora.db')
cursor = database.cursor()

price_fora = int(input('Если нужна мебель, то введите число 20000, иначе 0: '))

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    money BIGINT
)""")
database.commit()

def reg():
    global name
    name = input('Login: ')
    money = int(input('Yor cahs: '))
    if money < 2500:
        print('У вас не достаточно средств!')
        exit()
    cursor.execute("SELECT user FROM users WHERE user = (?)", [name])
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users(user,money) VALUES (?,?)", [name, money])
        database.commit()
        print('Вы зарегистрированны в базе!')
        func_fora()
    else:
        print('Вы уже есть в базе данных!')
        sleep(5)
        func_fora()

def func_fora():
    for i in fora_1:
        fora_name = i
        price = fora_1[i]
        cursor.execute("SELECT money FROM users WHERE user = (?) AND money >= (?)", [name,price])
        if cursor.fetchone() is None:
            continue
        else:
            if price >= price_fora:
                print('У вас хватило денег')
                sleep(1.2)
                print(f'Название:{fora_name}')
                print(f'Цена:{price}')
                sleep(3)
                print()
            elif price == price_fora:
                print('У вас хватило денег')
                sleep(1.2)
                print(f'Название:{fora_name}')
                print(f'Цена:{price}')
                sleep(3)
                print()
reg()
