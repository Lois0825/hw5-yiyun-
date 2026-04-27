# CSV Quality Check Skill

## What this skill does
This skill checks CSV files for basic data quality issues, including missing values, row counts, and column counts. It helps quickly understand whether a dataset is usable before further analysis.

## Why I chose this
I chose this task because checking CSV data requires deterministic computation. A language model alone cannot reliably count rows or detect missing values, so a Python script is necessary.

## How to use
Provide a CSV file path, and the skill will generate a summary report.

Example:python .agents/skills/csv-quality-check/scripts/check_csv.py test.csv

## Script explanation
The Python script reads the CSV file using pandas and computes:
- number of rows
- number of columns
- missing values for each column

## What worked well
The script reliably produces consistent results and handles basic CSV validation efficiently.

## Limitations
- Only supports CSV files
- Does not perform advanced data validation
- Not optimized for very large datasets

## Demo Video
https://youtu.be/iCE1dY-jqAs

