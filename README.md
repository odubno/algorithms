# Algorithms
Documenting Popular Algorithms

## Big O Notation
An algorithm is simply a procedure or formula for solving a problem.
Big O Notation determines the efficiency of each algorithm.

Big O Notation describes how quickly runtime will grow relative to the input as the input get aribtrarily large.


| Big-O   | Name        |
| :-----: |:-----------:|
| 1       | Constant    |
| log(n)  | Logarithmic |
| n       | Linear      |
| nlog(n) | Log Linear  |
| n^2     | Quadratic   |
| n^3     | Cubic       |
| 2^n     | Exponential |

```python
def func_constant(lst):
    """
    O(1) Constant
    """
    print lst[0]

def func_linear(lst):
    """
    O(n) Linear
    """
    for val in lst:
        print val

def func_quadratic(lst):
    """
    O(n^2) Quadratic
    """
    for item_1 in lst:
        for item_2 in lst:
            print item_1, item_2
            
lst = [1, 2, 3]
func_constant(lst)
func_linear(lst)
func_quadratic(lst)
```
[Big O Cheat Sheet](http://bigocheatsheet.com/)

## Linked Lists

### Singly Linked List
- a collection of nodes that collectively form a linear sequence.
- each node stores a reference to an object that is an element of the sequence, as well as reference to the next node of the list.
- Going from one node to the next is known as traversing the linked.
- each node is represented as a unique object.

#### Insert element as the head:
- create a new node
- set its element to the new element
- set its next link to the refer to the current head
- then set the list's head to point to the new node.

### Doubly Linked List
- explicit reference to the node before and after
- allow a great variety of time update operations, including insertions and deletions
- header and trailer for each node. eg guards.

## Recursion
Two main instances of recursion:
- Function makes one or more calls to itself.
- Data structure uses smaller instances of the exact same type of data structure.




