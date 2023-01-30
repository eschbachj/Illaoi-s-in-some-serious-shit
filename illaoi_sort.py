def illaoiSort(arr):
        
        if len(arr) > 1:
 
            mid = len(arr)//2
            sub_array1 = arr[:(mid - 1)]
            sub_array2 = arr[(mid + 1):]
        
            illaoiSort(sub_array1)
            illaoiSort(sub_array2)
         
            i = j = k = 0
 
            while i < len(sub_array1) and j < len(sub_array2):
                if len(sub_array1[i][0]) < len(sub_array2[j][0]):
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
                
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
                
d = {
    "Stand with me my brothers and sisters" : "Jarvan IV",
    "I will end this misuse of magic": "Maokai",
    "I have seen two paths and made another between.": "Karma",
    "Hitting me is like boxing with shadows" : "Vayne",
    "Let this day be legend" : "Pantheon",
    "Fear is the first of many foes" : "Garen",
    "The secrets of magic are mine alone" : "Xerath",
    }


list_d = list(d.items())
illaoiSort(list_d)
champ_order = [None] * len(list_d)

for i in range(0, len(list_d)):
    champ_order[i] = list_d[i][1]
    
print(champ_order)
