---
name: csv-quality-check
description: Check CSV files for basic data quality issues such as missing values, row/column counts, and simple structure validation. Use when working with tabular data that needs quick inspection before analysis.
---

## What this skill does
This skill helps inspect CSV files and quickly generate a basic data quality report. It focuses on deterministic checks like counting rows, columns, and identifying missing values.

## When to use
- When a user provides a CSV file
- When doing quick data validation before analysis
- When checking data completeness

## When NOT to use
- Not for unstructured data (e.g., text, PDFs)
- Not for advanced statistical analysis or machine learning tasks
- Not for very large-scale distributed data processing

## Inputs
- A file path to a CSV file

---
name: csv-quality-check
description: Check CSV files for basic data quality issues such as missing values, row/column counts, and simple validation. Use when quickly inspecting tabular data before analysis.
---

## What this skill does
This skill inspects a CSV file and generates a simple data quality report, including row count, column count, and missing values.

## When to use
- When a user provides a CSV file
- When doing quick data validation
- Before starting data analysis

## When NOT to use
- Not for unstructured data (e.g., text, PDF)
- Not for advanced analytics or ML tasks

## Inputs
- A CSV file path

## Steps
1. Load the CSV file using pandas
2. Count total number of rows and columns
3. Calculate missing values for each column
4. Generate a summary report

## Output format
A dictionary-like JSON output:
```json
{
  "rows": 100,
  "columns": 5,
  "missing_values": {
    "column1": 0,
    "column2": 3
  }
}


