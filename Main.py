from typing import Optional


class Node:
    """
    This class is to create a node
    """

    def __init__(self, data=None, next=None):
        """
        Instance variables of Node object
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        node=Node(data)
        temp=self.head
        if temp==None:
            self.head=node
            return

        while temp.next!=None:
            temp=temp.next
        temp.next=node

    def status(self):
        """
        It prints all the elements of list.
        """
        temp=self.head
        print("[",end="")
        while temp.next!=None:
            print(temp.data,end=", ")
            temp=temp.next
        print(temp.data,end="]\n")


class Solution:
    """
    This class is for adding two linked list
    """

    @staticmethod
    def get_total_elements(linked_list):
        count=1
        temp=linked_list.head
        while temp != None:
            temp = temp.next
            count += 1
        return count

    @staticmethod
    def balance(linked_list,n,val = 0):
        for i in range(n):
            linked_list.insert_at_end(val)
        return linked_list

    def get_node(self,linked_list):
        temp=linked_list.head
        x = None
        while temp!=None:
            x = temp
            temp = temp.next
            yield x.data


    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        a = self.get_total_elements(first_list)
        b = self.get_total_elements(second_list)
        result = LinkedList()

        if a>b:
            second_list = self.balance(second_list, b)
        else:
            first_list = self.balance(first_list, a)
        temp_val = 0
        for i,j in zip(self.get_node(first_list),self.get_node(second_list)):
            # print(f"values are : {i}, {j}")
            total = i+j
            # print(f"temp val : {temp_val}")
            visited = False
            if total+temp_val>9:
                visited = True
                if temp_val>0:
                    total += temp_val
                    temp_val = 0
                    # print(f"Yeah! temp_val > 0 so now total will be : {total}")
                temp_val += total//10
                # print(f"Now temp will be : {temp_val} because i+j is : {total}")
                total = total%10
            if temp_val>0 and not visited:
                total += temp_val
                temp_val = 0
            result.insert_at_end(total)

        if temp_val>0:
            result.insert_at_end(temp_val)

        return result




# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()

