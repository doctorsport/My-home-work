#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для анализа нажмите 'A'").upper()
    if control == 'Q':
        print('Процедура завершена')
        break
        num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
