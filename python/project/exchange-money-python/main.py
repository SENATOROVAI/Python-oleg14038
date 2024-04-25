from run_exchangerates import exchange

if __name__ == "__main__":
    cur = input("Input the curreny:").upper()
    amount = input("Inputrailt amount: ")
    print(exchange(f"{cur}", f"{amount}"))
