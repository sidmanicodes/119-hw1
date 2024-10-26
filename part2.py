"""
Part 2: Performance Comparisons

**Released: Wednesday, October 16**

In this part, we will explore comparing the performance
of different pipelines.
First, we will set up some helper classes.
Then we will do a few comparisons
between two or more versions of a pipeline
to report which one is faster.
"""

import part1
from tqdm import tqdm
from typing import Optional

"""
=== Questions 1-5: Throughput and Latency Helpers ===

We will design and fill out two helper classes.

The first is a helper class for throughput (Q1).
The class is created by adding a series of pipelines
(via .add_pipeline(name, size, func))
where name is a title describing the pipeline,
size is the number of elements in the input dataset for the pipeline,
and func is a function that can be run on zero arguments
which runs the pipeline (like def f()).

The second is a similar helper class for latency (Q3).

1. Throughput helper class

Fill in the add_pipeline, eval_throughput, and generate_plot functions below.
"""
import time
import matplotlib.pyplot as plt

# Number of times to run each pipeline in the following results.
# You may modify this if any of your tests are running particularly slow
# or fast (though it should be at least 10).
NUM_RUNS = 10

class ThroughputHelper:
    def __init__(self):
        # Initialize the object.
        # Pipelines: a list of functions, where each function
        # can be run on no arguments.
        # (like: def f(): ... )
        self.pipelines = []

        # Pipeline names
        # A list of names for each pipeline
        self.names = []

        # Pipeline input sizes
        self.sizes = []

        # Pipeline throughputs
        # This is set to None, but will be set to a list after throughputs
        # are calculated.
        self.throughputs = None

    def add_pipeline(self, name: str, func: callable, size: int) -> None:
        self.pipelines.append(func)
        self.names.append(name)
        self.sizes.append(size)

    def compare_throughput(self, create_input_from_size: bool = True) -> list[float]:
        # Measure the throughput of all pipelines
        # and store it in a list in self.throughputs.
        # Make sure to use the NUM_RUNS variable.
        # Also, return the resulting list of throughputs,
        # in **number of items per second.**
        if not self.throughputs:
            self.throughputs = []

        for i in tqdm(range(len(self.pipelines)), desc="Comparing throughputs..."):
            total_time = 0
            for _ in range(NUM_RUNS):
                start = time.time()

                # If we have data to pass through pipeline
                if create_input_from_size:
                    self.pipelines[i]([10] * self.sizes[i]) # Execute function

                # If we have no data to pass through pipeline
                else:
                    print(f"Running {self.names[i]}")
                    self.pipelines[i]()

                end = time.time()
                total_time += end - start # Increment total execution time of current run

            # Average throughput = number of items / average time
            # print(f"sizes[i]: {self.sizes[i]}")
            avg_throughput = self.sizes[i] / total_time / NUM_RUNS
            self.throughputs.append(avg_throughput)

        return self.throughputs

    def generate_plot(self, filename):
        # Generate a plot for throughput using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        plt.figure(figsize=(16, 10))

        bars = []

        for i in range(len(self.names)):
            bar = plt.bar(x=self.names[i], height=self.throughputs[i], label=self.names[i])
            bars.append(bar)

        plt.xlabel("Pipeline")
        plt.ylabel("Average throughput")
        plt.title(f"Average throughput across all pipelines for {NUM_RUNS} runs")
        plt.legend()

        plt.savefig(filename)
        # plt.show()

"""
As your answer to this part,
return the name of the method you decided to use in
matplotlib.

(Example: "boxplot" or "scatter")
"""

def q1() -> str:
    # Return plot method (as a string) from matplotlib
    return "bar plot"

"""
2. A simple test case

To make sure your monitor is working, test it on a very simple
pipeline that adds up the total of all elements in a list.

We will compare three versions of the pipeline depending on the
input size.
"""

LIST_SMALL = [10] * 100
LIST_MEDIUM = [10] * 100_000
LIST_LARGE = [10] * 100_000_000

