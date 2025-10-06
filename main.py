# main.py
import os
from solders.keypair import Keypair
import pandas as pd

def generate_solana_wallet():
    # Генерация нового кошелька
    keypair = Keypair()
    public_key = str(keypair.pubkey())
    private_key = keypair.secret().hex()
    seed = keypair.seed.hex()
    return public_key, private_key, seed

def save_to_excel(wallets, filename="solana_wallets.xlsx"):
    # Создание DataFrame
    df = pd.DataFrame(wallets, columns=["address", "Private key", "Seed"])
    # Сохранение в Excel
    df.to_excel(filename, index=False)
    print(f"Кошельки сохранены в {filename}")

def main():
    print("=== Генератор Solana кошельков ===")
    try:
        num_wallets = int(input("Введите количество кошельков для генерации: "))
        if num_wallets <= 0:
            print("Ошибка: Введите положительное число.")
            return
    except ValueError:
        print("Ошибка: Введите корректное число.")
        return

    wallets = []
    for _ in range(num_wallets):
        address, private_key, seed = generate_solana_wallet()
        wallets.append((address, private_key, seed))
        print(f"Сгенерирован кошелек: {address}")

    # Сохранение в Excel
    save_to_excel(wallets)
    print("Генерация завершена!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
