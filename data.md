
# Integers and Floats
You have already been exposed to integers (numbers) through the previous exercises. Integers represent whole numbers in Python. Floats represent numbers with decimal values. Pop the following into python and check the output and how they are different. Note: It's important to understand the basics of these datatypes now as they have properties exclusive to their data type. 
```python
x = 3
y = float(3)
print(x,y)
```
## Tip Calculator 
You will be creating a tip calculator that must accomplish all of the following

- Create variables representing at the bill, tip and total amount
paid
- Receive user input and assign that user input to the variables in
step 1 (excluding total)
- Change the data type of bill from String to Float
- Change the data type of tip to Integer (int)
- Calculate the total that needs to be paid
- Print the f string after the user has input data
# Lists
These ints and floats can be stored in lists to let you manage complexitymore easily. Try the following code and check the output. 
```python
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
```
You may noticed the following

1.  We can store different data types inside a list, they do not need to be the same.
2.  if we print the variable "values" we can see the entire list
3.  If we use a for loop we can easily iterate through the list and access the values.

## What if we just want one single, specific value?
We can access individual elements in the list by using brackets ([]) and the elements position. Note that in CS we tend to begin counting at 0. 
```python
print(values[0])
print(values[6])
```
By printing the values at position 0 and 6 we can access the first and last elements. Try accessing element 7 and see what happens. Would you have been able to debug this?

# Strings
Strings are a list of characters that represent text. It's important to  understand that a String is not simply "just text", it is instead a list of characters. For example, "test" is really a list with each letter stored as an element in a list.
```
"test"
["t","e","s","t"]
```
## Why does this matter?
Think to yourself, how does knowing that each character in a String is really an element in a list? What does that allow us to do? Why do computers want Strings represented this way?