def add_list(l: list[int]) -> int:
    total = 0

    for item in l:
        total += item

    return total

def q2a():
    # Create a ThroughputHelper object
    h = ThroughputHelper()
    # Add the 3 pipelines.
    # (You will need to create a pipeline for each one.)
    # Pipeline names: small, medium, large
    h.add_pipeline(name='small', size=len(LIST_SMALL), func=add_list)
    h.add_pipeline(name='medium', size=len(LIST_MEDIUM), func=add_list)
    h.add_pipeline(name='large', size=len(LIST_LARGE), func=add_list)

    # Run pipelines
    throughputs = h.compare_throughput()

    # Generate a plot.
    # Save the plot as 'output/q2a.png'.
    h.generate_plot(filename='output/q2a.png')
    # Finally, return the throughputs as a list.
    return throughputs

"""
2b.
Which pipeline has the highest throughput?
Is this what you expected?

=== ANSWER Q2b BELOW ===
The largest pipeline had the highest throughput. I expected this because since we are sending
the most amount data through the pipeline, and I didn't necessarily expect the execution time to
scale linearly
=== END OF Q2b ANSWER ===
"""

"""
3. Latency helper class.

Now we will create a similar helper class for latency.

The helper should assume a pipeline that only has *one* element
in the input dataset.

It should use the NUM_RUNS variable as with throughput.
"""

class LatencyHelper:
    def __init__(self):
        # Initialize the object.
        # Pipelines: a list of functions, where each function
        # can be run on no arguments.
        # (like: def f(): ... )
        self.pipelines = []

        # Pipeline names
        # A list of names for each pipeline
        self.names = []

        self.sizes = []

        # Pipeline latencies
        # This is set to None, but will be set to a list after latencies
        # are calculated.
        self.latencies = None

    def add_pipeline(self, name: str, func: callable, size: int) -> None:
        self.pipelines.append(func)
        self.names.append(name)
        self.sizes.append(size)

    def compare_latency(self, create_input_from_size: bool = True) -> list[float]:
        # Measure the latency of all pipelines
        # and store it in a list in self.latencies.
        # Also, return the resulting list of latencies,
        # in **milliseconds.**
        if not self.latencies:
            self.latencies = []

        for i in tqdm(range(len(self.pipelines)), desc="Comparing latencies"):
            total_time = 0
            for _ in range(NUM_RUNS):
                start = time.time()

                # If there is data to pass through the pipe
                if create_input_from_size:
                    self.pipelines[i]([10] * self.sizes[i])

                # If there are no arguments, execute the pipeline
                else:
                    self.pipelines[i]()

                end = time.time()
                total_time += end - start # Increment total execution time of current run

            # Average throughput = number of items / average time
            # print(f"sizes[i]: {self.sizes[i]}")
            avg_latency = total_time / self.sizes[i] / NUM_RUNS
            self.latencies.append(avg_latency * 1_000)

        return self.latencies

    def generate_plot(self, filename: str) -> None:
        # Generate a plot for latency using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        plt.figure(figsize=(16, 10))

        bars = []

        for i in range(len(self.names)):
            bar = plt.bar(x=self.names[i], height=self.latencies[i], label=self.names[i])
            bars.append(bar)

        plt.xlabel("Pipeline")
        plt.ylabel("Average latency")
        plt.title(f"Average latencies across all pipelines for {NUM_RUNS} runs")
        plt.legend()

        plt.savefig(filename)

"""
As your answer to this part,
return the number of input items that each pipeline should
process if the class is used correctly.
"""

def q3():
    # Return the number of input items in each dataset,
    # for the latency helper to run correctly.
    return 1

"""
4. To make sure your monitor is working, test it on
the simple pipeline from Q2.

For latency, all three pipelines would only process
one item. Therefore instead of using
LIST_SMALL, LIST_MEDIUM, and LIST_LARGE,
for this question run the same pipeline three times
on a single list item.
"""

LIST_SINGLE_ITEM = [10] # Note: a list with only 1 item

