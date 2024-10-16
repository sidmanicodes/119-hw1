"""
Part 2: Performance Comparisons

**Released: Wednesday, October 16**

In this part, each question will ask you to compare
two or more versions of a pipeline to determine which is the fastest.

You will compare the throughput and latency of each version of the pipeline
and report which one is faster.
"""

import part1

"""
=== Questions 1-5: Throughput and Latency Helpers ===

1. Throughput helper class

We will design and fill out two helper classes.
The first is a helper class for throughput.
The class is created by adding a series of pipelines
(via .add_pipeline(name, size, func))
where name is a title describing the pipeline,
size is the number of elements in the input dataset for the pipeline,
and func is a function that can be run on zero arguments
which runs the pipeline (like def f()).

Fill in the add_pipeline, eval_throughput, and generate_plot functions below.
"""

# Number of times to run each pipeline in the following results.
NUM_RUNS = 1000

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

    def add_pipeline(self, name, size, func):
        raise NotImplementedError

    def compare_throughput(self):
        # Measure the throughput of all pipelines
        # and store it in a list in self.throughputs.
        # Also, return the throughput as a string.
        raise NotImplementedError

    def generate_plot(self, filename):
        # Generate a plot for throughput using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        raise NotImplementedError

"""
1b. As your answer to this part,
return the number of times you ran the pipeline in the above helper class
in each call to eval_throughput, per pipeline.
"""

def q1b():
    # Return the number of times you ran the pipeline.
    raise NotImplementedError

"""
2. A simple test case

To make sure your monitor is working, test it on a very simple
pipeline that adds up the total of all elements in a list.

We will compare three versions of the pipeline depending on the
input size.
"""

LIST_SMALL = [10] * 1000
LIST_MEDIUM = [10] * 100_000
LIST_LARGE = [10] * 10_000_000

def add_list(l):
    # TODO
    raise NotImplementedError

def q2a():
    # Create a ThroughputHelper object
    h = ThroughputHelper()
    # Add the 3 pipelines.
    # (You will need to create a pipeline for each one.)
    raise NotImplementedError
    # Finally, return the throughput and generate a plot.
    # Save the plot as 'output/q2a.png'.

"""
2b.
Which pipeline has the highest throughput?
Is this what you expected?

=== ANSWER Q2b BELOW ===

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

        # Pipeline latencies
        # This is set to None, but will be set to a list after latencies
        # are calculated.
        self.latencies = None

    def add_pipeline(self, name, func):
        raise NotImplementedError

    def compare_latency(self):
        # Measure the latency of all pipelines
        # and store it in a list in self.latencies.
        # Also, return the latency as a string.
        raise NotImplementedError

    def generate_plot(self, filename):
        # Generate a plot for latency using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        raise NotImplementedError

"""
3b. As your answer to this part,
return the number of input items that each pipeline should
process if the class is used correctly.
"""

def q3b():
    # Return the number of input items in each dataset,
    # for the latency helper to run correctly.
    raise NotImplementedError

"""
4. To make sure your monitor is working, test it on
the simple pipeline from Q2.
"""

LIST_SINGLE_ITEM = [] # TODO: fill in this line

def q4a():
    # Create a LatencyHelper object
    h = LatencyHelper()
    # Add the single pipeline
    # Finally, return the throughput and generate a plot.
    # Save the plot as 'output/q4a.png'.
    raise NotImplementedError

"""
Q4b.
If you were to run all three pipelines in Q2,
which pipeline would have the lowest latency?

(This is a bit of a trick question!
Remember that latency is measured as the time
it takes to process one item only.)

=== ANSWER Q1b BELOW ===

=== END OF Q1b ANSWER ===
"""

"""
5. Comparison on Part 1

Finally, use the helpers above to calculate the throughput and latency
of the pipeline in part 1.
"""

# You should need both of these
from part1 import load_input
from part1 import PART_1_PIPELINE

def q5a():
    # Return the throughput of the pipeline in part 1.
    raise NotImplementedError

def q5b():
    # Return the latency of the pipeline in part 1.
    raise NotImplementedError

"""
===== Questions 6-10: Performance Comparisons =====

Next, we will look at a series of performance comparisons
to compare:
- the cost of getting input from a file, vs. in an existing DataFrame
- the cost of vectorization (compared to for loops)
- the cost of explicit transformations vs. SQL
- the cost of using different encodings (like one-hot encoding)
  and encodings for null values.
"""

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

    try:
        dfs = part1.load_input()
    except NotImplementedError:
        print("load_input() not found; did you complete part 1?")
        dfs = []

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
That's it for Part 1!

=== END OF PART 1 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 2", PART_2_PIPELINE)
