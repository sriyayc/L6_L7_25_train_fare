# L6_L7_25_train_fare — Train Fare

Lab 6: Code and Branch Coverage

## About

A small Python module that works out train base fares by class and distance, applies age concessions and calculates Tatkal charges.

## Files

| File | Description |
|------|-------------|
| `train_fare.py` | The module under test |
| `test_train_fare.py` | Starter test file |

Refer to the lab handout for instructions.

## Coverage Results

| Test file | Tests | Line coverage | Branch coverage |
|-----------|-------|---------------|-----------------|
| `test_train_fare.py` (starter) | 2 | 45% | 40% |
| `CodeCoverageTest_PES2UG24CS523_train_fare.py` | 13 | 100% | 98% (missed `36->38`) |
| `BranchCoverageTest_PES2UG24CS523_train_fare.py` | 31 | 100% | 100% |

The code coverage tests execute every line, but never produce a Tatkal charge
between 100 and 400, so the path where neither the cap nor the minimum applies
(`36->38`) is missed. The branch coverage tests add that case along with boundary
values (ages 5, 12, 13, 60; fare exactly 50; distance <= 0; charge exactly 100/400).

### Commands

```
coverage run -m pytest CodeCoverageTest_PES2UG24CS523_train_fare.py
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_PES2UG24CS523_train_fare.py
coverage report -m
```