def q4a():
    # Create a LatencyHelper object
    h = LatencyHelper()
    # Add the single pipeline three times.
    h.add_pipeline(name='pipe1', size=1, func=add_list)
    h.add_pipeline(name='pipe2', size=1, func=add_list)
    h.add_pipeline(name='pipe3', size=1, func=add_list)

    latencies = h.compare_latency()
    # Generate a plot.
    # Save the plot as 'output/q4a.png'.
    h.generate_plot('output/q4a.png')
    # Finally, return the latencies as a list.
    return latencies

"""
4b.
How much did the latency vary between the three copies of the pipeline?
Is this more or less than what you expected?

=== ANSWER Q1b BELOW ===
The latency was much higher for the first pipeline than the other two. I
didn't expect this because we are running the same amount of data through
the pipes, which are all identical
=== END OF Q1b ANSWER ===
"""

"""
Now that we have our helpers, let's do a simple comparison.

NOTE: you may add other helper functions that you may find useful
as you go through this file.

5. Comparison on Part 1

Finally, use the helpers above to calculate the throughput and latency
of the pipeline in part 1.
"""

# You will need these:
# part1.load_input
# part1.PART1_PIPELINE

from part1 import load_input as load_part1_input, PART_1_PIPELINE

df1, df2, df3 = load_part1_input()

# The total input size is the total number of rows in all dataframes
part1_input_size = df1.shape[0] + df2.shape[0] + df3.shape[0]

def q5a():
    # Return the throughput of the pipeline in part 1.
    print(part1_input_size)
    h = ThroughputHelper()
    h.add_pipeline(name='Part 1 pipeline', size=part1_input_size, func=PART_1_PIPELINE)
    throughputs = h.compare_throughput(create_input_from_size=False)
    return throughputs

def q5b():
    # Return the latency of the pipeline in part 1.
    h = LatencyHelper()
    h.add_pipeline(name='Part 1 pipeline', size=part1_input_size, func=PART_1_PIPELINE)
    latencies = h.compare_latency(create_input_from_size=False)
    return latencies

"""
===== Questions 6-10: Performance Comparison 1 =====

For our first performance comparison,
let's look at the cost of getting input from a file, vs. in an existing DataFrame.

6. We will use the same population dataset
that we used in lecture 3.

Load the data using load_input() given the file name.

- Make sure that you clean the data by removing
  continents and world data!
  (World data is listed under OWID_WRL)

Then, set up a simple pipeline that computes summary statistics
for the following:

- *Year over year increase* in population, per country

    (min, median, max, mean, and standard deviation)

How you should compute this:

- For each country, we need the maximum year and the minimum year
in the data. We should divide the population difference
over this time by the length of the time period.

- Make sure you throw out the cases where there is only one year
(if any).

- We should at this point have one data point per country.

- Finally, as your answer, return a list of the:
    min, median, max, mean, and standard deviation
  of the data.

Hints:
You can use the describe() function in Pandas to get these statistics.
You should be able to do something like
df.describe().loc["min"]["colum_name"]

to get a specific value from the describe() function.

You shouldn't use any for loops.
See if you can compute this using Pandas functions only.
"""

import pandas as pd
from typing import Union


def load_input(filename: str) -> pd.DataFrame:
    # Return a dataframe containing the population data
    # **Clean the data here**
    df = pd.read_csv(filename)

    # Remove world data
    df = df[df.Code != "OWID_WRL"]

    return df


