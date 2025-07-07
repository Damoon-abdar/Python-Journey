import time
import math            # (math isn’t actually used, but I left the import in case you add features)

# ─────────────────────────────────────────────────────────
# 1.  ACCOUNT NUMBER  (exactly 12 digits, numeric only)
# ─────────────────────────────────────────────────────────
while True:
    acct = input("Enter your 12-digit account number: ").strip()
    if acct.isdigit() and len(acct) == 12:
        print("Great, let's continue.")
        break
    print("❌  Account number must be exactly 12 digits and contain no letters.")

# ─────────────────────────────────────────────────────────
# 2.  PHONE NUMBER  (Canadian 10-digit format)
# ─────────────────────────────────────────────────────────
while True:
    phone_raw = input("Phone linked to this account (+1 …): ").strip()
    phone = phone_raw.replace("-", "")
    if phone.isdigit() and len(phone) == 10:
        print("Great, moving on…")
        break
    print("❌  Phone number must contain exactly 10 digits (e.g., 647-939-6916).")

# Name lookup
clients = {
    "6479396961": "Damon Abedie",
    "4374554119": "Baran Abedie",
    "6479326965": "Mohammad Jaryani",
}
print(f"Welcome, {clients.get(phone, 'valued customer')}!")

# ─────────────────────────────────────────────────────────
# 3.  INVESTMENT DETAILS
# ─────────────────────────────────────────────────────────
while True:
    principal_raw = input("How much would you like to invest? $").strip()
    principal_raw = principal_raw.replace(",", "").replace("$", "")
    try:
        principal = float(principal_raw)
        if principal <= 0:
            raise ValueError
        break
    except ValueError:
        print("❌  Please enter a positive number.")

# Confirm APR
while True:
    agree = input("Our APR is 21 %. Do you agree? (Y/N): ").strip().upper()
    if agree == "Y":
        break
    if agree == "N":
        print("You must enter Y to continue.")
        continue
    print("❌  Please type Y or N only.")

# Select term length
valid_terms = {3, 5, 7}
while True:
    years_raw = input("Choose a term (3 / 5 / 7 years): ").strip()
    if years_raw.isdigit() and int(years_raw) in valid_terms:
        years = int(years_raw)
        break
    print("❌  Please enter 3, 5, or 7.")

APR = 0.21
n = 2
amount = principal * (1 + APR / n) ** (n * years)
amount = round(amount, 2)

time.sleep(0.8)
print(f"\nAfter {years} years your balance will be: ${amount:,.2f}")

authxy = input("Dear user, we can let you contact one of our tellers as soon as possible. Would you like to proceed? (Y/N): ")
authxy = authxy.upper()
if authxy == "Y":
    print("Okay! You can call one of these numbers: ")
    num1ban = "6479396992"
    num2ban = "6489396961"
    num3ban = "6548769872"

