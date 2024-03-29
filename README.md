# Automated Alarm
## alarm.py

Your alarm clock can be programmed by Python provided you can write a function to automate it.

**NOTE:**
this is an assignment for my students and not an actual project, so I do not need any pull requests for this.

## Instructions:
1. Clone your repo (git it from GitHub Classroom).
2. Open in VS Code.
3. Open the terminal and run `poetry update`.
4. Run `poetry shell`.
5. Set the Python Interpreter to the poetry virtual environment.
6. Edit `alarm.py`.
7. In alarm, define a function titled, `set_alarm()` and give it two inputs: `day` and `no_school`.
8. Code the function to meet the requirements below.
9. Run pytest by typing `pytest` or `pytest -v` in the terminal.
10. Any time you commit and push your changes, GitHub will run tests on your code.
  - `git add *`
  - `git commit -m "what I just did"`
  - `git push origin main`
11. If you pass all tests, you will score 4/4 on GitHub classroom.

**requirements:**
-----------------

You want to make sure your alarm is set for...
* ***If it's a standard school day***...
  * set it for 7:00 on Mondays, Tuesdays, Thursdays, and Fridays
  * set it for 7:30 on Wednesdays
* ***If there is no school on a weekday*** (it's summer, a holiday, or some other break),
  * then it's 9:30 on Mondays (no school)
  * or 8:30 on all other weekdays (again, no school)
* Always set the alarm for 9:00am on the weekends (regardless of the day)

**Inputs:**
----------
* **set_alarm()** receives two inputs (string and boolean): `day` and `no_school`
  * **`day`** is a string ("Monday", "Tuesday", "Wednesday"...)
  * **`no_school`** is a boolean
    * `True` = if it's a vacation, holiday, or summer
    * `False` = if it's a standard school day

**Output:**
------------
`set_alarm()` returns one output (a string): time (e.g. `"8:00"`)

**Examples:**
inputs => output/s
--------------------------------
* `"Wednesday"` `True` => `'8:30'`
* `"Monday"` `True` => `'9:30'`
* `"Monday"` `False` => `'7:00'`
* `"Wednesday"` `False` => `'7:30'`
* `"Saturday"` `True` => `'9:00'`
* `"Saturday"` `False` => `'9:00'`
* `"Friday"` `False` => `'7:00'`
* `"Friday"` `True` => `'8:30'`
