# Distributions

## Various Normal Distributions

Basic code for the probability density function of the normal distribution:

```python
def normal_pdf(x, mu=0, sigma=1):
    factor = 1/math.sqrt((2*math.pi*sigma))
    v = -1 * ((x-mu)**2)/(2*sigma**2)
    return factor * math.exp(v)
```


![](https://raw.githubusercontent.com/lexruee/practical-datascience/master/tutorials/distributions/normal-dists.png)
