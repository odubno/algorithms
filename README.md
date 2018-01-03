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

