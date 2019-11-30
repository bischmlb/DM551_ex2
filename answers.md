### 1

a)

We have n different coupons, and we pick 2 of those each time. The probability of getting 1 new coupon is (n-i)/n. But since we only make progress if we get 2 new coupons, the probability of making progress, hence having i+2 coupons after the next step, will, assuming we always collect two different coupons be:

```((n-i)/n) * (n-(i-1))/n```


b)


c)
Let R be a random variable that indicates number of trials until success.


***


### 2

a)
13.4 om MAX 3-SAT


b)
Further analysis .. 13.15

c)


d)




***


### 3

a)


```py
def randperm(S):
    if p > 0:
        X_1 = A(S)
        for i in S:
            if i not in X_1:
                X_2.append(i)
        randperm(X_1)
        randperm(X_2)
        return X_1 ++ X_2
    if p == 0:
        return S[0]
```


b)  
First we need a base case, suppose the scenario for **k = 1**    
This means the size of S will be 2^1, so p = 1.  
When we enter RANDPERM the algorithm will recognize p > 0, because p = 1.  
It will call A on the given set S and generate a random subset X_1 of size 2^p-1, in this case 2^0, which will give us a subset X_1 with 1 element. X_2 will be the remaining element, that is not in X_1.  
X_1 and X_2 will be returned with 1 element in each. Example input could be {a,b} with outcome {b, a} where b is the random permutation X_1 of S, and a is the random permutation X_2 of S.  

Now we assume the same for k = **k+1.**  
The size of S is 2^k, so p = **k.**  
RANDPERM will again recognize p > 0, because p = k  
A will give us a random subset X_1 of S of size 2^k-1, and X_2 will be the remaining elements in S, that are not in X_1.
Finally we will return subset X_1 and X_2, both of size 2^k-1.

Should the size of the set S be 1, it will mean that we have a set size of 2^0, because 2^0 = 1, which means we will return the only element in the set, because p = k = 0.

We will assume that the algorithm works correctly for all k > 0.



c)  
If we were to implement A, we would simply pick r random elements from a set S. However, each time we pick an element, we would have to make sure, that the newly picked element, has not already been picked, else we would end up with duplicates in the returned subset. Elements are appended to the new subset as they are picked, given that they are of course not picked already.  
We should keep some kind of tracker, very suitingly r, which should be decremented everytime we append an element.     
The process of picking the elements could be done in a while loop, which would not break until r = 0.
Once r elements have been picked with no duplicates, we will check if the subset of the currently r picked elements has length S/2.  
The reason why A will always return a subset of size S/2, is because we suppose that A always takes sets containing 2r elements. So, if we pick r elements, A will return **S/2 = r elements**, because S/2 is always the value of r.

As an example, suppose we have S = {"a","b","c","d","e","f"}. The size of S = 6 = 2*3, which means that r = 3. A will randomly pick 3 elements one by one, as long as r > 0 and decrement the value of r by 1, each time it appends an element to the subset we wish to generate. First it picks "c", checks if "c" is already in the subset, and appends. Then it could pick "d", and then "a". The loop will break, because r = 0, giving us the subset subsetS = {"c","d","a"} and we return. Should we instead of "d" have picked "c" again, the algorithm would not decrement r, and instead pick a new element from S, and repeat.
We will not care about inputs with uneven amounts of elements, but we could throw some kind of exception, if this would be the case.



***


### 4

a)  
Each ball has 1/m chance of ending up in any given box, and the probability wont change based on the outcome of the other balls.
The expected number of balls in a fixed box i is
```n*(1/m)``` = ```n/m``` = ```m^2/m``` = ```m```



b)
V(X) = E(X^2) - (n/m)^2
V(X) =  
https://www.slader.com/textbook/9781259676512-discrete-mathematics-and-its-applications-8th-edition/519/exercises/38/#


c)


d)


e)



***


### 5

a)
In order to find the maximum flow using the Edmonds-Karp algorithm, we will have to find the bottleneck values. This is done by finding every augmenting path from ```s -> t``` using Breadth-First Search (BFS).  
When no more augmenting paths are left, we can sum the bottleneck values to see the max flow. Also this can be verified by summing the capacity values going into the sink **t**.

For this exercise, we will find every path with length 2,3 ..n until we have no more possible paths.
We will be adding each possible vertice with ```capacity > 0``` from **s** towards **t**, continuing until there are no more possible vertices and we reach the sink **t**.  
```
length 2 shortest paths:
path  |  augmentation
s14t  |  4  
s25t  |  8
s26t  |  7
s35t  |  1
s36t  |  2

length 3 shortest paths:
s314t  |  1
s315t  |  3

length 4 shortest paths:
s3156t  |  5
```

![graph](residualgraphs.png)

We stop finding augmenting paths, because are no more possible augmenting paths from s -> t.

We can now see that, our max flow ```f*``` is  
```12 + 15 + 4 = 31```



b)
First we find the set of reachable vertices from the source:
Set of reachables **R_v** vertices = {3, 1, 2, 5, t}.
Now we can find the all the minimum cut arcs, which are the arcs that are from a reachable vertex to a non reachable vertex. Such arcs are: A(3,6) = 2, A(1,4) = 5, A(2,6) = 7, A(5,6) = 5, A(5,t) = 12. We make the cuts.  

![minimum cut](minimumcut.png)

This means that our minimum cut capacity is
```2 + 5 + 7 + 5 + 12 = 31 = f*```

c)

Using our final residual graph, we can see that we will get the maximum flow ```4 + 15 + 13 = 32``` because we will be able to augment path ```s315t``` by 1. This means that vertices 1,2 and 5 will no longer be reachable, and we cut:

![](questionc.png)

Our new minimum cut capacity therefore is:
```4 + 15 + 2 + 1 + 10 = 32```, which is similar to the max flow.




***
