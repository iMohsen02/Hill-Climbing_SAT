# SAT Solver Using Hill Climbing Algorithm

This project implements a **Satisfiability Problem (SAT)** solver using the **Hill Climbing algorithm**. The program receives a Boolean formula in **Conjunctive Normal Form (CNF)** as input and attempts to find a satisfying assignment for the formula. This project is developed as part of the **Advanced Design of Algorithms** course at Ferdowsi University of Mashhad (FUM).

---

## Features

-   **Input Parsing**: Parses Boolean formulas in CNF, allowing logical operators like `AND`, `OR`, and `NOT`.
-   **Random Restart**: Detects local minima and flat regions and restarts the search from a random state.
-   **Scoring Function**: Evaluates the current state based on the number of satisfied clauses.
-   **Neighbor Generation**: Generates neighboring states by flipping one variable at a time.
-   **Deep Logging**: Optionally logs the internal operations for debugging and detailed analysis.

---

## Problem Statement

The **SAT problem** is the task of determining whether there exists a truth assignment to the variables of a Boolean formula such that the formula evaluates to `True`. In this project, the Boolean formula is provided in CNF, where:

-   A formula consists of a conjunction (`AND`) of clauses.
-   Each clause is a disjunction (`OR`) of literals.
-   A literal is a variable or its negation (`NOT`).

### Example Input

```text
(a OR b OR NOT u) AND (NOT a OR u) AND (b OR u) AND (u OR NOT g)
```

---

## Algorithm

1. **Input Parsing**:
    - Parse the input Boolean formula into a structured CNF representation.
2. **Initialization**:
    - Randomly assign truth values (`True` or `False`) to all variables.
3. **Hill Climbing**:
    - Evaluate the current state.
    - Generate neighboring states by flipping one variable at a time.
    - Move to the neighbor with the highest score (number of satisfied clauses).
    - Repeat until either a solution is found or a local minimum is reached.
4. **Random Restart**:
    - If stuck in a local minimum or a flat region, restart with a new random state.
5. **Termination**:
    - Stop when a solution is found or the iteration limit is reached.

---

## Code Overview

### Class: `hill_climbing`

The main class implementing the SAT solver.

#### Methods:

-   `parse_input_to_CNF`: Converts the input formula into a structured CNF format.
-   `random_init_state`: Initializes a random truth assignment for the variables.
-   `gen_state_neighbors`: Generates neighboring states by flipping one variable.
-   `score_of`: Calculates the score (number of satisfied clauses) for a given state.
-   `solution`: Checks if the current state satisfies all clauses.
-   `hill_climbing`: Implements the core hill climbing algorithm.
-   `hill_climbing_satisfiability`: Entry point for solving the SAT problem.

---

## How to Run

1. Ensure Python is installed on your system.
2. Save the code to a file, e.g., `hill_climbing_sat.py`.
3. Run the program:
    ```bash
    python hill_climbing_sat.py
    ```
4. Enter a Boolean formula in CNF format when prompted, or modify the `text_clause` variable in the code.

### Example Input

```text
(a OR b OR NOT u) AND (NOT a OR u) AND (b OR u)
```

### Example Output

```text
====================================================================================================
Solution Found
	█ Variables: {'a': True, 'b': False, 'u': True}
	█ Solution Found At Iteration: 15
```

---

## Key Features of the Algorithm

-   **Local Minima Handling**:
    -   Detects when the algorithm is stuck in a local minimum and restarts from a random state.
-   **Flat Region Detection**:
    -   Identifies regions where no improvement is possible and restarts from a random state.

---

## Educational Context

This project is developed as part of the **Advanced Design of Algorithms** course at Ferdowsi University of Mashhad (FUM). The project is supervised by **Dr. Naghibzadeh**.

### Contributors

-   **Mohsen Gholami Golkhatmi**
-   **Behnam Akbari**

---

## Notes

-   The program assumes that the input formula is in valid CNF format. Ensure proper syntax when entering the formula.
-   For debugging or detailed analysis, enable the `deep_log` flag in the code.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

---

## Contact

For any questions or issues, feel free to contact the contributors:

-   **Mohsen Gholami Golkhatmi**: iMohsen2002@gmail.com