def population_pipeline(df: pd.DataFrame) -> list[float, float, float, float, float]:
    # Input: the dataframe from load_input()
    def get_yoy_increase(group: pd.DataFrame) -> Union[float | None]:
        """
        Helper function used to calculate the YOY increase in population for a single country
        """
        group = group.sort_values(by='Year')

        min_year_row = group.iloc[0]
        max_year_row = group.iloc[-1]

        year_diff = max_year_row['Year'] - min_year_row['Year']
        pop_diff = max_year_row['Population (historical)'] - min_year_row['Population (historical)']

        if year_diff != 0:
            return pop_diff / year_diff
        return None
    
    # Return a list of min, median, max, mean, and standard deviation
    if df.shape[0] > 1:
        agg_df = df.groupby(by='Entity').apply(get_yoy_increase).dropna().reset_index(name='YOY_increase')
        stats = agg_df.describe()['YOY_increase']

        return [stats.loc['min'], stats.loc['50%'], stats.loc['max'], stats.loc['mean'], stats.loc['std']]
    else:
        return [0.0, 0.0, 0.0, 0.0, 0.0]

def q6():
    # As your answer to this part,
    # call load_input() and then population_pipeline()
    # Return a list of min, median, max, mean, and standard deviation
    df = load_input("./data/population.csv")
    stats = population_pipeline(df)
    return stats


"""
7. Varying the input size

Next we want to set up three different datasets of different sizes.

Create three new files,
    - data/population-small.csv
      with the first 600 rows
    - data/population-medium.csv
      with the first 6000 rows
    - data/population-single-row.csv
      with only the first row
      (for calculating latency)

You can edit the csv file directly to extract the first rows
(remember to also include the header row)
and save a new file.

Make four versions of load input that load your datasets.
(The _large one should use the full population dataset.)
"""

def load_input_small():
    return load_input('./data/population-small.csv')

def load_input_medium():
    return load_input('./data/population-medium.csv')

def load_input_large():
    return load_input('./data/population.csv')

def load_input_single_row():
    # This is the pipeline we will use for latency.
    return load_input('./data/population-single-row.csv')

def q7():
    # Don't modify this part
    s = load_input_small()
    m = load_input_medium()
    l = load_input_large()
    x = load_input_single_row()
    return [len(s), len(m), len(l), len(x)]

"""
8.
Create baseline pipelines

First let's create our baseline pipelines.
Create four pipelines,
    baseline_small
    baseline_medium
    baseline_large
    baseline_latency

based on the three datasets above.
Each should call your population_pipeline from Q7.
"""

def baseline_small() -> list[float, float, float, float, float]:
    df = load_input_small()
    stats = population_pipeline(df)
    return stats

def baseline_medium():
    df = load_input_medium()
    stats = population_pipeline(df)
    return stats

def baseline_large():
    df = load_input_large()
    stats = population_pipeline(df)
    return stats

def baseline_latency():
    df = load_input_single_row()
    stats = population_pipeline(df)
    return stats

def q8():
    # Don't modify this part
    _ = baseline_medium()
    return ["baseline_small", "baseline_medium", "baseline_large", "baseline_latency"]

"""
9.
Finally, let's compare whether loading an input from file is faster or slower
than getting it from an existing Pandas dataframe variable.

Create four new dataframes (constant global variables)
directly in the script.
Then use these to write 3 new pipelines:
    fromvar_small
    fromvar_medium
    fromvar_large
    fromvar_latency

As your answer to this part;
a. Generate a plot in output/q9a.png of the throughputs
    Return the list of 6 throughputs in this order:
    baseline_small, baseline_medium, baseline_large, fromvar_small, fromvar_medium, fromvar_large
b. Generate a plot in output/q9b.png of the latencies
    Return the list of 2 latencies in this order:
    baseline_latency, fromvar_latency
"""

POPULATION_SMALL = load_input_small()
POPULATION_MEDIUM = load_input_medium()
POPULATION_LARGE = load_input_large()
POPULATION_SINGLE_ROW = load_input_single_row()

def fromvar_small():
    population_pipeline(POPULATION_SMALL)

def fromvar_medium():
    population_pipeline(POPULATION_MEDIUM)

def fromvar_large():
    population_pipeline(POPULATION_LARGE)

def fromvar_latency():
    population_pipeline(POPULATION_SINGLE_ROW)

