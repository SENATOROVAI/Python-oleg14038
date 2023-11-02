from typing import List


#class ClassSolutin:(Parametr)
#class ClassSolutin:# объявляем  класс 
#    nums = [7, 2, 11, 15]
#    target = 9
#    def twoSum(self, nums: List[int], target: int,) -> List[int]:
#        for i in range(len(nums)): #Первый for проходиться по всем элемнентам, len - проверяем длинну массива (nums), range - переберает от 0 до 3 элемента нашего массива, i - указывает на первый элементам
#            for j in range(len(nums)): #После 1 прохождения for, for проходить еще раз,  j - указывает на первый элемент массива 
#                if nums[i] + nums[j] == target and i != j: #складываем элементы массива, если они в сумму доют 9 и элементы массива не равны 
 #                   return[i,j] #возращаем элементы 
#        return[] # None 
#c = ClassSolutin() # экземпляр класса Child 
#c.twoSum() #метод переопределен классом наследнико


# Хочу вывести два элемнта массива которые я складывю и получаю ответ, правильно ли делаю ?
                                  # И не могу понять почему ошбка, я так понял что это систексис ? 


class ClassSolutin:# объявляем  класс
    def twoSum(self, nums: List[int], target: int,) -> List[int]: 
         hashmap = {}# 2 : 0 
                     # 6 : 1
                     # 5 : 2 
                     # 8 : 3 
                     #11 : 4   
         for i in range(len(nums)):
             hashmap[[i]] = i 
        print(hashmap)
        for i in range(len(nums)):
            complent = target - nums[i]#Пример: получаем 12 
            if complent in hashmap and i != hashmap(complent):#Проверяем есть ли 12 в нашешем hashamp b и пытаемся вернуть одно и тоже число  
                return[i, hashmap[complent]]
            hashmap[nums[i]] = i 


