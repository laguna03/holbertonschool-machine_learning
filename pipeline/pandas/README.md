# Pandas Data Pipeline

This directory contains a comprehensive collection of Python scripts demonstrating various pandas DataFrame operations for data manipulation and analysis. The project focuses on cryptocurrency data processing, specifically working with Bitcoin exchange data.

## Project Overview

This project is part of the Holberton School Machine Learning curriculum, focusing on data pipelines using the pandas library. The scripts demonstrate fundamental to advanced DataFrame operations, from creation to visualization.

## Files Description

### Basic DataFrame Operations

- **`0-from_numpy.py`** - Creates a pandas DataFrame from a NumPy array with automatically generated column labels (A, B, C, etc.)
- **`1-from_dictionary.py`** - Creates a DataFrame from a Python dictionary with custom index labels
- **`2-from_file.py`** - Loads data from CSV files into a DataFrame with custom delimiters
- **`3-rename.py`** - Demonstrates column renaming operations
- **`4-array.py`** - Converts DataFrame columns to NumPy arrays

### Data Manipulation

- **`5-slice.py`** - Slices DataFrames to extract specific columns and rows (every 60th row)
- **`6-flip_switch.py`** - Performs DataFrame transposition and sorting operations
- **`7-high.py`** - Filters data based on high values in specific columns
- **`8-prune.py`** - Removes rows with missing values in critical columns
- **`9-fill.py`** - Handles missing data by:
  - Removing unnecessary columns (Weighted_Price)
  - Forward filling Close prices
  - Using Close values to fill missing High, Low, Open prices
  - Setting missing Volume values to 0

### Advanced Operations

- **`10-index.py`** - Sets the Timestamp column as the DataFrame index
- **`11-concat.py`** - Concatenates multiple DataFrames from different data sources (Bitstamp and Coinbase)
- **`12-hierarchy.py`** - Works with hierarchical/multi-level indexing
- **`13-analyze.py`** - Computes descriptive statistics for numerical columns
- **`14-visualize.py`** - Creates data visualizations using matplotlib, including:
  - Data preprocessing for 2017-2019 period
  - Time series plotting
  - Multiple subplot configurations

## Dependencies

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## Usage Examples

### Creating DataFrames

```python
# From NumPy array
from 0-from_numpy import from_numpy
df = from_numpy(np_array)

# From file
from 2-from_file import from_file
df = from_file('data.csv', ',')
```

### Data Processing Pipeline

```python
# Load data
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Clean and prepare data
df = fill(df)  # Handle missing values
df = index(df)  # Set proper index
df = slice(df)  # Extract relevant columns

# Analyze
stats = analyze(df)  # Get descriptive statistics
```

## Data Sources

The project primarily works with cryptocurrency exchange data, specifically:

- **Coinbase USD**: Minute-by-minute Bitcoin trading data from 2014-2019
- **Bitstamp**: Bitcoin exchange data for comparison and concatenation

## Key Learning Objectives

- DataFrame creation from various data sources
- Data cleaning and preprocessing techniques
- Handling missing values and data imputation
- Time series data manipulation
- Multi-source data concatenation
- Statistical analysis and visualization
- Index operations and hierarchical indexing

## Project Structure

```
pandas/
├── README.md
├── 0-from_numpy.py          # DataFrame creation from NumPy
├── 1-from_dictionary.py     # DataFrame creation from dict
├── 2-from_file.py          # CSV file loading
├── 3-rename.py             # Column renaming
├── 4-array.py              # DataFrame to array conversion
├── 5-slice.py              # Data slicing operations
├── 6-flip_switch.py        # Transposition and sorting
├── 7-high.py               # Value filtering
├── 8-prune.py              # Missing value removal
├── 9-fill.py               # Missing value imputation
├── 10-index.py             # Index operations
├── 11-concat.py            # DataFrame concatenation
├── 12-hierarchy.py         # Hierarchical indexing
├── 13-analyze.py           # Statistical analysis
└── 14-visualize.py         # Data visualization
```

## Notes

- All scripts follow PEP 8 style guidelines
- Each module includes comprehensive docstrings
- Functions are designed to be reusable and modular
- Error handling is implemented where appropriate
- The scripts build upon each other, creating a complete data processing pipeline

## Author

Pedro Laguna - Holberton School Machine Learning Program
