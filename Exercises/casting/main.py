# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print(f"Leek is {leek_price} euro per kilo.")

order_leek = "leek 4"
number_ordered_leek = order_leek[5]
sum_total_leek = int(number_ordered_leek) * leek_price
print(sum_total_leek)

broccoli_price = 2.34
order_broccoli = "broccoli 1.6"
number_ordered_broccoli = order_broccoli[9:12]
sum_total_broccoli = (float(number_ordered_broccoli) * broccoli_price)
print(f"{number_ordered_broccoli}kg broccoli costs {round(sum_total_broccoli,2)}e")