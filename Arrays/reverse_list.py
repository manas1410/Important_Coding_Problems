#Reverse a list 

def reverse_list(lis,start,end):
    while (start<end):
        lis[start],lis[end] = lis[end],lis[start]
        start,end = start+1, end-1
    print(lis)
        
input_list = input().split()
reverse_list(input_list,0,len(input_list)-1)
