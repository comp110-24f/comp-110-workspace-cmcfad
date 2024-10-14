"""Practice w for loops w range"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    # Print each index: name
    print(f"{idx}: {names[idx]}")
