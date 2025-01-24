## What is the Black-Scholes Model?

The Black-Scholes model, developed by Fischer Black and Myron Scholes, is a mathematical model used to estimate the theoretical price of European options. It assumes that the price of the underlying asset follows a geometric Brownian motion with constant volatility and no arbitrage opportunities.

The model is widely used in finance to:

- Calculate the fair price of call and put options.
- Assess the sensitivity of option prices to various factors (option greeks).
- Understand market behaviour and risk management.

### Black-Scholes Formula

The formulas for the price of European call and put options are as follows:

#### Call Option Price:

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?C%20%3D%20S%20N%28d_1%29%20-%20K%20e%5E%7B-rT%7D%20N%28d_2%29" alt="Call Option Formula"/>
</p>

#### Put Option Price:

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?P%20%3D%20K%20e%5E%7B-rT%7D%20N%28-d_2%29%20-%20S%20N%28-d_1%29" alt="Put Option Formula"/>
</p>

Where:

- \( S \): Current stock price
- \( K \): Strike price
- \( T \): Time to maturity (in years)
- \( r \): Risk-free interest rate (annualised)
- \( σ ): Volatility of the stock (annualised)
- \( N(x) \): Cumulative distribution function of the standard normal distribution

Intermediate terms:

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?d_1%20%3D%20%5Cfrac%7B%5Cln%28S%2FK%29%20%2B%20%28r%20%2B%20%5Csigma%5E2%2F2%29T%7D%7B%5Csigma%5Csqrt%7BT%7D%7D" alt="d1 Formula"/>
</p>
<p align="center">
    <img src="https://latex.codecogs.com/png.latex?d_2%20%3D%20d_1%20-%20%5Csigma%5Csqrt%7BT%7D" alt="d2 Formula"/>
</p>

<!DOCTYPE html>
<html lang="en">
<body>
    <h2>Option Greeks</h2>
    <ul>
        <li><strong>Delta (Δ):</strong> Sensitivity of the option price to changes in the underlying asset price.</li>
        <li><strong>Gamma (Γ):</strong> Rate of change of delta with respect to the underlying asset price.</li>
        <li><strong>Vega (ν):</strong> Sensitivity of the option price to changes in volatility.</li>
        <li><strong>Theta (Θ):</strong> Sensitivity of the option price to the passage of time.</li>
        <li><strong>Rho (ρ):</strong> Sensitivity of the option price to changes in the risk-free interest rate.</li>
    </ul>
</body>
</html>

### Call-Put Parity

In addition to the Black-Scholes model, call-put parity provides an essential relationship between the prices of European call and put options with the same strike price and expiration date. The call-put parity formula is expressed as:

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?C%20-%20P%20%3D%20S%20-%20K%20e%5E%7B-rT%7D" alt="Call-Put Parity Formula"/>
</p>

Where:

- \( C \): Call option price
- \( P \): Put option price
- \( S \): Current stock price
- \( K \): Strike price
- \( r \): Risk-free interest rate (annualised)
- \( T \): Time to maturity (in years)

This relationship is fundamental in options pricing, ensuring no arbitrage opportunities exist and providing a basis for understanding option valuation in different market conditions.

This project particularly examines the impact of volatility on pricing. 
