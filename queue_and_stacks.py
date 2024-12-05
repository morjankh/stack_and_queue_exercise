class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


#########Q1#############
def MaintainRolling(lst,k):
    if k>len(lst):
        return lst
    stack=[]
    for i in range(len(lst)-k,len(lst)):
        stack.append(lst[i])
    return(stack)    


#########Q2#############
def ShelfArrangement(lst):
    if len(lst)>0:
        LastIndex= lst.pop()     
        reverslst=ReversLst(lst)
        reverslst.append(LastIndex)
        lst = ReversLst(reverslst)
    return lst
def ReversLst(lst):
    new_reversed_lst=[]
    for i in range(len(lst)-1,-1,-1):
       new_reversed_lst.append(lst[i])
    return new_reversed_lst  

    # stack = []  
    # for book in lst:
    #     stack.append(book)   
    # reversed_list = []
    # while stack:
    #     reversed_list.append(stack.pop())
    
    # return reversed_list


#########Q3#############
def undo(lst,k):
    for i in range (0,k):
        if lst:
            lst.pop()
        else:
            break    
    return lst    

##############Q4##########
def parentheses(s):
   
   if not s:
       return True

   open = ["(","[","{"]
   close = [")","]","}"]
   dic = {")":"(", "]":"[", "}":"{"}
   stack=[]
   for pare in s:
       if pare in open:
           stack.append(pare)
       elif pare in close:
           if dic[pare] != stack.pop():
               return False
       else:
           continue
   return True   


#########Q5#############
def Temperature(temp):
    n = len(temp)
    result = [0] * n
    for i in range(n):
        for j in range(i+1,n):
            if temp[j]>temp[i]:
                result[i]=j-i
                break

    return result      

#########Q6#############
from collections import deque
def simualte(customer):
    queue=deque(customer)
    served_customer=[]
    while queue:
        served_customer.append(queue.popleft())
    return(served_customer)    

      
###########Q7##############

class FamilyTreeNode:
    def __init__(self,name):
        self.name= name 
        self.children = []

    def add_child(self,child):
        self.children.append(child)    


def search_family_tree_dfs(root,target_name):
    if not root:
        return False

    if root.name== target_name:
        return True

    for child in root.children:
        if search_family_tree_dfs(child,target_name):
            return True
    return False        

###########Q8##############

class directory:
    def __init__(self,value):
        self.value= int(value) 
        self.children = []

    def add_child(self,child):
        self.children.append(child)    

def sum_all_dirctory(root):
    if not root:
        return 0
    total_sum  = root.value
    for child in root.children:
        total_sum += sum_all_dirctory(child)

    return total_sum

###########Q9##############
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


from collections import deque
from collections import deque

def is_symmetric_iterative(root):
    if not root:
        return True 

    queue = deque([(root.left, root.right)])
    while queue:
        t1, t2 = queue.popleft()  
        
        if not t1 and not t2:
            continue
    
        if not t1 or not t2 or t1.value != t2.value:
            return False
    
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    return True







# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)

# print(is_symmetric_iterative(root)) 

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.right = TreeNode(3)

# print(is_symmetric_iterative(root))  



# a= directory("10")
# b= directory("20")
# c= directory("20")
# d= directory("10")
# a.add_child(b)
# a.add_child(c) 
# b.add_child(d)

# print( sum_all_dirctory(a))
# a= FamilyTreeNode("A")
# b= FamilyTreeNode("B")
# c= FamilyTreeNode("C")
# d = FamilyTreeNode("D")
# e = FamilyTreeNode("E")

# a.add_child(b)
# a.add_child(c)
# b.add_child(d)
# b.add_child(e)
# print(search_family_tree_dfs(a, "E"))  # Output: True
# print(search_family_tree_dfs(a, "Z"))  # Output: False


# arr = [73, 74, 75, 71, 69, 72, 76, 73]
# print(Temperature(arr))



       

# def Tempartury(days):
#     lst=[]
#     c=0
#     for i, v in enumerate(days):
#         for j in range(i+1,len(days)):
#             if days[j]>v:
#                 c=c+1
#                 lst.append(c)
#                 c=0
#                 break
#             else:    
#                 c=c+1
#                 lst.append(c)
#                 break
#         c=0  
#     return lst      

# arr = [73, 74, 75, 71, 69, 72, 76, 73]

