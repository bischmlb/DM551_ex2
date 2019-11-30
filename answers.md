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
set with n distinct elements
n = 2^k for k > 0

```py
def randperm(S):
    X_1 = {}
    X_2 = {}
    if p > 0:
        X_1 = A(S)
        X_1 = randperm(X_1)
        for i in S:
            if i not in X_1:
                X_2.append(i)
        X_2 = randperm(X_1)
        return X_1X_2
    if p = 0:
        return S[0]
    else:
        return error
```


b)


c)



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
