# AI in Soccer Analysis: Trend & Performance Tracker

A zero-dependency, online-compiler-friendly Python program designed to analyze soccer team performance trends over time. 

By utilizing pure Python built-in features, this script requires zero external libraries (like NumPy, Pandas, or SciPy), making it completely lightweight and ready to run out of the box in any environment.

## 🚀 Key Features
* **Zero Dependencies:** Runs flawlessly on standard Python 3 installations or online Python compilers.
* **Rolling Window Averages:** Computes a configurable moving average (default: last 3 matches) to smooth out match-to-match volatility.
* **Least-Squares Regression:** Uses custom linear algebra implementations to compute exact trend lines and slopes for team progression.
* **Comprehensive Metrics:** Tracks progression across critical football analytics benchmarks:
  * Points (Form)
  * Realized Goal Difference
  * Expected Goals (xG) Difference
  * Passing Accuracy percentages

## 📋 Sample Output
When executed, the program processes your matchday records and generates a clean text report:

```text
=== Soccer Trend Summary (Online Compiler Version) ===
Matches analyzed: 12
Rolling window: last 3 matches

Points          : upward   trend | slope = 0.0524 pts/matchday
Goal Difference : upward   trend | slope = 0.0612 goals/matchday
xG Difference   : upward   trend | slope = 0.0490 xG/matchday
Pass Accuracy   : upward   trend | slope = 0.5874 %/matchday

Recent form (last rolling values):
- Avg points:        1.67
- Avg goal diff:     1.00
- Avg xG diff:       1.13
- Avg pass accuracy: 86.00%
```

## 🛠️ How To Run
Simply execute the Python file via your terminal:
```bash
 soccer_analysis.py
```
