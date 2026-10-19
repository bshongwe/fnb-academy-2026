# The High-Score Tracker Game

best_score = None

while True:
    user_input = input("Enter game score (or type 'stop' to end): ").strip().lower()

    if user_input == "stop":
        print("Game session ended!")
        if best_score is None:
            print("No scores were recorded.")
        else:
            print(f"Best score this session: {best_score}")
        break

    score = int(user_input)

    if best_score is None:
        best_score = score
        print(f"Best score recorded: {best_score}")
    elif score > best_score:
        best_score = score
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")