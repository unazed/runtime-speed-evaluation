# runtime-speed-evaluation
visualize runtime execution times for arbitrary functions against other functions


Ever wanted to compare function execution speeds in Python? With this tool, albeit with a bit of time to set it up, you can easily contrast differences and decide whether one function is more optimal (in terms of efficiency/speed) than another.

For (a bad) example, comparing two completely random functions I found on the internet which have no textual relation, besides the context which is prime generation.

![](https://i.imgur.com/ElJ0Jnq.png)

An obvious detail to notice is that when it does an exponential curve like that, it means that the function is, obviously, working harder on the dataset with the ever-growing iteration cycle; which is a bit of a misleading name because it really just is the `x` in `f(x)`, just a value that's substituted into the functions using the special replacement string so that the graph can actually be usable.

A completely useless debugging note is that when both functions produce a line scoring across the top, middle or bottom; it probably means you forgot to put the special replacement strings inside.
Here's the full output & configuration I had set up to produce that graph:

```
{*} How many functions would you like to compare? 2
{*} What is the unique replacement string? %%%
{*} What should be the starting integer? 1
{*} What should be the ending integer? 100
{*} How many times should it run? 100
{*} How many times should each function run individiually? 10
Setup (run once) {0} 
Code {0} r=range(2,%%%);[x for x in r if sum(x%d<1 for d in r)<2]               
Color {0} red          
Setup (run once) {1} 
Code {1} r=range(2,%%%);m=[x*y for x in r for y in r];[x for x in r if not x in m]
Color {1} green
```
