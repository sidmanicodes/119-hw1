"""
Part 1: Data Processing in Pandas

This part will explore a dataset of world university rankings
called the "QS University Rankings".

The ranking data was taken 2019--2021 from the following website:
https://www.topuniversities.com/university-rankings/world-university-rankings/2021

First, let's load the libraries we will need.
"""

import pandas as pd
import pytest
import matplotlib.pyplot as plt

"""
1. Load the data into Pandas

Our first step is to load the data into a Pandas DataFrame.

In doing so, we will also change the column names
to lowercase and reorder to get only the columns we are interested in.
Fill in the parts marked TODO below.

When you are done, remove the `@pytest.mark.skip` for the following test.
You can run it with `pytest part1.py`.
It should pass.
"""

NEW_COLUMNS = ['rank', 'university', 'region', 'academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']

def q1():
    # Load the input files and return them as a list of 3 dataframes.
    df_2019 = pd.read_csv('data/2019.csv', encoding='latin-1')
    df_2020 = pd.read_csv('data/2020.csv', encoding='latin-1')
    df_2021 = pd.read_csv('data/2021.csv', encoding='latin-1')

    # Standardizing the column names
    df_2019.columns = df_2019.columns.str.lower()
    df_2020.columns = df_2019.columns.str.lower()
    df_2021.columns = df_2019.columns.str.lower()

    # Restructuring the column indexes
    # TODO:
    # Fill out this part. You can use column access to get only the
    # columns we are interested in using the NEW_COLUMNS variable above.
    raise NotImplementedError

    return [df_2019, df_2020, df_2021]

@pytest.mark.skip
def test_q1():
    assert len(q1()) == 3

"""
2. Input validation

Let's do some basic sanity checks on the data for Q1.

First, fill in the following unit test.
It should check that all three data frames have the same shape,
and the correct number of rows and columns in the correct order.

When the unit test is implemented, remove the part
`@pytest.mark.skip` and then run `pytest part1.py` to run
your code. Did it work?
"""

@pytest.mark.skip
def test_q2():
    # Check:
    # - that all three dataframes have the same shape
    # - the number of rows
    # - the number of columns
    # - the columns are listed in the correct order
    raise NotImplementedError

"""
3. Input validation, continued

Now write a unit test for another property: that the set of university names
in each year is the same.
Remove the part `@pytest.mark.skip` and then run `pytest part1.py` to run
your code. Did it work?
"""

@pytest.mark.skip
def test_q2():
    # Check:
    # - that the set of university names in each year is the same
    raise NotImplementedError

"""
Did the test pass or fail? Comment below and explain why.

=== ANSWER Q3 BELOW ===

=== END OF Q3 ANSWER ===

Important:
If it failed, add @pytest.mark.xfail to the test_q3() function.
"""

"""
4. Random sampling

Now that we have the input data validated, let's get a feel for
the dataset we are working with by taking a random sample of 5 rows
at a time.

Implement q4() below to sample 5 points from each year's data.

Code design: I recommend using a for loop to iterate over the dataframes.
If df is a DataFrame, df.sample(5) returns a random sample of 5 rows.
"""

def q4():
    # Sample 5 rows from each dataframe
    # Print out the samples
    raise NotImplementedError

# Uncomment below and run python3 part1.py to see the samples.
# q4()

"""
You can run a few times to see different samples.

Based on the data, write down at least 2 strengths
and 3 weaknesses of this dataset.

=== ANSWER Q4 BELOW ===
Strengths:
1.
2.

Weaknesses:
1.
2.
3.
=== END OF Q4 ANSWER ===
"""

"""
5. Data cleaning

Let's see where we stand in terms of null values.
We can do this in two different ways.
First, use .info() to see the number of non-null values in each column
displayed in the console.

Then, write a version using .count() to return the number of null values
in each column as a dictionary.

Remove the @pytest.mark.skip and run the tests when you are done.
"""

def q5_info():
    # TODO
    raise NotImplementedError

def q5_count():
    # TODO
    raise NotImplementedError
    # Remember to return the dictionary here

NUM_NON_NULL = 0 # TODO: Fill this in

@pytest.mark.skip
def test_q5():
    q5_info()
    dict = q5_count()
    for key, value in dict.items():
        assert value == NUM_NON_NULL

"""
6. Adding columns

Notice that there is no 'year' column in any of the dataframe. As your first task, append an appropriate 'year' column in each dataframe.

Append a column 'year' in each dataframe. It must correspond to the year for which the data is represented.
"""

def q6():
    # TODO
    raise NotImplementedError

"""
7. Next, find the count of universities in each region that made it to the Top 100 each year. Print all of them/
"""

def q7():
    # Enter Code here
    # TODO
    raise NotImplementedError

"""
Do you notice some trend? Comment on what you observe and why might that be consistent throughout the years.

=== ANSWER Q7 BELOW ===

=== END OF Q7 ANSWER ===
"""

"""
8.
From the data of 2021, find the average score of all attributes for all universities.
"""

