# EdabileCode

list3: 
When implementing list3.py, I tried to use the power of and keyword. When I was trying to put an if condition to avoid out-of-bound error, I used the power of the "and" operator.
The general syntax of an if-statement along with logical and, or is as follows: if condition1 and condition2 / if condition1 or condition2
We know that as soon as condition1 is false, the second condition2 is not evaluated for "and" operation. 
This is why I put condition 1 as index<len(l)-1 and condition2 as value>l[index+1]
If value>l[index+1] is placed as first condition , it will get evaluated and we will get out-of-bound error. 
If index<len(l)-1 is placed as first condition, the statement value>l[index+1] will never get evaluated. 
This is a very interesting concept that I have learned in the past and thought to mention it so it would be a review for anyone seeing this. 