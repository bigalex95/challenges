## Similar Civilizations (Подобные цивилизации)

**Time Limit:** 2 seconds  
**Memory Limit:** 256 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

At one of the Ivy League universities, an active anthropological study of the characteristic features of various ancient civilizations has begun.

They took n civilizations and k sets of characteristics — the presence of writing, political structure, religions, types of property, and others.

For convenience, a simulation was created that assigns sets of binary characteristics to civilizations equally probably and independently, i.e., after generation, each civilization corresponds to a binary string ch_i of length k.

The metric that the group monitors is the maximum similarity of the first civilization with some of the remaining n-1 civilizations. Moreover, the researchers are interested in the expected value of such a quantity.

Formally, if we consider the sets of characteristics of n civilizations ch₁, ch₂, ..., ch*n with one distinguished ch₁, then we need to find E[max*{2≤i≤n} sim(ch₁, ch_i)], where sim(a, b) is the number of identical bits in pairwise comparison of a and b, i.e., |{j | a_j = b_j}|.

As one of the group members with an algorithmic background, you were asked to solve this problem. To avoid computational errors, the answer must be found modulo 10⁹+7.

It can be shown that the answer is representable as a fraction P/Q, where P, Q are integers (P > 0, Q > 0), and Q is coprime with modulus 10⁹+7. You need to calculate P·Q⁻¹ modulo 10⁹+7.

### Input Format

The first and only line contains integers n, k (2 ≤ n ≤ 10⁹, 1 ≤ k ≤ 10⁵).

### Output Format

Output a single integer — the answer to the problem modulo 10⁹+7.

### Examples

**Input:**

```
2 10
```

**Output:**

```
5
```

**Input:**

```
3 1
```

**Output:**

```
750000006
```

### Note

In the first example, two civilizations with ten characteristics. The expected value of maximum similarity equals the expected value of similarity — 5.

In the second example, out of 8 possible arrangements of one characteristic across three civilizations, in six cases the maximum similarity is 1, in two cases it's 0. Then the expected value is 6/8.
