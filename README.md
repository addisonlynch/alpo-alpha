# ALPO Alpha

## Important Note

Any text that looks like ``this`` must be spelled and capitalized **excatly as shown**.


## Spreadsheets

Place both of the below spreadsheets (Google Forms and results) in the same
folder as ``alpha.py``. 

### Google Forms

Download the poll results directly from Google Forms and ensure that the following columns
(spelled **exactly** as below, including capitalization) are present **in any order**.

* ``Full Name`` - *Used to sort the results workbook by first name*
* ``3 Unit Pick``
* ``2 Unit Pick``
* ``1 Unit Pick`` 

**Additional spreadsheet columns are OK** (including before, between,
and after the above list), and will be safely ignored by the program.

An example spreadsheet is shown below:

| Timestamp          | Full Name       | 3 Unit Pick                                 | 2 Unit Pick                   | 1 Unit Pick                                |
| ------------------ | --------------- | ------------------------------------------- | ----------------------------- | ------------------------------------------ |
| 6/10/2021 18:38:30 | Ian Ackerman    | Turkey ML (+488)                            | Los Angeles Dodgers ML (-300) | Wales vs Switzerland OVER 2.5 Goals (-110) |
| 6/10/2021 18:39:24 | Jordan Aghimien | Miami Marlins (+120)                        | Turkey vs. Italy DRAW (+299)  | Pirates ML (+10000000000)                  |
| 6/10/2021 18:41:22 | Zizo Mansour    | Bucks ML (-130)                             | Pirates ML (+10000000000)     | Atlanta Braves ML (-130)                   |
| 6/10/2021 18:43:09 | Addison Lynch   | Wales vs Switzerland UNDER 2.5 Goals (-110) | Turkey vs. Italy DRAW (+299)  | Los Angeles Dodgers ML (-300)              |

An example Excel workbook is located in the **examples** folder of this repository named "googleforms.xlsx".


### Results

The results spreadsheet must have two columns only, ``Pick`` and ``Result`` spelled and capitalized in such fashion.

The values for the ``Result`` column must either be:

* ``win``
* ``lose``
* ``push``

Copy and paste each of the possible picks into the ``Pick`` column,
and type each of the corresponding results from the list above into
the ``Result`` column.

**Picks should be spelled, capitalized, and formatted exactly as copied from Google Forms**

An example spreadsheet is shown below:

| Pick                                        | Result |
| ------------------------------------------- | ------ |
| Pens Ml (+110)                              | win    |
| Flyers ML (-110)                            | lose   |
| Bucks ML (-130)                             | push   |
| Nets ML (+120)                              | lose   |
| Clippers ML (+145)                          | win    |
| Jazz ML (-130)                              | push   |
| Atlanta Braves ML (-130)                    | lose   |
| Miami Marlins (+120)                        | win    |
| Houston Astros vs. Red Sox over 8 (-110)    | win    |
| Los Angeles Dodgers ML (-300)               | win    |
| Pirates ML (+10000000000)                   | lose   |
| Turkey ML (+488)                            | push   |
| Italy ML (-110)                             | push   |
| Turkey vs. Italy DRAW (+299)                | push   |
| Wales vs Switzerland OVER 2.5 Goals (-110)  | win    |
| Wales vs Switzerland UNDER 2.5 Goals (-110) | lose   |

An example Excel workbook is located in the **examples** folder of this repository named "results.xlsx".

###


## Installation

Installation requires Python >= 3.5 and the pip package manager.

To install, first install the dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

Run script using 

```bash
python alpha.py googleforms.xlsx results.xlsx
```

Where ``googleforms.xlsx`` and ``results.xlsx`` are the names of the Google
Forms and results spreadsheet, both located in the same folder as ``alpha.py``
(you can use finder to paste the files here)

### Scores

An excel workbook with a name beginning with ``scores_`` followed by the current
date and time will be generated in the same folder as ``alpha.py`` with the results.