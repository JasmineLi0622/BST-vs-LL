# activity2 part3
#i think the user might want to change these two attributes easily and freely so i do not make them private
class ListNode:
    def __init__(self,cargo=None,next=None):
        self.cargo=cargo
        self.next=next
    
    def __str__(self):
        return(self.cargo)
#make head, size private to keep users from changing them freely
class LinkedList:
    def __init__(self,head=None,size=None):#insert a number for the head
        if head==None:
            self.__head=None
        else:
            self.__head=ListNode(head)
        if type(size)==int: #size being positive int or None
            if size>0:
                self.__size=size
            else:
                print('size need to be a positive int, set size to None')
                self.__size=None
        elif size==None:
            self.__size=size
        else:
            print('size need to be a positive int, set size to None')
            self.__size=None
    
    def get_head(self):
        return(self.__head)
    
    def get_size(self):
        return(self.__size)
    
    def set_size(self,size):
        if type(size)==int: #size being positive int or None
            n=0
            node=self.__head
            while node!=None:
                node=node.next
                n=n+1
            if size>=n and size>0:
                self.__size=size
            else:
                print('size need to be a positive int larger than current size, set size to None')
                self.__size=None
        elif size==None:
            self.__size=size
        else:
            print('size need to be a positive int larger than current size, set size to None')
            self.__size=None
        
    def is_empty(self):
        if self.__head==None:
            return(True)
        else:
            return(False)
    
    def is_full(self):
        n=0
        if self.__size!=None:
            node=self.__head
            while node!=None:
                node=node.next
                n=n+1
            if n==self.__size:
                return(True)
            elif n<self.__size:
                return(False)
        else:
            return(False)
    
    def __str__(self):#the format is : [cargo,id] - [cargo,id] - [cargo,None]
        linklist=[]
        node=self.__head
        cur_node=None
        str_list=''
        while node!=None:
            linklist.append(node)
            node=node.next
        for cur_node in linklist:
            if cur_node.next!=None:
                str_list+=('['+str(cur_node.cargo)+','+str(id(cur_node.next))+']'+' - ')
            else:
                break
        str_list+='['
        if cur_node!=None:
            str_list+=str(cur_node.cargo)+','
        str_list+='None]'
        return(str_list)
            
    
    def search_result(self,value):
        node=self.__head
        past_node=None
        find=False
        while node!=None:
            if node.cargo==value:
                find=True
                break
            else:
                past_node=node
                node=node.next
        return(find,node,past_node)#return the last searched node and its parent node
    
    def search(self,value):
        return(self.search_result(value)[0])
    
    def traverse(self):
        linklist=[]
        node=self.__head
        while node!=None:
            linklist.append(node)
            node=node.next
        return([x.cargo for x in linklist])
    
    def delete(self,value):#when delete duplicate value, delete the first one
        if not self.search(value):
            print('do not have this value in the linked list')
        else:
            parent_node=self.search_result(value)[2]
            del_node=self.search_result(value)[1]
            if parent_node!=None:
                parent_node.next=del_node.next
            else:
                self.__head=del_node.next
            print('delete successfully')
            
    def insert(self,value):#insert should not be none
        node=self.__head
        if value!=None:
            if node==None:
                self.__head=ListNode(value)
            else:
                if not self.is_full():#if have max size, check the tree is full
                    while node!=None and node.next!=None:
                        node=node.next
                    node.next=ListNode(value) 
                    #print('insert successfully')
                else:
                    print('failed,reached the max size')
        else:
            print('Do not insert None')
           
        

            
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        