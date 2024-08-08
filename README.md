# Overview
The focus of this study is to report the performance of Upper Confidence Bound (UCB) and discounted UCB with different choices of the discount factor (γ).

## Theoretical Aspect of the Effect of γ

In discounted UCB, recent and previous observations are weighted differently based on the discount factor γ. The weight for an observation decreases as it gets further in the past. This is represented by the term γ<sup>t−j</sup>, which is large when j is close to t, meaning recent observations significantly affect the estimate μ̂. Conversely, past observations far from the present time sequence t have minimal impact.

- **γ close to 1**: Minimal discounting of past observations, equivalent to standard UCB.
- **γ close to 0**: Significant discounting, primarily considering only the most recent observation.

When the environment changes suddenly after a time step T/2, relying on previous observations becomes less effective. Thus, a properly chosen γ in discounted UCB can outperform standard UCB by reducing dependence on outdated observations.

## Empirical Aspect of the Effect of γ

Empirical results show that:

- UCB exhibits the highest cumulative regret.
- Discounted UCB generally shows lower regret.
- The performance difference between γ = 0.1 and γ = 0.5 is not substantial.
- γ = 0.9 leads to higher cumulative regrets compared to the other two values of γ.

Given the sudden change in the reward function after T/2, past observations become less relevant, making discounted UCB a better choice than UCB. However, γ = 0.9 might be too large as it overly relies on past observations.

---

# Results

## Cumulative Regret of UCB and Discounted UCB

The table below summarizes the cumulative regrets for UCB and discounted UCB with different γ values across multiple trials.

| Trial | UCB | DUCB (γ = 0.1) | DUCB (γ = 0.5) | DUCB (γ = 0.9) |
|-------|:---:|:--------------:|:--------------:|:--------------:|
| 1     | <div align="center">11</div> | <div align="center">3</div> | <div align="center">4</div> | <div align="center">6</div> |
| 2     | <div align="center">37</div> | <div align="center">3</div> | <div align="center">2</div> | <div align="center">6</div> |
| 3     | <div align="center">59</div> | <div align="center">4</div> | <div align="center">2</div> | <div align="center">7</div> |
| 4     | <div align="center">8</div> | <div align="center">3</div> | <div align="center">2</div> | <div align="center">3</div> |
| 5     | <div align="center">12</div> | <div align="center">2</div> | <div align="center">2</div> | <div align="center">7</div> |

## Cumulative Regret Plots

- **Figure 1**: Cumulative Regret of UCB

![Cumulative Regret of UCB](https://github.com/neurokimchi/discountedUCB/blob/master/figures/fig1.png)

- **Figure 2**: Cumulative Regret of Discounted UCB with different γ values:

  - (a) γ = 0.1
  
  ![Cumulative Regret of DUCB (γ = 0.1)](https://github.com/neurokimchi/discountedUCB/blob/master/figures/fig2.png)
  
  - (b) γ = 0.5
  
  ![Cumulative Regret of DUCB (γ = 0.5)](https://github.com/neurokimchi/discountedUCB/blob/master/figures/fig3.png)
  
  - (c) γ = 0.9
  
  ![Cumulative Regret of DUCB (γ = 0.9)](https://github.com/neurokimchi/discountedUCB/blob/master/figures/fig4.png)

---

# Conclusion

The results suggest that discounted UCB with a properly chosen γ can significantly reduce cumulative regret compared to standard UCB, especially in environments with sudden changes.
