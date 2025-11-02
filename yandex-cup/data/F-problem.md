## Sequence (Последовательность)

**Time Limit:** 5 seconds  
**Memory Limit:** 1024 MB  
**Input:** standard input  
**Output:** standard output

**Subtask:** A solution correctly working within constraints 1 ≤ n ≤ 10³ and 1 ≤ q ≤ 10³ will be awarded 2 points.

**Full solution:** working within the constraints described in the input format will be awarded 10 points (including 2 points for the subtask above).

### Problem Statement

Developer Vlad didn't maintain work-life balance and worked too much. His friends were very worried about this and decided to organize a joint vacation. Vlad didn't want to spend much time and therefore agreed to go somewhere only near the office. The choice fell on an exhibition of famous abstractionists, which was held at the "Garage" Museum of Contemporary Art.

At the exhibition, Vlad was greatly impressed by Kandinsky's work. Standing before the painting "Sequence" (1935), he told his friends: "Oh, I can do that too!" This idea wouldn't let him go, and returning home in the evening, he began working on his version of the painting.

Vlad prepared a black-and-white sketch of the future painting. The sketch consists of q different elements that need to be colored. To give originality to his work, Vlad decided to choose colors algorithmically. He knew that in the nearest paint store on the counter there are always n paints of different shades. Each color has its own unique identifier. Vlad didn't want to go to the store several times, so he prepared q pairs of numbers (l_i, r_i) in advance, with which he wanted to determine the color of the i-th fragment of the painting using some formula.

He settled on the following formula. Let the set M = {a*i & a*{i+1} & ... & a_j | l ≤ i ≤ j ≤ r}, where x & y means bitwise AND of numbers x and y. Then the value of the identifier itself is MEX(M).

### Input Format

- First line contains one integer n (1 ≤ n ≤ 2·10⁵) — the number of paints in the store.
- Second line contains n numbers a₁, a₂, ..., a_n (0 ≤ a_i < 2⁶⁰) — the sequence of paint colors in the store.
- Third line contains one integer q (1 ≤ q ≤ 10⁶) — the number of painting fragments.
- Next q lines each contain two integers l and r (1 ≤ l ≤ r ≤ n) — the formula parameters for calculating the color of the i-th painting fragment.

### Output Format

For each painting fragment, output one integer — the color identifier to paint it with.

### Examples

**Input:**

```
6
2 1 3 7 15 31
10
1 5
2 6
1 3
2 5
3 4
2 2
1 6
2 6
3 6
2 4
```

**Output:**

```
4
0
4
0
0
0
4
0
0
0
```

**Input:**

```
5
1 2 3 4 5
15
1 1
1 2
1 3
1 4
1 5
2 2
2 3
2 4
2 5
3 3
3 4
3 5
4 4
4 5
5 5
```

**Output:**

```
0
3
4
5
6
0
0
1
1
0
1
1
0
0
0
```

### Note

MEX of a set of numbers is the minimum non-negative integer not contained in this set. For example, MEX({0, 2, 3}) equals 1, and MEX({5, 2, 1}) equals 0.
