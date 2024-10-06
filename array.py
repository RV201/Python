int_array = array.array('i', [1, 2, 3, 4])
int_array.insert(0, -1)  # -1,1,2,3,4
int_array.insert(2, -2)  # -1,1,-2,2,3,4
print(int_array)