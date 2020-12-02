## Day-1 Solution explanation

### Part-1

This problem tests your string parsing skills. You can do this in multiple ways, I did the hard way. Which includes splitting and indexing of individual strings. We take the input as list of strings where each string is a password for example is of form `1-3 a: abcde`. In part-1 we are needed to check if the count of `a` in the previous example is atleast 1 and atmost 2. So what I did was take the individual password and split it based on space so the example stated before will be split as `['1-3', 'a:', 'abcde']`, which makes it easier since the first letter of the second element of split is the letter we need to check, and the minimum and maximum counts are done using splitting the first element of the split with delimiter `-` so it would become ['1', '3']. Now we just check the condition using an `if` and count them and return the answer. This solves part-1

---

### Part-2

We can use the previous solution and modify the solution a little bit, taking previous example `1-3 a: abcde`, we are needed to check if the atleast one of the `1` and `3` index element must be `'a'` but not both. Here `1` element is `'a'` but `3` is not `'a'`. This is a valid password. Now we are needed to return how many such valid passwords are there in the input. This concludes day2

---

To see the implementation details check the source code in this directory.
