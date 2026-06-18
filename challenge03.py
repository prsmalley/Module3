#Name:
#Module 3 - Challenge Problems (not graded — for if you finish early or want more!)
'''
These are harder than the assignment on purpose, and they lean hard on conditionals
(if / elif / else) plus everything from Modules 1 and 2. Some may need ideas we
haven't covered yet — looking things up and experimenting is part of coding. Have fun!
'''

'''
####Challenge 01: Leap Year
Ask the user for a year, then print whether it is a leap year.
The rules:
  - A year is a leap year if it is divisible by 4...
  - ...EXCEPT years divisible by 100 are NOT leap years...
  - ...UNLESS they are also divisible by 400 (those ARE leap years).
(Hint: you'll need to combine conditions with and / or, or nest your if statements.)
'''
print('Challenge 01')
#write your code below




'''
####Challenge 02: Rock, Paper, Scissors
Ask Player 1 for their choice (rock, paper, or scissors).
Ask Player 2 for their choice.
Print who wins, or whether it's a tie.
(Hint: think carefully about every combination — this is a lot of branches!)
'''
print('\nChallenge 02')
#write your code below




'''
####Challenge 03: Safe Calculator
Ask the user for two numbers and an operator (+, -, *, or /).
Use if / elif / else to do the right calculation and print the result.
Make sure your program does NOT crash if the user tries to divide by zero —
print a friendly message instead.
'''
print('\nChallenge 03')
#write your code below




'''
####Challenge 04: Break the Grader  (a puzzle about how grading works)
Open tests/test_assignment03.py and read it carefully.

This grader is sneakier than Module 2's — it runs your program several times with
DIFFERENT inputs and checks the output each time.

Your challenge: write a program that passes every check WITHOUT using a single
if / elif / else — no real decisions at all.

Think about:
  - Each time it runs, is the grader checking that the RIGHT answer appears...
    or also that the WRONG answers do NOT appear?
  - If you just printed every possible answer every time, what would happen?
  - How would you rewrite the tests so a program with no conditionals can't pass?

To try it: save a copy of your real assignment03.py first(!), then experiment in
assignment03.py and run:  python tests/test_assignment03.py
When you're done, put your real assignment03.py back.

(Nothing to hand in — this is about understanding why testing decision-making
code is genuinely hard.)
'''
print('\nChallenge 04 — see the comments above')
