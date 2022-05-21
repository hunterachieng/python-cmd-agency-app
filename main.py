import csv
data = []
with open('real-estate-sample.csv', 'r') as file:
    reader = csv.reader(file)
    data.extend(list(reader))
    # print(data)
    def merge(left, right):
        if len(left) <=0 or len(right) <=0:
            return left or right
        
        sorted_data = []
        i = j=0
        while len(sorted_data) < len(left) + len(right):
            if left[i][1] < right[j][1]:
                sorted_data.append(left[i])
                i+=1
            else:
                sorted_data.append(right[j])
                j+=1
            if i == len(left) or j == len(right):
                sorted_data.extend(left[i:] or right[j])
                break
        return sorted_data


    def estateSort(data):
        if len(data) < 2:
            return data 
        middle = len(data)//2
        print(middle)
        left =  estateSort(data[1:middle])
        right = estateSort(data[middle:])
        # print(left)

        return merge(left,right)
    print(estateSort(data))



   
