```python
def hats_on_cats():
    number_of_circles = 100
    cats = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10,\
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
        21, 22, 23, 24, 25, 26, 27, 28, 29, \
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, \
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, \
        51, 52, 53, 54, 55, 56, 57, 58, 59, \
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, \
        70, 71, 72, 73, 74, 75, 76, 77, 78, 79, \
        80, 81, 82, 83, 84, 85, 86, 87, 88, 89, \
        90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    cats_with_hats = []
    cats_without_hats = []
    cats_in_question = []
    cats_with_hats.extend(cats[::1])
    i = 2
    while i <= number_of_circles:
        cats_in_question = (cats[::i])
        check = any(item in cats_with_hats for item in cats_in_question)
        if check == True:
            cats_without_hats.extend(cats_in_question)
            cats_with_hats = list(set(cats_with_hats) ^ set(cats_in_question))
            i += 1
        else:
            cats_with_hats.extend(cats_in_question)
            cats_without_hats = list(set(cats_without_hats) ^ set(cats_in_question))
            i += 1
        

    return set(cats_with_hats)

hats_on_cats()
```
