from BinarySearch import BinarySearch 
import json
import unittest
import time
import random

bs=BinarySearch()

# Cargando los elementos de las listas a través de un json
with open("items.json", "r") as file:
  data = json.load(file)

# Organizando los valores para crear las listas. 
simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]

# creando una lista con más elementos 1.000.000
my_list = list(range(1000000))

# escogiendo un elemento de la lista
item = random.choice(my_list)

# definiendo el indice del elemento 
expected_index = my_list.index(item)

class TestBinarySearch(unittest.TestCase):
    def test_busqueda_binaria_comparacion(self):
        item, expected_index 
        print(item)
        print(expected_index)

        # Tiempo de búsqueda para búsqueda binaria. Notación O(log(n))
        start_time = time.time()
        binary_search_index = bs.binary_search(my_list,item) # => None
        bs_time = time.time() - start_time
    
        # my_list.index(item) devuelve el indice donde por primera vez aparece el elemento de la búsqueda, 
        # esta búsqueda se realiza de forma lineal con una notación O(n)
        start_time = time.time()
        linear_search_index = my_list.index(item)
        ls_time = time.time() - start_time

        print("Binary Search Time:", bs_time)
        print("Linear Search Time:", ls_time)

        self.assertEqual(expected_index, binary_search_index)
        self.assertEqual(expected_index, linear_search_index)
        self.assertTrue(bs_time < ls_time)

        print("Tiempo requerido para buscar un elemento random")
        print("--- Linear Search %f seconds ---" % (ls_time))
        print("--- Binary Search %f seconds ---" % (bs_time))
        #return (bs_time, ls_time) 
    
  
if __name__ == '__main__':
    unittest.main()
    