# Дана строка в виде случайной последовательности чисел от 0 до 9. 
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности. 
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. 


str = "1 5 9 7 8 3 4 5 3"

list1 = str.split(" ")

def count_it(sequence):
    c = []
    for i in range (0, len(sequence)):
        count = 0
        for j in range (0, len(sequence)):
            if sequence[i] == sequence[j]:
                count +=1
        c.append(count)
    d = {sequence[i]: c[i] for i in range (0, len(sequence))}
    return d

print(count_it(list1))