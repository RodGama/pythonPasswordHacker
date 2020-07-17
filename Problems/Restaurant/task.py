import itertools


for main_course, price_main_course in zip(main_courses, price_main_courses):
    for dessert, price_dessert in zip(desserts, price_desserts):
        for drink, price_drink in zip(drinks, price_drinks):
            price = price_main_course + price_dessert + price_drink
            if price_main_course + price_dessert + price_drink < 31:
                print(main_course, dessert, drink, price)
