#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user_data(**user_data) -> None:
    print(f'Имя: {user_data.get("name")}, '
          f'фамилия: {user_data.get("surname")},'
          f'год рождения: {user_data.get("birth_year")},'
          f'город проживания: {user_data.get("city")},'
          f'email: {user_data.get("email")},'
          f'телефон: {user_data.get("phone")}')

if __name__ == '__main__':
    user = {
        'name': 'Берик',
        'surname': 'Саттыклышов',
        'birth_year': '1981',
        'city': 'Нур-Султан',
        'email': 'doctor@gmail.com',
    }

    print_user_data(**user)