def q9a() -> list[int, int, int, int, int, int]:
    # Add all 6 pipelines for a throughput comparison
    h = ThroughputHelper()

    h.add_pipeline(name='baseline_small', func=baseline_small, size=len(POPULATION_SMALL))
    h.add_pipeline(name='baseline_medium', func=baseline_medium, size=len(POPULATION_MEDIUM))
    h.add_pipeline(name='baseline_large', func=baseline_large, size=len(POPULATION_LARGE))

    h.add_pipeline(name='fromvar_small', func=fromvar_small, size=len(POPULATION_SMALL))
    h.add_pipeline(name='fromvar_medium', func=fromvar_medium, size=len(POPULATION_MEDIUM))
    h.add_pipeline(name='fromvar_large', func=fromvar_large, size=len(POPULATION_LARGE))

    # Compare throughputs
    throughputs = h.compare_throughput(create_input_from_size=False)

    # Generate plot in ouptut/q9a.png
    h.generate_plot('output/q9a.png')

    # Return list of 6 throughputs
    return throughputs

def q9b() -> list[int, int]:
    # Add 2 pipelines for a latency comparison
    h = LatencyHelper()

    h.add_pipeline(name='baseline_latency', func=baseline_latency, size=len(POPULATION_SINGLE_ROW))
    h.add_pipeline(name='fromvar_latency', func=fromvar_latency, size=len(POPULATION_SINGLE_ROW))

    # Compare latencies
    latencies = h.compare_latency(create_input_from_size=False)

    # Generate plot in ouptut/q9b.png
    h.generate_plot('output/q9b.png')

    # Return list of 2 latencies
    return latencies

"""
10.
Comment on the plots above!
How dramatic is the difference between the two pipelines?
Which differs more, throughput or latency?
What does this experiment show?

===== ANSWER Q10 BELOW =====
On average, the throughputs from the variables were much higher than from the
files, which makes sense since we're shoving the same amount of data through the pipeline
but it takes additional time for the baseline pipes to load the files. For the same reason,
the latency for the baseline was much higher than when loading from a variable
===== END OF Q10 ANSWER =====
"""

"""
===== Questions 11-14: Performance Comparison 2 =====

Our second performance comparison will explore vectorization.

Operations in Pandas use Numpy arrays and vectorization to enable
fast operations.
In particular, they are often much faster than using for loops.

Let's explore whether this is true!

11.
First, we need to set up our pipelines for comparison as before.

We already have the baseline pipelines from Q8,
so let's just set up a comparison pipeline
which uses a for loop to calculate the same statistics.

Create a new pipeline:
- Iterate through the dataframe entries. You can assume they are sorted.
- Manually compute the minimum and maximum year for each country.
- Add all of these to a Python list. Then manually compute the summary
  statistics for the list (min, median, max, mean, and standard deviation).
"""

import numpy as np
from collections import defaultdict

def for_loop_pipeline(df: pd.DataFrame) -> list[float, float, float, float, float]:
    # Input: the dataframe from load_input()
    # Return a list of min, median, max, mean, and standard deviation
    entities = df["Entity"].unique()
    entities_dict = {}
    stats = defaultdict(dict)
    res = [0 for _ in range(len(entities))]

    for i, entity in enumerate(entities):
        entities_dict[entity] = i

    for _, entry in tqdm(df.iterrows(), desc="Iterating over rows"):
        entity = entry["Entity"]
        if entity not in stats:
            stats[entity]['max_year'] = entry["Year"]
            stats[entity]['min_year'] = entry["Year"]
            stats[entity]['max_population'] = entry["Population (historical)"]
            stats[entity]['min_population'] = entry["Population (historical)"]
        else:
            if entry["Year"] > stats[entity]['max_year']:
                stats[entity]['max_year'] = entry["Year"]
                stats[entity]['max_population'] = entry["Population (historical)"]

            
            if entry["Year"] < stats[entity]['min_year']:
                stats[entity]['min_year'] = entry["Year"]
                stats[entity]['min_population'] = entry["Population (historical)"]

            if stats[entity]['min_year'] != stats[entity]['max_year']:
                res[entities_dict[entity]] = (stats[entity]['max_population'] - stats[entity]['min_population']) / (stats[entity]['max_year'] - stats[entity]['min_year'])

    # Compute (min, median, max, mean, and standard deviation)
    return [np.min(res), np.median(res), np.max(res), np.mean(res), np.std(res)]

