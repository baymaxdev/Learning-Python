# A program that manages a person's pocket money and keeps a check of it

# ==================== POCKET MONEY ====================

monthly_pocket_money = float(input("Enter your monthly pocket money: "))

initial_amount_added = float(input("Enter the amount you want to add: "))

current_balance = monthly_pocket_money + initial_amount_added

print(f"\nYour pocket money becomes: Rs. {current_balance}")

# ==================== ADD MORE MONEY ====================

another_addition = "yes"

while another_addition == "yes":
    additional_amount = float(input("Enter the additional amount: "))

    current_balance = current_balance + additional_amount

    print(f"Your updated balance is: Rs. {current_balance}")

    another_addition = input("Do you want to add more money? (yes/no): ").lower()

print(f"\nYour available balance is: Rs. {current_balance}")

# ==================== EXPENSE VARIABLES ====================

total_expense = 0
expense_count = 0
largest_expense = 0
largest_expense_name = ""
expense_categories = []

another_expense = "yes"

# ==================== EXPENSE SECTION ====================

while another_expense == "yes":
    expense_amount = float(input("\nHow much amount did you spend? "))

    if expense_amount <= current_balance:
        expense_name = input("Where did you spend the money? ")

        expense_category = input("What category is this expense? ")

        expense_categories.append(expense_category)

        expense_count += 1

        current_balance = current_balance - expense_amount

        total_expense += expense_amount

        # Check for the biggest expense

        if expense_amount > largest_expense:
            largest_expense = expense_amount

            largest_expense_name = expense_name

        # Show expense information

        print(
            f"\nYou spent Rs. {expense_amount} on {expense_name}."
            f"\nCategory: {expense_category}"
            f"\nYour new balance is: Rs. {current_balance}"
        )

        # Low balance warning

        if current_balance < 1000:
            print("\n==== WARNING! ====")
            print("Your balance is getting low!")

            add_money = input("Do you want to add more money? (yes/no): ").lower()

            if add_money == "yes":
                money_added = float(input("Enter the amount you want to add: "))

                current_balance = current_balance + money_added

                print(f"Your updated balance is: Rs. {current_balance}")

    else:
        print("\n==== INSUFFICIENT BALANCE! ====")
        print(f"You cannot spend Rs. {expense_amount}.")
        print(f"Your current balance is: Rs. {current_balance}")

    another_expense = input("\nDo you want to add another expense? (yes/no): ").lower()

# ==================== FINAL SUMMARY ====================

print("\n\n========== SUMMARY ==========")

print(f"Total expense: Rs. {total_expense}")

print(f"Remaining pocket money: Rs. {current_balance}")

print(f"Number of expenses: {expense_count}")

# Show biggest expense only if an expense was made

if expense_count > 0:
    print(
        f"Biggest expense: Rs. {largest_expense} "
        f"which was spent on {largest_expense_name}"
    )

# Show expense categories

if len(expense_categories) > 0:
    print("\nCategories of your expenses:")

    for category in expense_categories:
        print(f"- {category}")
