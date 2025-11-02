## Easter Island Statues (Статуи острова Пасхи)

**Time Limit:** 1 second  
**Memory Limit:** 256 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

The main attraction of Easter Island is n stone statues. The island's inhabitants are very proud of them and want all of them to be visible from the sea, from whichever side a ship approaches.

The inhabitants marked the island's territory into n horizontal and n vertical rows and numbered the horizontal rows from 1 to n from north to south, and the vertical rows from 1 to n from west to east. It turned out that the i-th statue is located in the cell at the intersection of horizontal row r_i and vertical row c_i. Several statues can be located in the same cell.

For all statues to be visible from ships arriving from the west or east, they must all be placed in different horizontal rows. Similarly, for all statues to be visible from ships arriving from the north or south, they must all be placed in different vertical rows.

In one day, the island's inhabitants can move any one statue to a cell adjacent by side to the current one. Help them determine the minimum number of days needed to arrange the statues so that they are all in different horizontal and vertical rows.

### Input Format

- First line contains integer n (1 ≤ n ≤ 10⁵) — the number of statues.
- Next n lines describe the initial position of the statues. Each contains integers r_i and c_i (1 ≤ r_i, c_i ≤ n) — the numbers of the horizontal and vertical rows at whose intersection the statue is located.

### Output Format

Output one integer — the minimum number of days for the island's inhabitants to arrange the statues so that no two of them are in the same horizontal or vertical row.

### Examples

**Input:**

```
3
1 2
1 3
3 3
```

**Output:**

```
3
```

**Input:**

```
5
3 2
5 4
1 3
2 3
1 2
```

**Output:**

```
6
```
