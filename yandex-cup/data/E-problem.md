## The Legend of Icarus (Легенда об Икаре)

**Time Limit:** 2 seconds  
**Memory Limit:** 256 MB  
**Input:** standard input  
**Output:** standard output

### Problem Statement

**This is an interactive problem.**

To escape from the island of Crete and avoid the wrath of the angry Minos, the master Daedalus made wings for his son Icarus, held together with wax. Daedalus warned Icarus: "Don't fly too high; the sun will melt the wax. Don't fly too low; the sea water will wet the feathers."

Formally, Icarus's flight obeys the following rules:

1. If Icarus is at height H and H < N, sea water will get on his wings;
2. If Icarus is at height H and N ≤ H < M, sea water will not get on his wings, and the sun will not melt the wax;
3. If Icarus rises above M, the wax will immediately melt, and he will fall, which is unacceptable;
4. It is known that (M - N) > N.

Your task is to help Icarus find the height N — the minimum height at which sea water will not wet Icarus's wings. Icarus has no more than 200 attempts to find height N, but each attempt must not be higher than M.

It is known that 1 ≤ N ≤ M ≤ 10¹⁸.

### Interaction Protocol

To make queries, the program must use standard output.

Your program should output queries — integers h_i (1 ≤ h_i ≤ 10¹⁸) one per line. After outputting each line, the program must perform a "flush" operation.

The input data will contain answers to queries, i.e., strings of the form "wet", "ok", or "fail". The i-th of these strings is the result of Icarus rising to height h_i.

1. If h_i < N, the input will contain the string "wet";
2. If N ≤ h_i ≤ M, the input will contain the string "ok";
3. If h_i > M or the number of queries exceeded 200, the input will contain the string "fail".

After the program reads "fail", it must immediately terminate.

When your program has found the number N, output a string of the form "! N" (without quotes), where N is the answer, and terminate the program.

### Example

**Input/Output:**

```
8
wet
11
ok
9
wet
10
ok
! 10
```
