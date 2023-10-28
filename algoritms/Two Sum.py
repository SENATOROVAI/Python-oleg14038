from typing import List
class ClassSolutin:
    nums = [7, 2, 11, 15]
    target = 9 
    def twoSum(self, nums: List[int], target: int,) -> List[int]:
                               #for i указывает на перывый элемет массива 
    for i in range(len(nums)): # len - проверяем длинну массива (nums), range - переберает от 0 до 3 элемента нашего массива, i - указывает на первый элемент 
        for j in range(len(nums)): # j - указывает на первый элемент массива 
            if nums[i] + nums[j] == target and i != j:#складываем элементы массива и если они  равны = 9 и равны друг другу  
                return[i, j] #возращаем элементы 
    return[] # None 
object_of_class_list1 = ClassSolutin
object_of_class_list1.twoSum(i, j)# Хочу вывести два элемнта массива которые я складывю и получаю ответ, правильно ли делаю ?
                                  # И не могу понять почему ошбка, я так понял что это систексис ?  




