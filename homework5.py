immutable_var = (1, 2, 3, 4, "door", "wood", True)
print(immutable_var)
# immutable_var[1] = 5      # Кортежи не поддерживают изменение элементов т.к. в нем содержится не список, а ссылки.
                            # Но в случае добавления списка, последний можно изменять в кортеже.
mutable_list = ["Food", "Table", "Window", "Floor"]
mutable_list[1] = "Door"
mutable_list[2] = "Wood"
print(mutable_list)