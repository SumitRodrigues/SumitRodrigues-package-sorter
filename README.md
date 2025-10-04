# Package Sorter

A Python function to classify packages into `STANDARD`, `SPECIAL`, or `REJECTED` based on their dimensions and mass.

---

## How It Works
- **Bulky**: Volume ≥ 1,000,000 cm³ **or** any dimension ≥ 150 cm.
- **Heavy**: Mass ≥ 20 kg.
- **Stacks**:
  - STANDARD → Neither bulky nor heavy
  - SPECIAL → Either bulky or heavy
  - REJECTED → Both bulky and heavy

---

## Usage
Clone this repository:

`git clone https://github.com/SumitRodrigues/SumitRodrigues-package-sorter.git`

Run:

`python sort.py`

Expected output:

SPECIAL
SPECIAL
SPECIAL
REJECTED
STANDARD

Test Cases:

(100, 100, 100, 10) → SPECIAL

(200, 50, 50, 10) → SPECIAL

(100, 100, 100, 25) → SPECIAL

(200, 200, 200, 25) → REJECTED

(50, 50, 50, 5) → STANDARD
