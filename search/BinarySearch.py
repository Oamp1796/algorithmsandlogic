import json

# Cargando los elementos de las listas a través de un json
with open("items.json", "r") as file:
  data = json.load(file)

#La función binary_search me devuelve el valor de posición del item que estamos buscando dentro de la lista

class BinarySearch():
    def binary_search(self, list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
                mid = (low + high) // 2  
                guess = list[mid]
                if guess == item:
                    return mid
                if guess > item:
                    high = mid - 1
                else:
                    low = mid + 1
        return None
    
#my_list = [x**2 for x in range(20)]
#my_list = data["list_with_1000_items"]
#print(my_list) 
#print(binary_search(my_list, 9887)) # => 990
#print(binary_search(my_list, -1)) # => None
