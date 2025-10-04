# 📦 Package Sorter

A Python function to classify packages into `STANDARD`, `SPECIAL`, or `REJECTED` based on their dimensions and mass.

---

## 🚀 How It Works
- **Bulky**: Volume ≥ 1,000,000 cm³ **or** any dimension ≥ 150 cm.
- **Heavy**: Mass ≥ 20 kg.
- **Stacks**:
  - STANDARD → Neither bulky nor heavy
  - SPECIAL → Either bulky or heavy
  - REJECTED → Both bulky and heavy

---

## 🛠️ Usage
Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/package-sorter.git
cd package-sorter
