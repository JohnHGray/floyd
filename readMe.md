# From Iterative to Recursive:  Floyd-Warshall Algorithm 

## Solve All Pairs Shortest Path (APSP) problems

### Given edge-weighted and directed graphs

### Contents

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
### Solution Matrix

```python
graph = [[0, 7, 12, 8],
         [noPath, 0, 5, 7],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]
```
