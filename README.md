# Homework 1: Data Processing and Performance

This homework has three parts.
The first part reviews some of the basics of data processing
in the context of Pandas
(input, cleaning, validation, and manipulation of DataFrames).
The second part is about performance measuring & comparison, and
will explore several design choices which can affect performance.
Finally, the third part is your "project proposal".

For part 3: like the rest of the homeworks in this class, homework 1 comes with a project component.
This task will ask you to choose a basic domain and dataset for your project,
including manually collecting a small sample dataset of 10 data points.

## Getting Started

This homework will be submitted through GitHub Classroom.
You can find the instructions to join the classroom and accept the assignment on Piazza.
Clone your repository,
then open up and complete `part1.py`, `part2.py`, and `part3.py`.

If you get stuck, you can take a look at `hints.md` or consult Piazza.

## Grading Notes

In order to receive credit for your work, please follow the following guidelines.

- Make sure that you `git commit` and `git push` your latest code to your personal repository. This is how you will "submit" your code. Go to `github.com/<your repository link>` online to see if the changes are there; if you see the latest, most up-to-date version, then you are good to go.

- Make sure that `python3 part1.py`, `python3 part2.py`, and `python3 part3.py` run successfully with no errors, and the same for
`pytest part1.py`, `pytest part2.py`, and `pytest part3.py`.
We cannot give credit to code that doesn't run.

- Each part should produce, when run, a corresponding answers file `part<n>-answers.txt`, i.e. `part1-answers.txt`, `part2-answers.txt`, and `part3-answers.txt`,
and corresponding plots in `plots`.
Please commit these output files along with your project and ensure that they
are regenerated when the code is run.

- Don't rename any functions or methods or change the function signatures
  unless asked to do so.

- As discussed in the syllabus, a small number of points on each homework (at most 10% of the grade) are reserved for style points. Here are some thoughts to consider: are your variable names chosen appropriately? Have you added comments with `#` or docstrings with `"""` where appropriate? Have you removed any obsolete, unused code blocks, functions, or variables?

## Credits

Many thanks to Hassnain (the TA)
and the data science course at LUMS (CS 334 taught by Dr. Mobin Javed)
for the data and some of the exercises that were used in Part 1 of this homework assignment.
