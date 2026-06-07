# Приложение БАНК для отслеживания накапливаемых на счетах клиентов банка сумм.
# Таблица Клиент должна содержать следующую информацию: Код клиента, Клиент (Ф.И.О.), Периодический платеж, Годовой %,
# Срок вклада, Пластиковая карта (логическое поле), Конечная сумма.

import sqlite3 as sq
from databases import bank_clients


with sq.connect('bank.db') as con:
    bank = con.cursor()

    bank.execute("DROP TABLE IF EXISTS Client")
    bank.execute("""CREATE TABLE IF NOT EXISTS Client (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT NOT NULL,
        periodic_payment REAL NOT NULL,
        interest_rate REAL NOT NULL,
        deposit_term INTEGER NOT NULL,
        has_plastic_card INTEGER NOT NULL DEFAULT 0,
        final_sum REAL
    )""")

    bank.executemany("INSERT INTO Client VALUES (NULL, ?, ?, ?, ?, ?, ?)", bank_clients)

    bank.execute("SELECT client_id, periodic_payment, interest_rate, deposit_term FROM Client")
    clients_data = bank.fetchall()

    for client in clients_data:
        c_id, payment, interest, term = client
        total_invested = payment * term
        interest_gained = total_invested * (interest / 100) * (term / 12)
        calculated_final = total_invested + interest_gained

        bank.execute(
            "UPDATE Client SET final_sum = ? WHERE client_id = ?",
            (calculated_final, c_id)
        )


    def print_table(title_text):
        print('\n', title_text)
        print(f"{'ID':<4} {'Ф.И.О.':<28} {'Платеж':<10} {'Годовой %':<9} {'Срок (мес)':<10} {'Карта':<6} {'Конечная сумма':<15}")
        bank.execute("SELECT * FROM Client")
        for row in bank.fetchall():
            c_id, fio, payment, interest, term, card, final = row
            card_str = "Да" if card == 1 else "Нет"
            print(f"{c_id:<4} {fio:<28} {payment:<10} {interest:<9} {term:<10} {card_str:<6} {final:<15.2f}")


    print_table("Исходное содержимое таблицы Client")

    print("\n 1. Клиенты со сроком > 12 месяцев:")
    bank.execute("SELECT fio, deposit_term FROM Client WHERE deposit_term > 12")
    for row in bank.fetchall():
        print(f" - {row[0]} (Срок: {row[1]} мес.)")


    print("\n 2. Клиенты с пластиковой картой:")
    bank.execute("SELECT fio FROM Client WHERE has_plastic_card = 1")
    for row in bank.fetchall():
        print(f" - {row[0]}")


    print("\n 3. Высокий платеж (>13000) и ставка (>12%):")
    bank.execute("SELECT fio, periodic_payment, interest_rate FROM Client WHERE periodic_payment > 13000 AND interest_rate > 12")
    for row in bank.fetchall():
        print(f" - {row[0]} (Платеж: {row[1]}, Ставка: {row[2]}%)")

    bank.execute("UPDATE Client SET interest_rate = 16.5 WHERE interest_rate < 11.0")

    bank.execute("UPDATE Client SET has_plastic_card = 1 WHERE deposit_term >= 36")

    bank.execute("UPDATE Client SET periodic_payment = 11000.0 WHERE client_id = 2")

    print_table("Таблица после проведения 3-х операций редактирования")

    bank.execute("DELETE FROM Client WHERE client_id = 6")

    bank.execute("DELETE FROM Client WHERE final_sum < 150000.0")

    bank.execute("DELETE FROM Client WHERE deposit_term <= 12 AND has_plastic_card = 0")

    print_table("Итоговая таблица после проведения 3-х операций удаления")