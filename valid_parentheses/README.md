## Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

## Example 1:

```
Example 1:

Input: s = "()"

Output: true
```

## Example 2:

```
Example 2:

Input: s = "()[]{}"

Output: true
```

## Example 3:

```
Input: s = "(]"

Output: false
```


## Example 4:

```
Input: s = "([])"

Output: true
```

## Example 5:

```
Input: s = "([)]"

Output: false
```

## Explanation:

```
An expression is balanced if each opening bracket has a corresponding closing bracket 
of the same type, the pairs are properly ordered and no bracket closes before its matching 
opening bracket.

Balanced: "[()()]{}" → every opening bracket is closed in the correct order.
Not balanced: "([{]})" → the ']' closes before the matching '{' is closed, breaking 
the nesting rule.

Input: s = "[{()}]"
Output: true
Explanation:  All the brackets are well-formed.

Input:  s = "([{]})"
Output: false
Explanation: The expression is not balanced because there is a closing ']' before the closing '}'.
```