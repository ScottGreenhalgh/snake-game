from math import floor

currencies = (
  ('FIFTY', 5000),
  ('TWENTY', 2000),
  ('TEN', 1000),
  ('FIVE', 500),
  ('TWO', 200),
  ('ONE', 100),
  ('FIFTY_PENCE', 50),
  ('TWENTY_PENCE', 20),
  ('TEN_PENCE', 10),
  ('FIVE_PENCE', 5),
  ('TWO_PENCE', 2),
  ('ONE_PENCE', 1)
)

def calculateChange(x, coins):
    change = {}
    for denomination, value in coins:
        while value <= x:
            change[denomination] = change.get(denomination, 0) + 1
            x = x - value
    return change


amount = (float(input("Enter an amount:\n£"))*100)

print(calculateChange(amount, currencies))
