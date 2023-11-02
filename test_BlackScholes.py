import pytest
from BlackScholes import BS_option, BS_imply_volatility, ncdf_delta
from math import exp, sqrt, pi

def test_call_put():
    call_atm = BS_option(100, 100, 1, 0, 0.3, 'C')
    put_atm = BS_option(100, 100, 1, 0, 0.3, 'P')
    assert call_atm[0] == put_atm[0]  # put = call for ATM option when
    assert call_atm[1] - put_atm[1] == 1
    assert call_atm[2] == put_atm[2]   # same gamma for call and put
    assert call_atm[4] == put_atm[4]   # same vega for call and put
    assert call_atm[3] <= 0
    assert put_atm[3] <= 0
    assert abs(call_atm[0] - put_atm[0] - 100 + 100 * exp(-0.00*1)) < 1e-9

def test_call_put_parity():
    call_atm = BS_option(100, 120, 1, 0.05, 0.5, 'C')
    put_atm = BS_option(100, 120, 1, 0.05, 0.5, 'P')
    assert call_atm[1] - put_atm[1] == 1
    assert call_atm[2] == put_atm[2]   # same gamma for call and put
    assert call_atm[4] == put_atm[4]   # same vega for call and put
    assert call_atm[3] <= 0
    assert put_atm[3] <= 0
    assert abs(call_atm[0] - put_atm[0] - 100 + 120 * exp(-0.05*1)) < 1e-9

def test_BS_imply_volatility():
    call_atm = BS_option(100, 120, 0.5, 0.05, 0.3, 'C')
    assert abs(BS_imply_volatility(100, 120, 0.5, 0.05, call_atm[0], 'C') -0.3) < 1e-4

def test_ncdf_delta():
    assert ncdf_delta(0) == 1/ sqrt(2*pi)