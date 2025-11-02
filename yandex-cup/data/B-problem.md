## Hills, Greeks, Gags (Горки, греки, гэги)

**Time Limit:** 1 second  
**Memory Limit:** 256 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

As is known, in Ancient Greece the foundations of philosophy were laid, thanks to which, in particular, the concept of science was formalized. Mathematics was considered one of the main sciences of that time: Pythagoras, Euclid, Archimedes — you've definitely heard these names!

Even such outstanding scientists sometimes have to come down from heaven to earth and ask architects to build buildings for their schools. Architects are people of an engineering mindset, and therefore here and there they encounter problems related to mathematics.

They have n building blocks standing on a straight line. Block number i has height h*i; the length and width of all blocks are considered to be one unit. We call a **hill** a continuous subsequence from the l-th to the r-th block such that there exists m: l < m < r and h_l < h*{l+1} < ... < h*m > h*{m+1} > ... > h_r.

The architects need to know how many hills exist in this sequence of blocks.

### Input Format

- First line contains integer t (1 ≤ t ≤ 100) — the number of test cases.
- Next (2·t) lines describe the test cases.
- First line of each test case contains integer n (1 ≤ n ≤ 2·10⁵) — the number of blocks.
- Second line of each test case contains n integers h₁, h₂, ..., h_n (1 ≤ h_i ≤ 10⁹) — the heights of the blocks.

It is guaranteed that Σn ≤ 2·10⁵.

### Output Format

For each test case, output one integer — the number of hills in the sequence of blocks.

### Example

**Input:**

```
5
5
1 2 3 2 1
1
1000000000
1
1
6
1 2 3 3 2 1
10
1 5 8 4 6 3 8 10 14 7
```

**Output:**

```
4
0
0
0
6
```
