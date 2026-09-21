# бд
users_db = {
    "ivan": {"password": "password123", "ocinki": [10, 12, 4, 8, 3, 11, 5]},
    "pedro": {"password": "qwerty2026", "ocinki": [12, 11, 10, 9, 12]},
    "Sigma": {"password": "321", "ocinki": [3, 2, 4, 5, 1, 4]},
    "v321": {"password": "admin", "ocinki": [7, 8, 6, 9, 4, 11]}
}

print("=== Авторизація в системі оцінок ===")
login = input("Введіть логін: ").strip()
password = input("Введіть пароль: ").strip()

# Перевірка логіна та пароля
if login in users_db and users_db[login]["password"] == password:
    user_data = users_db[login]
    ocinki = user_data["ocinki"]
    
    print(f"\nУспішний вхід! Вітаємо, {login}.")
    print(f"Ваш перелік оцінок: {ocinki}")
    
    # Підрахунок оцінок
    zad = 0
    nezad = 0
    
    for ocinki in ocinki:
        if 5 <= ocinki <= 12:
            zad += 1
        elif 1 <= ocinki <= 4:
            nezad += 1

    # Виведення результатів
    print(f"Кількість задовільних оцінок (5-12): {zad}")
    print(f"Кількість незадовільних оцінок (1-4): {nezad}")

else:
    print("\nПомилка: Неправильний логін або пароль!")