def q11() -> list[float, float, float, float, float]:
    # As your answer to this part, call load_input() and then
    # for_loop_pipeline() to return the 5 numbers.
    # (these should match the numbers you got in Q6.)
    df = load_input("./data/population.csv")
    return for_loop_pipeline(df)

"""
12.
Now, let's create our pipelines for comparison.

As before, write 4 pipelines based on the datasets from Q7.
"""

def for_loop_small():
    df = load_input_small()
    return for_loop_pipeline(df)

def for_loop_medium():
    df = load_input_medium()
    return for_loop_pipeline(df)

def for_loop_large():
    df = load_input_large()
    return for_loop_pipeline(df)

def for_loop_latency():
    df = load_input_single_row()
    return for_loop_pipeline(df)

def q12():
    # Don't modify this part
    _ = for_loop_medium()
    return ["for_loop_small", "for_loop_medium", "for_loop_large", "for_loop_latency"]

"""
13.
Finally, let's compare our two pipelines,
as we did in Q9.

a. Generate a plot in output/q13a.png of the throughputs
    Return the list of 6 throughputs in this order:
    baseline_small, baseline_medium, baseline_large, for_loop_small, for_loop_medium, for_loop_large

b. Generate a plot in output/q13b.png of the latencies
    Return the list of 2 latencies in this order:
    baseline_latency, for_loop_latency
"""

def q13a():
    # Add all 6 pipelines for a throughput comparison
    h = ThroughputHelper()

    h.add_pipeline(name='baseline_small', func=baseline_small, size=len(POPULATION_SMALL))
    h.add_pipeline(name='baseline_medium', func=baseline_medium, size=len(POPULATION_MEDIUM))
    h.add_pipeline(name='baseline_large', func=baseline_large, size=len(POPULATION_LARGE))

    h.add_pipeline(name='forloop_small', func=for_loop_small, size=len(POPULATION_SMALL))
    h.add_pipeline(name='forloop_medium', func=for_loop_medium, size=len(POPULATION_MEDIUM))
    h.add_pipeline(name='forloop_large', func=for_loop_large, size=len(POPULATION_LARGE))

    # Compare throughputs
    throughputs = h.compare_throughput(create_input_from_size=False)

    # Generate plot in ouptut/q13a.png
    h.generate_plot('output/q13a.png')

    # Return list of 6 throughputs
    return throughputs

def q13b():
    # Add 2 pipelines for a latency comparison
    h = LatencyHelper()

    h.add_pipeline(name='baseline_latency', func=baseline_latency, size=len(POPULATION_SINGLE_ROW))
    h.add_pipeline(name='forloop_latency', func=for_loop_latency, size=len(POPULATION_SINGLE_ROW))

    # Compare latencies
    latencies = h.compare_latency(create_input_from_size=False)

    # Generate plot in ouptut/q13b.png
    h.generate_plot('output/q13b.png')

    # Return list of 2 latencies
    return latencies

"""
14.
Comment on the results you got!

14a. Which pipelines is faster in terms of throughput?

===== ANSWER Q14a BELOW =====
The baseline pipelines had a much higher throughput compared to the for-loop
implementations, which is to be expected
===== END OF Q14a ANSWER =====

14b. Which pipeline is faster in terms of latency?

===== ANSWER Q14b BELOW =====
While there was a large difference between the throughputs of the pipelines,
there wasn't that much of a difference in latency, though it should be noted that
latency for the for-loops were slightly higher
===== END OF Q14b ANSWER =====

14c. Do you notice any other interesting observations?
What does this experiment show?

===== ANSWER Q14c BELOW =====
This experiment shows the power that vectorized operations have, and that if we
want to enhance our pipeline's throughput and latency we should take full advantage of them
===== END OF Q14c ANSWER =====
"""

