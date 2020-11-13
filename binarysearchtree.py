# -*- coding: utf-8 -*-
#Activity 2
#i think the user want to access or change the attributes of TreeNode freely and easily so i do not make them private
#but due to the strict constraint of BST, so i set root and max_node private to make sure the user cannot change it freely
class TreeNode:
    def __init__(self,cargo,lchild=None,rchild=None):
            self.lchild=lchild
            self.rchild=rchild
            self.cargo=cargo
        
    def print_value(self):
        print('the value is:',self.cargo)
        return self.cargo
    

class BinarySearchTree:#the input should all be numbers
    def __init__(self,root=None,max_node=None):#insert a number for root
        if root==None:
            self.__root=None
        else:
            self.__root=TreeNode(root) #make a root with no lchild and rchild
        if type(max_node)==int:
            if max_node>0:
                self.__max_node=max_node
            else:
                print('max_node should be positive int，set max_node as None')
                self.__max_node=None
        elif max_node==None:
            self.__max_node=max_node
        else:
            print('max_node should be positive int，set max_node as None')
            self.__max_node=None
    
    def get_root(self):
        return(self.__root)
    
    def get_max_node(self):
        return(self.__max_node)

        
    def is_empty(self):
        if self.__root==None:
            print('the tree is empty')
            return(True)
        else:
            print('the tree is not empty')

    def depth_tree(self,node):#count the depth of the tree
        if node==None:
            depth=0
            return(depth)
        else:
            ldepth=self.depth_tree(node.lchild)
            rdepth=self.depth_tree(node.rchild)
            depth=max(ldepth,rdepth)+1
            return(depth)
    
    def count_node(self,node):#count the number of nodes of the tree
        if node==None:
            node_no=0
            return(node_no)
        else:
            lnode_no=self.count_node(node.lchild)
            rnode_no=self.count_node(node.rchild)
            node_no=lnode_no+rnode_no+1
            return(node_no)
    
    def is_full(self):#when the node number equals 2^depth-1, the tree is full tree
        root=self.__root
        if root == None:
            print('the tree is not full tree')
            full=False
        else:
            node_no=self.count_node(root)
            depth=self.depth_tree(root)
            full= (node_no==pow(2,depth)-1)#check if the node number equals 2^depth-1
            if full:
                print('the tree is full tree')
            else:
                print('the tree is not full tree')
        return(full)

    def is_full2(self):#check the number of the node meet the limited size
    #this one is the one you required
                      
        if self.__max_node==None:
            print('the tree has no limited size, it is not full')
            full=False
        else:
            node_no=self.count_node(self.__root)
            if node_no==self.__max_node:
                print('the tree is full')
                full=True
            else:
                print('the tree is not full')
                full=False
        return(full)
    
    def set_max_node(self,max_node):
        if type(max_node)==int:
            if max_node>=self.count_node(self.__root) and max_node>0:
                self.__max_node=max_node
            else:
                print('max_node should be a positive int larger than current node number，set max_node as None')
                self.__max_node=None
        elif max_node==None:
            self.__max_node=max_node
        else:
            print('max_node should be a positive int larger than current node number，set max_node as None')
            self.__max_node=None
        
        
    def search_value(self,value):
        cur_node=self.__root
        past_node=None
        child=None
        while cur_node!=None:
            if cur_node.cargo!=value:
                try:#check whether comparable
                    if cur_node.cargo>value:
                        past_node=cur_node
                        cur_node=cur_node.lchild
                        child='left'
                    else:
                        past_node=cur_node
                        cur_node=cur_node.rchild
                        child='right'
                except:
                    return([False,cur_node])
            else:
                break
        if cur_node!=None:
            if cur_node.cargo==value:
                return([True,cur_node,past_node,child])
                #return the last not None node that searched and whether find the value 
                #if find return parent node and their relationship
            else:
                return([False,cur_node])
        else:
            return([False,past_node])
        
    def search(self,value):
        return(self.search_value(value)[0])
        
    def insert(self,value):
        if self.search(value): #if value is in the tree, do not insert
            print('the value is already in the tree, change the value')
        else:
            if self.__max_node==None or self.__max_node>=self.count_node(self.__root)+1 : #check if the node number equals max_node
                if value!=None:#the value should not be none
                    if self.__root==None:
                        self.__root=TreeNode(value)
                        #print('insert successfully')
                    else:
                        cur_node=self.search_value(value)[1] #get the last searched not none node
                        try:#keep data comparable
                            if value<cur_node.cargo:
                                cur_node.lchild=TreeNode(value)
                                #print('insert successfully')
                            elif value>cur_node.cargo:
                                cur_node.rchild=TreeNode(value)
                                #print('insert successfully')
                            else:
                                print('already have this value in the tree')
                        except:
                            print('please change the data type')
                else:
                    print('please do not insert None')
            else:
                print('failed,the current tree already reaches the max_size')

    
    def get_nodes(self,node): #prorder
        if node==None:
            return([])
        else:
            lnodes=self.get_nodes(node.lchild)
            rnodes=self.get_nodes(node.rchild)
            return(lnodes+rnodes+[node])
    
    def traverse(self):
        node_list=[x.cargo for x in self.get_nodes(self.__root)]
        node_list.sort()
        return(node_list)
            
        

    def print_tree(self):
        #if the depth of the tree is large, the result will of one line will be printed on several lines 
        #which seems wrong, but as long as your screen is big enough, the result is true!!
        #so please use BST with small depth to test this method
        #also please use anaconda to run this method, because here i used matrix in numpy
        depth=self.depth_tree(self.__root) #the last level of the tree should at most have 2^(k-1) nodes
        cur_node_list=[self.__root]
        cur_depth=0
        cur_coordinate_list=[pow(2,depth-1)-1]
        len_max=0
        import numpy as np
        matrix=np.full([depth,pow(2,depth)-1],None)
        while cur_depth<depth:
            i=0
            next_node_list=[]
            next_coordinate_list=[]
            while cur_node_list!=[]:
                cur_node=cur_node_list.pop(0)
                if cur_node!=None:
                    matrix[cur_depth,cur_coordinate_list[i]]=cur_node.cargo
                    if cur_node.lchild!=None:
                        next_node_list.append(cur_node.lchild)
                        next_coordinate_list.append(cur_coordinate_list[i]-pow(2,depth-cur_depth-2))
                    else:
                        next_node_list.append(None)
                        next_coordinate_list.append(cur_coordinate_list[i]-pow(2,depth-cur_depth-2))
                    if cur_node.rchild!=None:
                        next_node_list.append(cur_node.rchild)
                        next_coordinate_list.append(cur_coordinate_list[i]+pow(2,depth-cur_depth-2))
                    else:
                        next_node_list.append(None)
                        next_coordinate_list.append(cur_coordinate_list[i]+pow(2,depth-cur_depth-2))
                    if len_max<len(str(cur_node.cargo)):
                        len_max=len(str(cur_node.cargo))
                else:
                    next_node_list.append(None) 
                    next_coordinate_list.append(cur_coordinate_list[i]-pow(2,depth-cur_depth-2))
                    next_node_list.append(None) 
                    next_coordinate_list.append(cur_coordinate_list[i]+pow(2,depth-cur_depth-2))

                i+=1
            cur_depth+=1
            cur_node_list=next_node_list
            cur_coordinate_list=next_coordinate_list
          
        for i in list(range(depth)):
            for j in list(range(pow(2,depth)-1)):
                if matrix[i,j]!=None:
                    print("{cargo: ^{length}}".format(cargo=matrix[i,j],length=len_max),end='') #make the nodes have the same length
                else:
                    print("{cargo: ^{length}}".format(cargo='',length=len_max),end='')
            print('')
        
    def Inorder_get_nodes(self,node):
        if node==None:
           return([])
        else:
            lnodes=self.Inorder_get_nodes(node.lchild)
            rnodes=self.Inorder_get_nodes(node.rchild)
            return(lnodes+[node]+rnodes)

        
    def delete(self,value):
        if self.search(value)==False:#check if the value is in the BST
            return('{} is not in this BST'.format(value))
        else:
            del_node=self.search_value(value)[1]
            del_node_parent=self.search_value(value)[2]
            del_node_type=self.search_value(value)[3]
            if del_node.lchild==None and del_node.rchild==None:#if it has no left child and right child, set this node to none
                if del_node_parent==None:#check is this is the root
                    self.__root=None
                elif del_node_type=='left':
                    del_node_parent.lchild=None
                else:
                    del_node_parent.rchild=None
            elif del_node.lchild==None:#if it only have right child, replace it with right child
                if del_node_parent==None:
                    self.__root=del_node.rchild
                elif del_node_type=='left':
                    del_node_parent.lchild=del_node.rchild
                else:
                    del_node_parent.rchild=del_node.rchild
            elif del_node.rchild==None:#if it only have left child, replace it with left child
                if del_node_parent==None:
                    self.__root=del_node.lchild
                elif del_node_type=='left':
                    del_node_parent.lchild=del_node.lchild
                else:
                    del_node_parent.rchild=del_node.lchild
            else: #if it has both right child and left child
                ldepth=self.depth_tree(del_node.lchild)
                rdepth=self.depth_tree(del_node.rchild)
                if ldepth<=rdepth:#if the left tree is not deeper than right, then use the right tree,so that the tree can keep relative balance
                    replace_node=self.Inorder_get_nodes(del_node.rchild)[0]#get the min in the right tree
                    del_node2_parent=self.search_value(replace_node.cargo)[2]
                    del_node2_type=self.search_value(replace_node.cargo)[3]
                    del_node.cargo=replace_node.cargo
                    if del_node!=del_node2_parent:
                        if replace_node.rchild!=None:
                            del_node2_parent.lchild=replace_node.rchild
                        else:
                            del_node2_parent.lchild=None    
                    else:
                        if replace_node.rchild!=None:
                            del_node2_parent.rchild=replace_node.rchild
                        else:
                            del_node2_parent.rchild=None
                        
                else:
                    replace_node=self.Inorder_get_nodes(del_node.lchild)[-1]#get the max in the left tree
                    del_node2_parent=self.search_value(replace_node.cargo)[2]
                    del_node2_type=self.search_value(replace_node.cargo)[3]
                    del_node.cargo=replace_node.cargo
                    if del_node!=del_node2_parent:
                        if replace_node.lchild!=None:
                            del_node2_parent.rchild=replace_node.lchild
                        else:
                            del_node2_parent.rchild=None
                    else:
                        if replace_node.lchild!=None:
                            del_node2_parent.lchild=replace_node.lchild
                        else:
                            del_node2_parent.lchild=None
            print('Delete successfully')
     
                
#bibligraphy:
#is_full:https://blog.csdn.net/stpeace/article/details/8148776?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-1-8148776.nonecase&utm_term=%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E6%98%AF%E6%BB%A1%E4%BA%8C%E5%8F%89%E6%A0%91&spm=1000.2123.3001.4430               
            
            
    

     
            
