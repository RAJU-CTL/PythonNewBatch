print("Hello Students")

# Developer can write english here - ignored by Python
# This statement starting with # is caled Single Line Comment

'''
This is called Comment Block - Multi Line comment
You can write Paragraphs here - Three Single Quotes '
'''

'''
4 Items in Shopping cart
Bill total - taxes = 12.36
'''
toothbursh_price = 2.99
photo_frame_price = 9.99
toys_price =10.39
washer = 699.99

total = toothbursh_price + photo_frame_price + toys_price + washer
print("Total Bill Price : ", total)

tax = total*0.1236
print("Tax Amount :: ", tax)

total_billing_amount = total + tax
print("total billing amount :: ", total_billing_amount)