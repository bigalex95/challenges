## Decoding Mayan Code (Расшифровка кода Майя)

**Time Limit:** 3 seconds  
**Memory Limit:** 1024 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

The Maya were one of the most advanced civilizations of Mesoamerica, existing from approximately 2000 BC to 1500 AD. They built incredible cities with impressive architecture, such as Chichen Itza in Mexico. Mayan writing and its decipherment have allowed us to better understand their culture, religion, and way of life.

Decoding Mayan code is complicated by the fact that different tribes have different dialects, making it more difficult to apply techniques such as frequency analysis.

It is known that there were n tribes in total and the tribes form a certain hierarchy. Formally, there are n-1 subordination relationships (u_i, v_i) indicating that tribe v_i is directly subordinate to tribe u_i.

We will consider that tribe a is subordinate to tribe b if for some k ≥ 1 there exists a chain of tribes c₁, c₂, ..., c*k such that a = c₁, b = c_k, and for any 1 ≤ i < k, tribe c_i is directly subordinate to tribe c*{i+1}. It is known that all tribes are subordinate to tribe number 1.

For each tribe i, its sacred word s_i is known. While studying Mayan texts, researchers often found occurrences of sacred words in texts. The researchers have q queries of the following type: For text t_i, how many substrings of this text match the sacred words of tribes subordinate to tribe v_i.

### Input Format

- First line contains two integers n and q (1 ≤ n ≤ 10⁵, 1 ≤ q ≤ 10⁵) — the number of tribes and the number of queries.
- Next n lines each contain one string s_i (1 ≤ |s_i| ≤ 10⁶) — the sacred word of tribe i.
- Next n-1 lines describe subordinations. The i-th of them contains two integers u_i and v_i (1 ≤ u_i ≤ n, 1 ≤ v_i ≤ n), meaning that tribe v_i is directly subordinate to tribe u_i.
- Next q lines describe queries. The i-th of them contains an integer v_i and a string t_i (1 ≤ v_i ≤ n, 1 ≤ |t_i| ≤ 10⁶).

It is guaranteed that Σ|s_i| ≤ 10⁶ and Σ|t_i| ≤ 10⁶.

|s| is the length of string s in characters. All strings consist of uppercase Latin letters.

### Output Format

Output q lines, where the i-th line contains one integer — the answer to the i-th query.

### Examples

**Input:**

```
5 4
A
B
C
D
E
1 2
1 3
1 4
2 5
1 AABCDE
1 A
2 BEE
3 CCCA
```

**Output:**

```
6
1
3
3
```

**Input:**

```
6 4
AA
AB
BC
CD
AA
AA
1 2
2 3
3 4
4 5
5 6
1 AAABCD
2 AABCD
3 BCD
1 DCBA
```

**Output:**

```
9
5
2
0
```

### Note

Sacred words of tribes can match; in the answer to the query, it is necessary to account for occurrences of ALL sacred words. (Example 2).
