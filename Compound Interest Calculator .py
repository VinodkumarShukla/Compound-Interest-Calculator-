# Function to calculate the final account balance
def calculate_balance(P, r, n, t):
    P_ = P * (1 + r / n) ** (n * t)
    interest_earned = P_ - P
    return P_, interest_earned


# Function to display the results with proper formatting
def display_results(P, P_, interest_earned):
    print(f"Original Principal (P): ${P:.2f}")
    print(f"Amount of Interest Earned (P'-P): ${interest_earned:.2f}")
    print(f"Total Value of the Account at the End (P'): ${P_:.2f}")


# Main program
while True:
    # Input from the user for the first set of parameters
    P = float(input("Enter the initial principal amount (P): $"))
    r = float(input("Enter the annual interest rate (in decimal form, e.g., 0.05 for 5%): "))
    n = int(input("Enter the number of times interest is compounded per year (e.g., 12 for monthly compounding): "))
    t = int(input("Enter the number of years to save (t): "))

    P_, interest_earned = calculate_balance(P, r, n, t)

    print("\nResults for the first set of parameters:")
    display_results(P, P_, interest_earned)

    # Ask if the user wants to compare with a second set of parameters
    compare = input("\nDo you want to compare with a second set of parameters? (yes/no): ").lower()

    if compare != "yes":
        break

    # Input from the user for the second set of parameters
    P2 = float(input("\nEnter the initial principal amount (P): $"))
    r2 = float(input("Enter the annual interest rate (in decimal form): "))
    n2 = int(input("Enter the number of times interest is compounded per year: "))
    t2 = int(input("Enter the number of years to save: "))

    P2_, interest_earned2 = calculate_balance(P2, r2, n2, t2)

    print("\nResults for the second set of parameters:")
    display_results(P2, P2_, interest_earned2)

    # Compare the results and determine which set of parameters produces the largest final balance
    if P_ > P2_:
        print("\nThe first set of parameters produces the largest final account balance (P').")
        break
    elif P_ < P2_:
        print("\nThe second set of parameters produces the largest final account balance (P').")
        break
    else:
        print("\nBoth sets of parameters produce the same final account balance (P').")
        break
