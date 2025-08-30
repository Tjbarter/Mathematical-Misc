import matplotlib.pyplot as plt
import random as rd

initial_bet = 1
initial_balance = 10000000
max_steps=10000000

def generate_random_walk_martingale(initial_bet, initial_balance, max_steps):
    balance_values = []
    bet = initial_bet
    balance = initial_balance
    
    for i in range(max_steps):
        # Adjust the bet if it's greater than the current balance
        if balance < bet:
            bet = balance
        
        random_outcome = rd.randint(0, 1)
        
        if random_outcome == 0:  # Lose the bet
            balance -= bet
            bet *= 2  # Double the bet
        else:  # Win the bet
            balance += bet
            bet = initial_bet  # Reset the bet

            bet = min(bet, 1000000)
        
        balance_values.append(balance)
        
        # Stop if balance goes to zero
        if balance <= 0:
            print(f"Bust at step {i} with balance {balance}")
            break
    
    return balance_values


balance_history = generate_random_walk_martingale(initial_bet, initial_balance, max_steps)
time_values = range(len(balance_history))

print(f"Final Balance: {balance_history[-1]}")
print(f"Highest Balance: {max(balance_history)}")
print(f"Greatest Profit Point: {((max(balance_history) - initial_balance) / initial_balance) * 100}%")

# Plot the balance history
plt.figure(figsize=(10, 6))
plt.plot(time_values, balance_history, label='Balance History', color='orange')
plt.axhline(y=0, color='red', linestyle='--', label='Bust Line')
plt.grid(True)
plt.xlabel('Steps')
plt.ylabel('Balance')
plt.title('Balance Over Time with Martingale Strategy')
plt.legend()
plt.show()


