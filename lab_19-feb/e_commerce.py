cart_value=int(input("Enter the cart value: "))
customer_membership=input("Enter the customer membership (gold/silver/platinum): ").lower()
if customer_membership=="gold" or customer_membership=="platinum" or customer_membership=="silver":
 print("membership type is valid.")
else:
 print("invalid membership")
 exit()
 
festival_season=input("Is it a festival season? (yes/no): ").lower()
if (festival_season=="yes" and cart_value>=10000):
  discount= 4500
  total_amount=cart_value-discount
  print("Total amount after discount: ", total_amount)
else:
 print("No discount applied. Total amount: ", cart_value)