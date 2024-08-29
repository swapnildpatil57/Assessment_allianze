list=[1,2,3,5,5,3,4]



def find_occurence(char,list):
    count=0
    for i in list:
        if char == i:
            count = count+1
    return count

print(find_occurence(5,list))


def find_occurence_word(word,string):
    string=string.split()
    count =0
    for i in string:
        if word == i:
            count=count +1
    return count

print(find_occurence_word('swapnil','swapnil patil'))



def non_duplicate(list):
    unique_list=[]
    for i in range(0,len(list)):
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(non_duplicate(list))
    

def reverse_string(s):
    reversed_str = ''
    # Iterate over the characters in the string from the last to the first
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i] # Build the reversed string character by character
    return reversed_str


list1="hello work"
s= (reverse_string(list1))
print ((s))


list =[1,33,4,5,2]
    
def sort_list(list):    
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] >= list[j]:
                list[i],list[j] =list[j],list[i]

sort_list(list)
print ("sortedlist", list)


                
            
                