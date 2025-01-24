## What is the Black-Scholes Model?

The Black-Scholes model, developed by Fischer Black and Myron Scholes, is a mathematical model used to estimate the theoretical price of European options. It assumes that the price of the underlying asset follows a geometric Brownian motion with constant volatility and no arbitrage opportunities.

The model is widely used in finance to:

- Calculate the fair price of call and put options.
- Assess the sensitivity of option prices to various factors (option greeks).
- Understand market behaviour and risk management.

### Black-Scholes Formula

The formulas for the price of European call and put options are as follows:

### Black-Scholes Formula

The formulas for the price of European call and put options are as follows:

#### Call Option Price:
\[
C = S N(d_1) - K e^{-rT} N(d_2)
\]

#### Put Option Price:
\[
P = K e^{-rT} N(-d_2) - S N(-d_1)
\]

Where:

- \( S \): Current stock price
- \( K \): Strike price
- \( T \): Time to maturity (in years)
- \( r \): Risk-free interest rate (annualised)
- \( \sigma \): Volatility of the stock (annualised)
- \( N(x) \): Cumulative distribution function of the standard normal distribution

Intermediate terms:

\[
d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}
\]
\[
d_2 = d_1 - \sigma\sqrt{T}
\]


### Option Greeks

The Black-Scholes model also provides the foundation for calculating option greeks, which measure the sensitivity of option prices to various factors:

- **Delta (Δ):** Sensitivity of the option price to changes in the underlying asset price.
- **Gamma (Γ):** Rate of change of delta with respect to the underlying asset price.
- **Vega (ν):** Sensitivity of the option price to changes in volatility.
- **Theta (Θ):** Sensitivity of the option price to the passage of time.
- **Rho (ρ):** Sensitivity of the option price to changes in the risk-free interest rate.
