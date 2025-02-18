### readme

data pipeline project for learning purposes

- extract from sources like kaggle/FRED
- load to duckdb
- transform in postgresql
- orchestration: TBD
- testing: tbd
- exploration/visualization: jupyter/matplotlib/seaborn

changelog
- 2025-02-17
    - add extract script for Stripe sample data
        - to do: load multiple Stripe objects, database side code
    - misc cleanup
- 2025-02-12:
    - create project structure
    - write extract scripts for Kaggle, FRED
    - write load script to DuckDB
    - confirm DuckDB readable from Jupyter notebook