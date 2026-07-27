
products = input("Enter products: ")
search_product = input("Enter product to search: ")

product_list = []

for product in products.split(","):
    product = product.strip().lower()
    product = product[0].upper() + product[1:]
    product_list.append(product)

print("Product list:")
print(product_list)


print("\nTotal products:", len(product_list))

if len(product_list) % 2 == 1:
    middle = len(product_list) // 2
    print("\nMiddle product:", product_list[middle])

max_count = 0

for product in set(product_list):
    if product_list.count(product) > max_count:
        max_count = product_list.count(product)

print("\nMost purchased product(s):")

for product in sorted(set(product_list)):
    if product_list.count(product) == max_count:
        print(product + ":", max_count, "time(s)")

search_product = search_product.strip().lower()
search_product = search_product[0].upper() + search_product[1:]

count = product_list.count(search_product)

if count > 0:
    print("\n" + search_product, "appears", count, "time(s).")
else:
    print("\n" + search_product, "has not been purchased.")

product_list.insert(0, "Nabati cake ")

if "Milk" in product_list:
    product_list.remove("Milk")

print("\nUpdated product list:")
print(product_list)