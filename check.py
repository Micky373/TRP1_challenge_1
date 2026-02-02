
from __future__ import annotations

import argparse


def bmi_index(w: float, h: float) -> float:
	if w <= 0 or h <= 0:
		raise ValueError("weight and height must be positive")
	return round(w / (h * h), 2)


def bmi_category(b: float) -> str:
	return ("Underweight" if b < 18.5 else
			"Normal weight" if b < 25 else
			"Overweight" if b < 30 else
			"Obesity")


def main() -> None:
	p = argparse.ArgumentParser()
	p.add_argument("-w", "--weight", type=float, required=True)
	p.add_argument("-h", "--height", type=float, required=True)
	a = p.parse_args()
	b = bmi_index(a.weight, a.height)
	print(f"BMI: {b} — {bmi_category(b)}")


if __name__ == "__main__":
	main()

