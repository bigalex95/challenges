## Two out of Three (Два из трёх)

**Time Limit:** 1 second  
**Memory Limit:** 256 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

The ancient Greek philosopher Pythagoras attached great importance to numbers, considering them the foundation of the world. Numbers possessing certain mathematical properties were ascribed mystical meanings. For example, odd numbers in Pythagoreanism were considered masculine, while even numbers were feminine. Divisibility of a number by others was a significant distinguishing feature for Pythagoras.

Now he is interested in numbers that are sufficiently divisible, but not completely perfect in this regard. For this, he wrote out an increasing sequence of natural numbers divisible by exactly two numbers among three predetermined numbers a, b, and c.

Help Pythagoras find the n-th number in this sequence.

### Input Format

- First line contains integers a, b, c (1 ≤ a, b, c ≤ 10⁶), the divisibility by which Pythagoras checks.
- Second line contains integer n (1 ≤ n ≤ 10¹⁸) — the index of the element in the sequence that Pythagoras wants to find. Elements are numbered starting from one.

### Output Format

Output the n-th natural number divisible by exactly two of the three numbers a, b, c.

If such a number doesn't exist or exceeds 10¹⁸, output −1.

### Examples

**Input:**

```
2 3 5
10
```

**Output:**

```
42
```

**Input:**

```
5 6 7
1000000
```

**Output:**

```
13999986
```

### Note

The sequence of natural numbers divisible by exactly two of the three numbers 2, 3, and 5 looks like this: 6, 10, 12, 15, 18, 20, 24, 36, 40, 42, 45, 48, 50, ... The tenth element of this sequence is 42.
