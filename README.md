# MannWhitney
# Language: Python
# Input: CSV
# Output: TXT
# Tested with: PluMA 2.0, Python 3.6
# Dependency: scipy_1.4.1, pandas_1.1.5

PluMA plugin that uses the Mann-Whitney test (Mann and Whitney, 1947)
to determine differentiating taxa for two sets of samples.

The input is a CSV file, with the sample name (ID) in the first column,
group (Group) in the second, and abundances following.

Output will be a TXT file, with differentiating taxa listed line-by-line.
