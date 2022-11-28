# Floyd Warshall Algorithms(matrixIterative and Recursive)

## Solve All Pairs Shortest Path (APSP) problems

### Given edge-weighted and directed graphs

### Contents

<jgray.7@liverpool.ac.uk>

1. Install requirements.txt
2. Run either file to return solution matrix
3. Run tests to check solutions specifically and overall

```python
pip install -r requirements.txt
```
### Given a matrix

```python
graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]
```
### Running file floydRecursive.py returns shortest paths, if any
### Note update in pair 0,2 from noPath to 12; and
### Note update in pair 1,3 from noPath to 7

```python
graph = [[0, 7, 12, 8],
         [noPath, 0, 5, 7],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]
```
