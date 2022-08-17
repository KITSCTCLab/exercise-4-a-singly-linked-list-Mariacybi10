# Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.</br>

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example 1

![alt text](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg "First LinkedList")

```
Input: 
first_list = [2,4,3]
second_list = [5,6,4]

Output: 
[7,0,8]
Explanation: 342 + 465 = 807.
```
## Example 2
```
Input: 
first_list = [0]
second_list = [0]

Output: 
[0]
```
## Example 3
```
Input: 
first_list = [9,9,9,9,9,9,9]
second_list = [9,9,9,9]

Output: 
[8,9,9,9,0,0,0,1]
```
# Constraints
```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```
