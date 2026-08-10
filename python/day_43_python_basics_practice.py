# PART 1 — The absolute basics: making Python say things
## 1.1 — `print()` — how Python talks to you

#`print()` puts something on the screen. 
# It's the first thing you'll ever run, and you'll use it forever (especially to check your work).

#print("Hello")

#**What each piece is:**
#- `print` — a command that means "show this on screen"
#- `( )` — the parentheses hold *what* to print
#- `"Hello"` — the text to show. The quotes mean "this is text."

#print("I am learning python")

## 1.2 — Text needs quotes. Numbers don't.

#TYPE THIS — both lines, then run:
#```python
#print("100")
#print(100)

#print("100")
#print(100)

#Both show `100` on screen — but they are **different things underneath**, 
# and this difference matters enormously later.
#- `"100"` with quotes = **text** (Python calls it a *string*). 
# It's the *characters* 1, 0, 0 — like a label.
#- `100` without quotes = a **number** Python can do math with.

#print(100+100)
#print("100"+"100")

#- First line → `200` (Python added the numbers)
#- Second line → `100100` (Python glued the text together, 
#                          like sticking two labels side by side)

## 1.3 — Comments: notes Python ignores

#A `#` means "Python, ignore the rest of this line." It's for notes to yourself.

# PART 2 — Boxes that hold things: variables
## 2.1 — A variable is a labeled box

#A **variable** stores a value and gives it a name, so you can use it later. 
# The `=` sign means "put the thing on the right into the box named on the left."

#rent = 5000 # rent is the box, 5000 is what you put into the box
#print(rent) #printing the box results in what you assigned to the box

#**Read `=` as "gets" or "is set to," NOT "equals."
# ** `rent = 5000` means "rent *gets* 5000." 
# (This matters — there's a different symbol for "equals," coming later.)

#tenant = "Loblaw"
#print(tenant)

#rent = 5000
#print (rent*12) #python looks up rent, takes out whats in the box and multiplies it by 12

## 2.2 — You can change what's in the box

#rent = 5000
#print(rent)
#rent = 8000
#print(rent)

#second assignment to the box replaces what was first placed into the box (takes the latest)

## 2.3 — Building on the box: `+=`

#Often you want to *add to* what's already in the box. 
# `+=` means "take what's in the box, add this, put the result back."

#total = 0
#total = total + 100 #total gets 100 (whatever total before was)
#print(total)

#the shortcut

#total = 0
#total += 100
#print(total)
#total += 50
#print(total)

#total += 100 is the shorter way to write total = total + 100

#**Remember `+=` — it's the heart of counting and summing, 
# which you'll do constantly.** We'll see why soon.

# PART 3 — Lists: holding many things

## 3.1 — A list is an ordered row of things

#A **list** holds multiple values in order. 
# You make one with square brackets `[ ]`, values separated by commas.

rents = [5000, 8000, 3000]
print(rents)

#> Think of a list as a single column in Excel, 
# or the set of rows a SQL query returns. 
# Many values, in order, held together under one name.