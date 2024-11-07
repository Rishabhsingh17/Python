def finance(salary,needs_percnt=0.5,wants_percnt=0.2,savings_percnt=0.3):
    if needs_percnt + wants_percnt + savings_percnt != 1:
        raise ValueError("The Percentage you had given should be combined make 100% or 1.")
    
    needs_amount = salary * needs_percnt
    wants_amount = salary * wants_percnt
    savings_amount = salary * savings_percnt

    needs_breakdown = {
        "Housing": needs_amount * 0.3,
        "Utilities": needs_amount * 0.1,
        "Groceries": needs_amount * 0.2,
        "Transportation": needs_amount * 0.1,
        "Insurance": needs_amount * 0.1,
        "Healthcare": needs_amount * 0.1,
    }
    wants_breakdown = {
        "Dining Out": wants_amount * 0.2,
        "Entertainment": wants_amount * 0.15,
        "Hobbies": wants_amount * 0.15,
        "Shopping": wants_amount * 0.2,
        "Subscriptions": wants_amount * 0.1,
        "Travel & Leisure": wants_amount * 0.2,
    }
    savings_breakdown = {
        "Emergency Fund": savings_amount * 0.25,
        "Retirement Savings": savings_amount * 0.3,
        "Investments": savings_amount * 0.25,
        "Large Purchase Savings": savings_amount * 0.1,
        "Debt Repayment": savings_amount * 0.1,
    }
    print(f"Monthly Salary: ₹{salary}")
    print("\nNeeds ({}%):".format(int(needs_percnt * 100)))
    for item, amount in needs_breakdown.items():
        print(f"  {item}: ₹{amount:.2f}")

    print("\nWants ({}%):".format(int(wants_percnt * 100)))
    for item, amount in wants_breakdown.items():
        print(f"  {item}: ₹{amount:.2f}")

    print("\nSavings ({}%):".format(int(savings_percnt * 100)))
    for item, amount in savings_breakdown.items():
        print(f"  {item}: ₹{amount:.2f}")

salary = int(input("Enter your monthly Salary:- "))
try:
    needs_pct = float(input("Enter percentage for Needs (default 50%): ") or 0.5) / 100
    wants_pct = float(input("Enter percentage for Wants (default 20%): ") or 0.2) / 100
    savings_pct = float(input("Enter percentage for Savings (default 30%): ") or 0.3) / 100

    finance(salary, needs_pct, wants_pct, savings_pct)

except ValueError as e:
    print("Error:", e)
