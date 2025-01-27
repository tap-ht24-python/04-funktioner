
# övning 1.1
#limit = 15
#index = 5
#while index <= limit:
#    print(index)
#    index = index + 2

# övning 1.3
counter = 0
for i in range(6):
    counter += i
print(counter)

# 0 + 1 + 2 + 3 + 4 + 5 == 15
# i är en förkortning av "index"


list = [1, -2, 3, -2, 4, -3]
summa = 0
for item in list:
    summa += item
print("Summan är: " + str(summa))
