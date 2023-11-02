from numpy.random import normal
from math import pi, exp, log, sqrt, erf
import numpy as np

sqrt_2pi = sqrt(2*pi)
number_days_per_year = 252 # used for theta calculation
vol_min, vol_start, vol_max = 0.01, 0.4, 10


def ncdf(x):
    """
    Cumulative distribution function for the standard normal distribution
    Requires the error function erf from the math module to avoid import scipy.stats which is not installed by default
    """
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def ncdf_delta(x:float) -> float:
    """
    First derivative of the cumulative distribution function (aka density function)for the standard normal distribution
    """
    return exp(-x**2/2) / sqrt_2pi

def BS_option(S:float, K:float, T:float, r:float, sigma:float, call_put:str) -> tuple:
    sigma_sqrt_t = sigma*sqrt(T)
    d1 = (log(S/K) + (r+0.5*sigma**2)*T)/sigma_sqrt_t
    d2 = d1 - sigma_sqrt_t
    n_d1 = ncdf(d1)
    n_d2 = ncdf(d2)
    n_delta_d1 = ncdf_delta(d1)
    if call_put.upper() in ['C','CALL']:
        price = S*n_d1-K*exp(-r*T)*n_d2
        delta = n_d1
        theta = (-S*n_delta_d1*sigma/(2*sqrt(T))-r*K*exp(-r*T)*n_d2)/number_days_per_year
    else:
        price = K*exp(-r*T)*(1-n_d2) - S*(1-n_d1)
        delta = n_d1 - 1
        theta =  (-S*n_delta_d1*sigma/(2*sqrt(T))+r*K*exp(-r*T)*(1-n_d2))/number_days_per_year
    gamma = n_delta_d1/(S*sigma_sqrt_t)
    vega = S*n_delta_d1*sqrt(T)/100
    return price, delta, gamma, theta, vega

def BS_imply_volatility(S:float, K:float, T:float, r:float, price:float, call_put:str) -> float:
    current_vol = vol_start
    epsilon = 1e-5
    max_counter = 25
    counter = 0
    opt = BS_option(S, K, T, r, current_vol, call_put)
    while abs(price-opt[0]) > epsilon and counter < max_counter:
        current_vol = current_vol + np.clip((price-opt[0])/ np.clip(opt[4], 1e-5, None)/100, - current_vol /2, current_vol /2)
        opt = BS_option(S, K, T, r, current_vol, call_put)
        counter += 1
    return current_vol

class option_bs():
    def __init__(self, S, K, T, r, sigma, call_put):
        if S > 0:
            self.stock = S
        else:
            raise ErrorValue("Stock S must be positive")
        if K >= 0:
            self.strike = np.clip(K,1e-5, None)
        else:
            raise ErrorValue("Strike (exercise price) K must be positive or zero")
        if T >= 0:
            self.maturity_year = np.clip(T,1e-5, None)
        else:
            raise ErrorValue("Maturity (in years) T must be positive")
        self.interest_rate = r
        self._volatility = np.clip(sigma,1e-6, None)
        if call_put.upper() in ['C','CALL']:
            self.call_put = 'C'
        elif call_put.upper() in ['P','PUT']:
            self.call_put = 'P'
        else:
            raise ErrorValue("call_put type is incorrect (must be 'C' or 'P')")

    def __str__(self):
        if self.call_put == 'C':
            opt_type = "Call option"
        else:
            opt_type = "Put option"
        return f"{opt_type} S:{self.stock:,.0f} K:{self.strike:,.0f} T:{self.maturity_year:,.2f} r:{self.interest_rate:.1%} vol:{self.volatility:.1%}"

    @property
    def volatility(self):
        return self._volatility

    @volatility.setter
    def volatility(self, sigma):
        if sigma < vol_min:
            raise ValueError(f"Volatilty must be more than {100*vol_min:,.2f}% or {vol_min:,.4f}")
        elif sigma >= vol_max:
            raise ValueError(f"Volatilty must be less than {100*vol_max:,.2f}% or {vol_max:,.4f}")
        else:
            self._volatility = sigma


    def get_price_and_greeks(self):
        res = BS_option(
            self.stock,
            self.strike,
            self.maturity_year,
            self.interest_rate,
            self.volatility,
            self.call_put
        )
        self.price = res[0]
        self.delta = res[1]
        self.gamma = res[2]
        self.theta = res[3]
        self.vega = res[4]

    def get_volatility_from_price(self, price):
        res = BS_imply_volatility(
            self.stock,
            self.strike,
            self.maturity_year,
            self.interest_rate,
            price,
            self.call_put
        )
        self._volatility = res
        self.get_price_and_greeks()

    def print_greeks(self):
        return f"Price:{self.price:,.2f} Delta:{100*self.delta:,.1f}% Gamma:{self.gamma:,.4f} Theta:{self.theta:.4f} Vega:{self.vega:.3f}"

def create_option_bs_object_from_prompt():
    opt_maturity_str = input("Enter the maturity of the option (in year): ")
    opt_strike_str = input("Enter the exercice price (strike) of the option: ")
    opt_type_str = input("Enter the type of the option ('C' for Call, 'P' for Put): ")
    opt_volatility_str = input("Enter the volatility of the option (in absolute, for 30% enter 0.3): ")
    stock_price_str = input("Enter the price of the underlying stock: ")
    interest_rate_str = input("Enter the interest rate (in absolute, for 5% enter 0.05): ")
    try:
        opt_maturity = float(opt_maturity_str)
        opt_strike = float(opt_strike_str)
        opt_volatility = float(opt_volatility_str)
        stock_price = float(stock_price_str)
        interest_rate = float(interest_rate_str)

        if stock_price> 0 and opt_maturity >0 and opt_volatility> 0 and opt_volatility < 10 and opt_strike>0 and interest_rate < 1 and opt_type_str.upper()[:1] in ['C','P']:
            return option_bs(stock_price, opt_strike, opt_maturity, interest_rate, opt_volatility, opt_type_str.upper()[:1])
        else:
            return None
    except:
        return None


if __name__ == "__main__":
    opt = create_option_bs_object_from_prompt()
    if opt:
        print(f"Description of the option: {opt}")
        opt.get_price_and_greeks()
        print(f"Pricing of the option: {opt.print_greeks()}")
    else:
        print("Wrong inputs")