## String Methods
[Python String Methods](https://docs.python.org/3.11/library/string.html) is a link that will take you the Python documentation site (Great Resource!). Here we can see there a number of functions built into Python for working with Strings. Some of which are made possible because of how the computer stores and interprets Strings. 

Let's put some of these into practice.
```python
x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
```
Here we can use the split function which allows for an parameter to be passed in. The parameter passed in will be used to split the string into a new list. By using an empty space we can break up our words into seperate elements. Since we know how to access elements in a list we can then store the first word as a seperate variable to be used later.

# Challenge
1. Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments. Then craft the function. 
2. Mad Libs Project

# Booleans and Control Flow
InPython we can evaluate statements to True or False.These are referred to as boolean data types. Something can evaulate to either True OR false, never both. We can use conditional statements, if, elif (else if) and  else to create a control flow in our applications. 

```python
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
```
Here, the user will either input Friday or not. It is either Friday or it is not. If the day of the week is Friday then we will print "correct". In all other situations we will print "incorrect"
## F Strings
Variables can be used inside Strings by adding an F before the String and using {} templates inside the String. See below
``` Python
x = "test"
print(f"hello {x}")
```
```python

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
```
What will happen when we run the above code? 

## Challenge
Let's create a function that determines if a number is odd or even
## Challenge
Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 

## Challenge

Create a function that accepts an input and determines all factors of the number. 

## Challenge 

Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. # Python Lesson: `while` Loops

## What is a `while` loop?

A `while` loop repeats a block of code **as long as a condition is true**. It's useful when you don't know in advance exactly how many times you need to repeat something — you just know the *condition* under which you should keep going (or stop).

```python
while condition:
    # do something
```

Python checks the condition before every pass through the loop. As soon as it's `False`, the loop stops and the program moves on.

---

## Example 1: Counting down with `while True` and `break`

```python
x = 500
y = 0

while True:
    if x > 0:
        x = x - 100
        print(x)
    else:
        break
```

### How it works

- `while True:` creates a loop that would normally run **forever**, since `True` is always true.
- Inside the loop, we check `if x > 0:`. If it is, we subtract 100 from `x` and print it.
- If `x` is *not* greater than 0 (i.e., it's reached 0 or below), we hit `break`, which immediately exits the loop.

### Tracing through it

| Pass | `x` before | Is `x > 0`? | Action | `x` after | Printed |
|------|-----------|-------------|--------|-----------|---------|
| 1 | 500 | Yes | subtract 100 | 400 | `400` |
| 2 | 400 | Yes | subtract 100 | 300 | `300` |
| 3 | 300 | Yes | subtract 100 | 200 | `200` |
| 4 | 200 | Yes | subtract 100 | 100 | `100` |
| 5 | 100 | Yes | subtract 100 | 0 | `0` |
| 6 | 0 | No | `break` | — | (loop ends) |

**Output:**
```
400
300
200
100
0
```

### Key idea: the "infinite loop + break" pattern

Notice this loop uses `while True`, which never becomes false on its own. Instead, we control when it stops using `break` inside an `if` statement. This is a very common pattern in Python — it gives you full control over *exactly* when and why the loop exits, rather than relying on the `while` condition itself.

> **Note:** The variable `y = 0` is created at the top but never used in the loop. It doesn't affect the program — but it's a good reminder that unused variables can be a sign of leftover or incomplete code!

### Equivalent version without `while True`

You could also write this same logic using the condition directly:

```python
x = 500

while x > 0:
    x = x - 100
    print(x)
```

Both versions produce the same output. The `while True` + `break` version is useful when the stopping logic is more complex than a simple condition (see Example 2).

---

## Example 2: Getting input from the user until they type "exit"

```python
while True:
    z = input("multiply?")
    if z == "exit":
        break
```

### How it works

- Again, `while True:` starts a loop with no built-in stopping point.
- `z = input("multiply?")` pauses the program, shows the prompt `multiply?`, and waits for the user to type something.
- If what the user typed is exactly `"exit"`, the loop `break`s and ends.
- Otherwise, the loop repeats and asks again.

### Why use `while True` here?

This is a great example of when `while True` is genuinely necessary: we don't know **how many times** the user will need to respond before they type "exit". It could be once, or it could be a hundred times. Using `while True` with a `break` lets the loop keep running *indefinitely* until the user gives us a specific signal to stop.

### Try it yourself

This loop currently reads input but doesn't do anything with it besides checking for `"exit"`. As an exercise, try modifying it to actually multiply numbers:

```python
while True:
    z = input("Enter a number to multiply by 2 (or 'exit' to quit): ")
    if z == "exit":
        break
    number = float(z)
    print(number * 2)
```


# Python Lesson: Dictionaries

## What is a dictionary?

A **dictionary** (`dict`) is a way to store data as **key–value pairs**. Instead of accessing items by position (like a list, using `0`, `1`, `2`...), you access them by a **name** you choose — the "key."

Think of it like a real dictionary: you look up a *word* (the key) to find its *definition* (the value). Or think of a product label: you look up `"price"` to find `699.99`.

```python
{
    "key1": value1,
    "key2": value2,
}
```

Dictionaries use **curly braces** `{ }`, and each key is connected to its value with a colon `:`. Pairs are separated by commas.

---

## Part 1: A single dictionary

Let's start with one item — a vacuum for sale:

```python
vac = {
    "name": "Dyson V15 Cordless Vacuum",
    "price": 699.99,
    "department": "Appliances",
    "description": "High-powered cordless vacuum with laser dust detection."
}
```

Here, `vac` is a dictionary with **four keys**: `"name"`, `"price"`, `"department"`, and `"description"`. Each key points to a value — some are strings, one is a number (a `float`).

### Accessing values

To get a value out of a dictionary, use square brackets with the key name (as a string):

```python
print(vac["name"])
print(vac["price"])
```

**Output:**
```
Dyson V15 Cordless Vacuum
699.99
```

You can also combine multiple lookups in one `print()` call:

```python
print(vac["name"], vac["price"])
```

**Output:**
```
Dyson V15 Cordless Vacuum 699.99
```

### Important: keys vs. values

- The **key** (`"name"`, `"price"`, etc.) is always a fixed label you use to look something up.
- The **value** (`"Dyson V15 Cordless Vacuum"`, `699.99`, etc.) is the actual data.
- If you try to access a key that doesn't exist — like `vac["color"]` — Python will raise a `KeyError`, because that key was never defined.

### Try it yourself

```python
print(vac["department"])
print(vac["description"])
```

What do you think each line will print? Run it and check.

### Changing a value

Dictionaries are **mutable**, meaning you can change their values after creating them:

```python
vac["price"] = 649.99
print(vac["price"])
```

**Output:**
```
649.99
```

---

## Part 2: A list of dictionaries

One dictionary can represent one item. But what if you have a whole *store* full of items? You can put many dictionaries into a **list**, giving you a list of dictionaries:

```python
best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Sony Noise Cancelling Headphones",
        "price": 299.99,
        "department": "Audio",
        "description": "Wireless over-ear headphones with industry-leading noise cancellation."
    },
    {
        "name": "Apple iPhone 15",
        "price": 999.99,
        "department": "Mobile Phones",
        "description": "Latest Apple smartphone with A17 chip and advanced camera system."
    }
]
```

Now `best_buy_items` is a **list**, and each *element* of that list is a **dictionary**. This is a very common pattern in real-world programming — think of it like a spreadsheet, where each row is one dictionary and the whole spreadsheet is the list.

### Accessing one item in the list

Since it's a list, you can use a normal index to grab one dictionary:

```python
print(best_buy_items[0])
```

**Output:**
```
{'name': 'Samsung 55" 4K UHD TV', 'price': 429.99, 'department': 'Televisions', 'description': '55-inch Ultra HD Smart TV with HDR and built-in streaming apps.'}
```

That prints the *whole dictionary*. To get just one value from it, you combine list indexing **and** dictionary key access:

```python
print(best_buy_items[0]["name"])
print(best_buy_items[0]["price"])
```

**Output:**
```
Samsung 55" 4K UHD TV
429.99
```

Read this left to right: "Get item `0` from the list, then get the `"name"` key from that dictionary."

---

## Part 3: Displaying all items with `enumerate`

Printing one item at a time by typing out `best_buy_items[0]`, `best_buy_items[1]`, etc. doesn't scale. Instead, we can loop through the whole list — and use `enumerate()` to keep track of each item's index as we go.

### What does `enumerate` do?

Normally, a `for` loop over a list just gives you each item:

```python
for item in best_buy_items:
    print(item["name"])
```

But if we also want to know the **position** of each item (so a user can type a number to choose one), we wrap the list in `enumerate()`:

```python
for index, item in enumerate(best_buy_items):
    print(index, item["name"])
```

`enumerate()` hands back two things each time through the loop: the **index** (starting at 0) and the **item** itself. That's why we write `index, item` instead of just `item`.

### Putting it in a function

```python
def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

show_items(best_buy_items)
```

**Output:**
```
0 : Samsung 55" 4K UHD TV
1 : Sony Noise Cancelling Headphones
2 : Apple iPhone 15
```

Now a user browsing this list can see a numbered menu of every item.

---

## Part 4: Letting the user choose an item

Now let's combine everything: show the numbered list, ask the user to type a number, and look up the item they picked.

```python
def choose_item():
    show_items(best_buy_items)
    x = int(input("Which item number do you want to buy? "))
    print(best_buy_items[x])

choose_item()
```

### How it works, step by step

1. `show_items(best_buy_items)` prints the numbered menu.
2. `input("Which item number do you want to buy? ")` pauses and waits for the user to type something. `input()` always returns a **string**, even if the user types a number.
3. `int(...)` converts that string into an actual integer, so we can use it as a list index.
4. `best_buy_items[x]` uses that number to look up the matching dictionary in the list, and we print the whole thing.

### A word of caution

What happens if the user types `99` (a number with no matching item), or types `"television"` instead of a number? Try it and see what error you get. This is a great example of why real programs need to **validate input** — we'll cover that (`try`/`except`) in a later lesson.

---

## Summary

| Concept | Example | What it does |
|---|---|---|
| Create a dict | `vac = {"name": "Dyson", "price": 699.99}` | Stores key–value pairs |
| Access a value | `vac["name"]` | Looks up the value for a given key |
| Change a value | `vac["price"] = 649.99` | Updates the value for a key |
| List of dicts | `best_buy_items = [ {...}, {...} ]` | Stores many dicts together |
| Access nested | `best_buy_items[0]["name"]` | Index into the list, then key into the dict |
| `enumerate()` | `for i, item in enumerate(items):` | Loops with both index and item |
