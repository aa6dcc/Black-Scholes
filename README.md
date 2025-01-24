## What is the Black-Scholes Model?

The Black-Scholes model, developed by Fischer Black and Myron Scholes, is a mathematical model used to estimate the theoretical price of European options. It assumes that the price of the underlying asset follows a geometric Brownian motion with constant volatility and no arbitrage opportunities.

The model is widely used in finance to:

- Calculate the fair price of call and put options.
- Assess the sensitivity of option prices to various factors (option greeks).
- Understand market behaviour and risk management.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black-Scholes Model</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>Black-Scholes Model</h1>
    <p>The Black-Scholes formula for European call and put options are:</p>
    <h2>Call Option Price</h2>
    <p>
        \( C = S N(d_1) - K e^{-rT} N(d_2) \)
    </p>
    <h2>Put Option Price</h2>
    <p>
        \( P = K e^{-rT} N(-d_2) - S N(-d_1) \)
    </p>
    <h2>Intermediate Terms</h2>
    <p>
        \( d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \)
    </p>
    <p>
        \( d_2 = d_1 - \sigma\sqrt{T} \)
    </p>
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
