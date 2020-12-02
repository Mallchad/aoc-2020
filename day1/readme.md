## Day-1 Solution Explanation

### Part-1

You are given a list of integers as the input. You need to find two elements that sum to 2020 and report their product.

So a classic brute-force approach would work for this problem. Just run two `for` loops over the input and check whether they sum up to 2020, if they do then just
return their product. That solves Part-1 of day-1 and on to Part-2

---

### Part-2

The input of the Part-2 is the same as before but now you need to find three such elements that sum to 2020 and report their product.

At first I felt like the brute-force solution might take more time to run. But I just implemented it since it was just an addition of one line to the previous code.
And it actually worked the input was small enough to produce the result instantly. So the approach was to run three `for` loops over the input and check whether they sum 
to 2020, if they do return their product. This concludes day-1.

---

### Optional

Now lets see if we can solve this even more faster. The part-1 solution right now is `O(N^2)` time comlexity and part-2 is `O(N^3)` time complexity. Can we do better? Yes, if we
employ a method called hashing we can make part-1 take `O(N)` time complexity and part-2 take `O(N^2)` time complexity.

So what we do is we push all the elements of the input to hash-table in python a `set`. For part-1 we traverse the input and check if `2020-el` is present in the set
, if yes then `el * 2020-el` would be our answer. For part-1 we use two for loops to traverse two elements at a time and check if `2020-first-second` is present in the
set, if yes then `first * second * 2020-first*second` would be our answer.

Now how does this reduce time complexity? It is because the searching for the `2020-el` in the part-1 and `2020-first-second` in the part-2 take O(1) time.

---

### Code

You can check the source code file `day1.py` for the implementation details. Only the brute force ones are implemented. The optional is for knowledge purpose.
