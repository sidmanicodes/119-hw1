"""
Part 2: Performance Comparisons

In this part, each question will ask you to compare
two or more versions of a pipeline to determine which is the fastest.

You will compare the throughput and latency of each version of the pipeline
and report which one is faster.
"""

"""
1. Helper class

First, design and fill out the following helper class.
The helper class works by running a pipeline (provided as input)
on a series of datasets (also provided as input).

It can be used to calculate throughput and latency, as well
as to plot the throughput and latency as a function of the dataset.
"""

# Number of times to run each pipeline in the following results.
NUM_RUNS = 1000

class ThroughputLatencyMonitor:
    def __init__(self):
        # Initialize the object.
        # Datasets: a list of input CSV files
        self.datasets = []

        # Pipelines: a list of functions, where each function
        # can be run on an input dataset
        self.pipelines = []

        # Pipeline lengths: a list of how many data elements are
        # in each pipeline.
        # Should be the same length as self.pipelines
        self.pipeline_lengths = []

    def add_dataset(self, dataset):
        # TODO
        raise NotImplementedError

    def add_pipeline(self, pipeline):
        # TODO
        raise NotImplementedError

    def eval_throughput(self):
        # Measure the throughput of all pipelines
        # Return a Numpy array where row i, column j is the
        # throughput for pipeline i on dataset j.
        # This should also save the results to a variable inside the class.
        # TODO
        raise NotImplementedError

    def eval_latency(self):
        # Measure the latency of all pipelines
        # Return a Numpy array where row i, column j is the
        # latency for pipeline i on dataset j.
        # This should also save the results to a variable inside the class.
        # TODO
        raise NotImplementedError

    def generate_plots(self, throughput_filename, throughput_latency):
        # Generate plots for throughput and latency using matplotlib.
        # Save the results in the filenames provided.
        # TODO
        raise NotImplementedError

    def save_results(self):
        # Save the throughput and latency results to a CSV file.
        # There should be 2 rows per dataset (one for throughput and one for latency).
        # Columns should be:
        # - dataset name, throughput or latency, pipeline 1, pipeline 2, ..., best pipeline (where best is a number between 1 and the number of pipelines).
        # TODO
        raise NotImplementedError

"""
2. A simple comparison

First we will compare a simple comparison between two pipelines.
"""

"""
3. The cost of input

Next we will look at the cost of getting input from a file vs.
getting it from an already constructed DataFrame.
"""

"""
4. Vectorization
"""

"""
5. Explicit transformations vs. SQL
"""

"""
6. One-hot encoding
"""