"""
===== Questions 15-17: Reflection Questions =====
15.

Take a look at all your pipelines above.
Which factor that we tested (file vs. variable, vectorized vs. for loop)
had the biggest impact on performance?

===== ANSWER Q15 BELOW =====
Vectorized vs. for loop had the biggest impact on performance, as there was a significant difference
in throughput for the baseline vs for-loop pipelines
===== END OF Q15 ANSWER =====

16.
Based on all of your plots, form a hypothesis as to how throughput
varies with the size of the input dataset.

(Any hypothesis is OK as long as it is supported by your data!
This is an open ended question.)

===== ANSWER Q16 BELOW =====
It seems like more data actually leads to an improvement in throughput.
This is probably because of the overhead costs for set up and initialization 
for smaller datasets and the fact that CPUs are good at handling bulk data
processing
===== END OF Q16 ANSWER =====

17.
Based on all of your plots, form a hypothesis as to how
throughput is related to latency.

(Any hypothesis is OK as long as it is supported by your data!
This is an open ended question.)

===== ANSWER Q17 BELOW =====
Throughput is the inverse of latency. We can see that this is the case 
because our latency graphs are basically the reflection of our throughput
graphs
===== END OF Q17 ANSWER =====
"""

"""
===== Extra Credit =====

This part is optional.

Use your pipeline to compare something else!

Here are some ideas for what to try:
- the cost of random sampling vs. the cost of getting rows from the
  DataFrame manually
- the cost of cloning a DataFrame
- the cost of sorting a DataFrame prior to doing a computation
- the cost of using different encodings (like one-hot encoding)
  and encodings for null values
- the cost of querying via Pandas methods vs querying via SQL
  For this part: you would want to use something like
  pandasql that can run SQL queries on Pandas data frames. See:
  https://stackoverflow.com/a/45866311/2038713

As your answer to this part,
as before, return
a. the list of 6 throughputs
and
b. the list of 2 latencies.

and generate plots for each of these in the following files:
    output/extra_credit_a.png
    output/extra_credit_b.png
"""

# Extra credit (optional)

def extra_credit_a():
    raise NotImplementedError

def extra_credit_b():
    raise NotImplementedError

"""
===== Wrapping things up =====

**Don't modify this part.**

To wrap things up, we have collected
your answers and saved them to a file below.
This will be run when you run the code.
"""

ANSWER_FILE = "output/part2-answers.txt"
UNFINISHED = 0

def log_answer(name, func, *args):
    try:
        answer = func(*args)
        print(f"{name} answer: {answer}")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},{answer}\n')
            print(f"Answer saved to {ANSWER_FILE}")
    except NotImplementedError:
        print(f"Warning: {name} not implemented.")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},Not Implemented\n')
        global UNFINISHED
        UNFINISHED += 1

def PART_2_PIPELINE():
    open(ANSWER_FILE, 'w').close()

    # Q1-5
    log_answer("q1", q1)
    log_answer("q2a", q2a)
    # 2b: commentary
    log_answer("q3", q3)
    log_answer("q4a", q4a)
    # 4b: commentary
    log_answer("q5a", q5a)
    log_answer("q5b", q5b)

    # Q6-10
    log_answer("q6", q6)
    log_answer("q7", q7)
    log_answer("q8", q8)
    log_answer("q9a", q9a)
    log_answer("q9b", q9b)
    # 10: commentary

    # Q11-14
    log_answer("q11", q11)
    log_answer("q12", q12)
    log_answer("q13a", q13a)
    log_answer("q13b", q13b)
    # 14: commentary

    # 15-17: reflection
    # 15: commentary
    # 16: commentary
    # 17: commentary

    # Extra credit
    log_answer("extra credit (a)", extra_credit_a)
    log_answer("extra credit (b)", extra_credit_b)

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
=== END OF PART 2 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 2", PART_2_PIPELINE)
