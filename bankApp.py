# 1. Note the variable login_types, the list of account types.
login_types = ["admin","moderator", "user", "guest"]
# 2. Complete the function called gatekeeper that returns the following error message strings in the following scenarios:
# For “admin”:
# program says “You have the privileges.”
# For “user”:
# program says “You have limited privileges.”
# For “guest”:
# program says “You have no privileges.”
def gatekeeper(login, account_age):
    if login == "admin" or login == "moderator":
        return "You have the privileges"
    elif login == "user" or account_age>=7:
        return "You have limited privileges."
    elif login == "guest":
        return "You have no privileges."
# 3. Call the gatekeeper function with a string and print what it returns.
print(gatekeeper("admin",8))

# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.

# 5. Complete the function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
# 6. If loan_balance is zero or more, it says “you don’t owe any money”
    if loan_balance >= 0:
        return "You do not owe any money"
# 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
    else:
        return "You owe $" + str(loan_balance)
    return

# 8. Call your function with a negative and positive number and print what it returns.
print(check_balance(300))
