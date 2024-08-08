# Overview
This repository contains the implementation and performance analysis of various bandit algorithms. The study involves:

1. Explore-then-Commit
2. Upper Confidence Bound (UCB)
3. Thompson Sampling
4. Linear UCB (LinUCB)
5. Linear Thompson Sampling (LinTS)
6. Non-linear Bandits (Bonus)

## 1. Explore-then-Commit
### Result
<div align="center">
  
| Hyperparameter (m) | Cumulative Regret |
|:------------------:|:-----------------:|
|         10         |      1001.40      |
|         20         |       214.90      |
|         30         |       334.02      |

![Explore then Commit accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig1.png)

</div>

## 2. Upper Confidence Bound (UCB)
### Reward Estimation + Confidence Bound
$$
\text{UCB} = \hat u_{t-1,i} + \sqrt{\frac{2 \ln t}{S_{t-1,i}}}
$$

### Result
<div align="center">
  
| Hyperparameter (α) | Cumulative Regret |
|:------------------:|:-----------------:|
| 0.1                | 256.50            |
| 0.5                | 977.03            |
| 1.0                | 1906.65           |

![UCB Bandit accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig2.png)

</div>

## 3. Thompson Sampling
### Posterior Distribution

$$
N \sim \left( \hat u_{t-1,i}, \frac{1}{S_{t-1,i} + 1} \right)
$$

### Result

<div align="center">

| Cumulative Regret |
|:------------------:|
|  100              |

![Thompson Sampling accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig3.png)

</div>

## 4. Linear UCB (LinUCB)
### Parameter Estimation

$$
\hat \theta_{t+1} = A^{-1}_ {t+1} b_{t+1}
$$

### Reward Estimation + Confidence Bound

$$
\text{UCB} = x^T \hat \theta_t + \alpha \sqrt{x^T A^{-1} x}
$$

### Result

<div align="center">

| Hyperparameter (α) | Cumulative Regret |
|:------------------:|:-----------------:|
| 0.5                | 24.43             |
| 1.5                | 177.89            |
| 2.5                | 487.73            |

![Linear UCB accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig4.png)
![Linear UCB estimation error](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig5.png)

</div>

## 5. Linear Thompson Sampling (LinTS)
### Posterior Distribution
$$
N \sim (\hat{\theta}_t, A^{-1}_t)
$$

### Result

<div align="center">

| Cumulative Regret |
|:------------------:|
| 1098.24            |

![Linear Thompson Sampling accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig6.png)
![Linear Thompson Sampling estimation error](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig7.png)

</div>

## 6. Generalized Linear Model (GLM) Bandits: Non-linear Bandits
### Modified Non-LinearReward Function For Testing

$$
R = (x^T \theta)^2 + \epsilon, \text{ where } \epsilon \sim N(\mu, \sigma^2)
$$

### GLM Parameter Estimation (MLE)

$$
\hat \theta_{t+1} = \max_{\theta} P(r|\theta) = A^{-1}_ {t+1} b_{t+1}
$$

### GLM UCB

$$
UCB_{GLM} = f(x^T \hat \theta_t) + \alpha \sqrt{x^T A^{-1} x} = (x^T \hat \theta_t)^2 + \alpha \sqrt{x^T A^{-1} x}
$$

### Result

<div align="center">

| Hyperparameter (α) | Cumulative Regret |
|:------------------:|:-----------------:|
| 0.1                | 62.16             |
| 0.5                | 727.63            |
| 1.5                | 5948.48           |

![GLM-UCB accumulated regret](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig8.png)
![GLM-UCB estimation error](https://github.com/neurokimchi/comparison-bandits/blob/master/figures/fig9.png)

</div>