def q8():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
9.
From the same data of 2021, now find the average of *each* region for **all** attributes **excluding** 'rank' and 'year'. Store the results in a temporary variable named **average_2021**.
"""

def q9():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
10.
Sort the average_2021 dataframe from the previous question based on overall score in a descending fashion (top to bottom).
"""

# Enter Code here

"""
11.
What do you observe from the table above? Which country tops the ranking?
Which countries went down in the rankings?

Note: This is an open-ended question. Comment on why you think is the reason that USA is not top of the list.

=== ANSWER Q11 BELOW ===

=== END OF Q11 ANSWER ===
"""

"""
12.
Represent all the attributes in the average_2021 dataframe using a box and whisker plot. Do you observe any anomalies in any of them? (7+3)

**Hint:** You can do this using subplots (and also otherwise)
"""

def q12():
    # Enter code here
    # TODO
    raise NotImplementedError

# Write about anomalies in comments

"""
13.
Represent all the attributes in the average_2021 dataframe using a scatter plot. Do you observe any general trend?

**Hint:** Very similar to the previous question
"""

def q13():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
We're just wrapping up now.

Let's come to the Top 10 Universities and observe how they performed over the years.

14. Create a smaller dataframe which has the top ten universities from each year, and only their overall scores across the three years. (5)

Hint:

*   There will be four columns in the dataframe you make
*   The top ten universities are same across the three years. Only their rankings differ.
*   Use the merge function. You can read more about how to use it in the documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
*   Shape of the resultant dataframe should be (10, 4)
"""

def q14():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
As you noticed that when you merged, Pandas auto-assigned the column names. Let's change them.

15.
For the columns representing scores, rename them such that they describe the data that the column holds.
"""

def q15():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
16.
Draw a suitable plot to show how the overall scores of the Top 10 universities varied over the three years. Clearly label your graph and attach a legend. Explain why you chose the particular plot.

Note:
*   All universities must be in the same plot.
*   Your graph should be clear and legend should be placed suitably
"""

def q16():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
17.
What do you observe from the plot above? Which university has remained consistent in their scores? Which have increased/decreased over the years?

=== ANSWER Q17 BELOW ===

=== END OF Q17 ANSWER ===

18.
Let's finally look at another useful tool to get an idea about how different variables are corelated to each other. We call it a **correlation matrix**

A correlation matrix provides a correlation coefficient (a number between -1 and 1) that tells how strongly two variables are correlated. Values closer to -1 mean strong negative correlation whereas values closer to 1 mean strong positve correlation. Values closer to 0 show variables having no or little correlation.

You can learn more about correlation matrices from here: https://www.statology.org/how-to-read-a-correlation-matrix/
"""

def q18():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
19.
Plot a correlation matrix to see how each variable is correlated to another. You can use the data from 2021. (5)

**Helpful link:** https://datatofish.com/correlation-matrix-pandas/
"""

def q19():
    # Enter code here
    # TODO
    raise NotImplementedError

"""
20. Comment on the matrix you obtained in the previous part.

=== ANSWER Q20 BELOW ===

=== END OF Q20 ANSWER ===
"""

"""
21. Exploring data manipulation and falsification

For fun, this part will ask you to come up with a way to alter the
rankings such that your university of choice comes out in 1st place.

The data does not contain UC Davis, so let's pick a different university.
UC Berkeley is a public university nearby and in the same university system,
so let's pick that one.

We will write two functions.
First, write a function that chooses a new column and calculates
it in such a way that Berkeley will come out on top in the 2021 rankings.

Then use it to sort the data by the new values and return the top 10 universities.
"""

def q21a(df):
    # TODO
    raise NotImplementedError

def q21b(df):
    # TODO
    raise NotImplementedError

"""
22. Exploring data manipulation and falsification, continued

This time, let's manipulate the data by changing the source files
instead.
Create a copy of data/2021.csv and name it
data/2021_falsified.csv.
Modify the data in such a way that UC Berkeley comes out on top.
"""

def q22():
    # TODO
    raise NotImplementedError

"""
23. Exploring data manipulation and falsification, continued

Which of the methods above do you think would be the most effective
if you were a "bad actor" trying to manipulate the rankings?

Which do you think would be the most difficult to detect?

=== ANSWER Q23 BELOW ===

=== END OF Q23 ANSWER ===
"""

"""
24. Wrapping things up

Finally, to wrap things up, let's put everything together
into a pipeline.
You will use this pipeline in the first part of Part 2.
"""

def q24():
    # TODO
    raise NotImplementedError

def PART_1_PIPELINE():
    # TODO
    raise NotImplementedError

"""
Wow! This was a long ride. But I'm sure you have learned alot through this assignment. Not only will this help you a lot in your project, but we have cleaned data extensively, looked at a variety of visualization techniques, analyzed the results we obtained.
"""

"""
=== Main function ===

Don't modify this part. It will put everything together,
run your pipeline and save all of your answers.
"""
