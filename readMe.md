# From Iterative to Recursive:  Floyd-Warshall Algorithm 

## Solve All Pairs Shortest Path (APSP) problems

### Given edge-weighted and directed graphs

<jgray.7@liverpool.ac.uk>

```bash
pip install -r requirements.txt
```
### Given a matrix

```python
graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]
```
### Run floydIterative.py or floydRecursive.py to generate equivalent Solution Matrix
### Both files return overall performance or duration times in seconds

```python
graph = [[0, 7, 12, 8],
         [noPath, 0, 5, 7],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]
```
### Run testFloyd.py to perform three unit tests with successful test as follows

```python
---------------------
(1) Given graph:
[[0, 7, inf, 8], [inf, 0, 5, inf], [inf, inf, 0, 2], [inf, inf, inf, 0]]
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
```