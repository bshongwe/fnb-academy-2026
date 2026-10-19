# Smart ATM Withdrawal Simulator

BALANCE = 10000000000.0

def run_atm():
    print("\n" + "=" * 40)
    print(f"{'WELCOME TO SMART ATM':^40}")
    print(f"{'Current Balance: R' + str(BALANCE):^40}")
    print("=" * 40)

    withdrawal = float(input("\nEnter withdrawal amount: ZAR"))

    if withdrawal <= 0:
        print("Invalid amount. You must withdraw more than ZAR0.")
    elif withdrawal <= BALANCE:
        remaining = round(BALANCE - withdrawal, 2)
        print(f"Withdrawal successful! Remaining balance: ZAR{remaining}")
    else:
        print("Declined. Insufficient funds.")

    print("=" * 40)

run_atm()