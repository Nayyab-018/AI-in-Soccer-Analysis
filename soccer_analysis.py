#!/usr/bin/env python3
"""
Online-compiler friendly Soccer Trend Analysis
(no external libraries required)

What it does:
- Uses built-in sample match data
- Computes rolling averages (last 3 matches)
- Computes simple linear trend slope for each metric
- Prints a clear text report

Works on most online Python compilers out of the box.
"""

from typing import List, Dict, Tuple


def rolling_average(values: List[float], window: int) -> List[float]:
    result = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        chunk = values[start : i + 1]
        result.append(sum(chunk) / len(chunk))
    return result


def linear_slope(x: List[float], y: List[float]) -> float:
    """
    Returns slope of best-fit line using least squares:
    slope = cov(x,y) / var(x)
    """
    n = len(x)
    if n < 2:
        return 0.0

    x_mean = sum(x) / n
    y_mean = sum(y) / n

    num = 0.0
    den = 0.0
    for i in range(n):
        dx = x[i] - x_mean
        num += dx * (y[i] - y_mean)
        den += dx * dx

    if den == 0:
        return 0.0
    return num / den


def trend_word(slope: float, tiny: float = 1e-9) -> str:
    if slope > tiny:
        return "upward"
    if slope < -tiny:
        return "downward"
    return "flat"


def analyze(data: List[Dict[str, float]], window: int = 3) -> None:
    matchday = [row["matchday"] for row in data]
    goals_for = [row["goals_for"] for row in data]
    goals_against = [row["goals_against"] for row in data]
    xg_for = [row["xg_for"] for row in data]
    xg_against = [row["xg_against"] for row in data]
    pass_accuracy = [row["pass_accuracy"] for row in data]
    points = [row["points"] for row in data]

    goal_diff = [gf - ga for gf, ga in zip(goals_for, goals_against)]
    xg_diff = [xf - xa for xf, xa in zip(xg_for, xg_against)]

    points_roll = rolling_average(points, window)
    goal_diff_roll = rolling_average(goal_diff, window)
    xg_diff_roll = rolling_average(xg_diff, window)
    pass_roll = rolling_average(pass_accuracy, window)

    metrics: List[Tuple[str, List[float], str]] = [
        ("Points", points_roll, "pts"),
        ("Goal Difference", goal_diff_roll, "goals"),
        ("xG Difference", xg_diff_roll, "xG"),
        ("Pass Accuracy", pass_roll, "%"),
    ]

    print("=== Soccer Trend Summary (Online Compiler Version) ===")
    print(f"Matches analyzed: {len(data)}")
    print(f"Rolling window: last {window} matches\n")

    for label, values, unit in metrics:
        slope = linear_slope(matchday, values)
        direction = trend_word(slope)
        print(f"{label:16s}: {direction:8s} trend | slope = {slope:.4f} {unit}/matchday")

    print("\nRecent form (last rolling values):")
    print(f"- Avg points:        {points_roll[-1]:.2f}")
    print(f"- Avg goal diff:     {goal_diff_roll[-1]:.2f}")
    print(f"- Avg xG diff:       {xg_diff_roll[-1]:.2f}")
    print(f"- Avg pass accuracy: {pass_roll[-1]:.2f}%")


def main() -> None:
    # Built-in demo data (12 matchdays)
    data = [
        {"matchday": 1, "goals_for": 1, "goals_against": 2, "xg_for": 1.2, "xg_against": 1.9, "pass_accuracy": 78, "points": 0},
        {"matchday": 2, "goals_for": 2, "goals_against": 1, "xg_for": 1.8, "xg_against": 1.2, "pass_accuracy": 80, "points": 3},
        {"matchday": 3, "goals_for": 0, "goals_against": 1, "xg_for": 0.7, "xg_against": 1.1, "pass_accuracy": 77, "points": 1},
        {"matchday": 4, "goals_for": 2, "goals_against": 1, "xg_for": 1.9, "xg_against": 1.0, "pass_accuracy": 81, "points": 3},
        {"matchday": 5, "goals_for": 3, "goals_against": 0, "xg_for": 2.3, "xg_against": 0.8, "pass_accuracy": 83, "points": 3},
        {"matchday": 6, "goals_for": 1, "goals_against": 2, "xg_for": 1.1, "xg_against": 1.7, "pass_accuracy": 79, "points": 0},
        {"matchday": 7, "goals_for": 2, "goals_against": 1, "xg_for": 1.7, "xg_against": 1.1, "pass_accuracy": 82, "points": 3},
        {"matchday": 8, "goals_for": 2, "goals_against": 1, "xg_for": 2.0, "xg_against": 1.2, "pass_accuracy": 84, "points": 1},
        {"matchday": 9, "goals_for": 1, "goals_against": 2, "xg_for": 1.4, "xg_against": 1.8, "pass_accuracy": 81, "points": 0},
        {"matchday": 10, "goals_for": 3, "goals_against": 1, "xg_for": 2.5, "xg_against": 0.9, "pass_accuracy": 85, "points": 3},
        {"matchday": 11, "goals_for": 2, "goals_against": 0, "xg_for": 2.1, "xg_against": 0.7, "pass_accuracy": 86, "points": 3},
        {"matchday": 12, "goals_for": 2, "goals_against": 1, "xg_for": 2.2, "xg_against": 1.0, "pass_accuracy": 87, "points": 1},
    ]

    analyze(data, window=3)


if __name__ == "__main__":
    main()
