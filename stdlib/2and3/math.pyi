# Stubs for math
# See: http://docs.python.org/2/library/math.html

from typing import Tuple, Iterable, Optional

import sys

e = ...  # type: float
pi = ...  # type: float
if sys.version_info >= (3, 5):
    inf = ...  # type: float
    nan = ...  # type: float

def acos(x: float) -> float: ...
def acosh(x: float) -> float: ...
def asin(x: float) -> float: ...
def asinh(x: float) -> float: ...
def atan(x: float) -> float: ...
def atan2(y: float, x: float) -> float: ...
def atanh(x: float) -> float: ...
def ceil(x: float) -> int: ...
def copysign(x: float, y: float) -> float: ...
def cos(x: float) -> float: ...
def cosh(x: float) -> float: ...
def degrees(x: float) -> float: ...
def erf(x: float) -> float: ...
def erfc(x: float) -> float: ...
def exp(x: float) -> float: ...
def expm1(x: float) -> float: ...
def fabs(x: float) -> float: ...
def factorial(x: int) -> int: ...
def floor(x: float) -> float: ...
def fmod(x: float, y: float) -> float: ...
def frexp(x: float) -> Tuple[float, int]: ...
def fsum(iterable: Iterable) -> float: ...
def gamma(x: float) -> float: ...
if sys.version_info >= (3, 5):
    def gcd(a: int, b: int) -> int: ...
def hypot(x: float, y: float) -> float: ...
if sys.version_info >= (3, 5):
    def isclose(a: float, b: float, rel_tol: float = ..., abs_tol: float = ...) -> bool: ...
def isinf(x: float) -> bool: ...
if sys.version_info[0] >= 3:
    def isfinite(x: float) -> bool: ...
def isnan(x: float) -> bool: ...
def ldexp(x: float, i: int) -> float: ...
def lgamma(x: float) -> float: ...
def log(x: float, base: float = ...) -> float: ...
def log10(x: float) -> float: ...
def log1p(x: float) -> float: ...
if sys.version_info >= (3, 3):
    def log2(x: float) -> float: ...
def modf(x: float) -> Tuple[float, float]: ...
def pow(x: float, y: float) -> float: ...
def radians(x: float) -> float: ...
def sin(x: float) -> float: ...
def sinh(x: float) -> float: ...
def sqrt(x: float) -> float: ...
def tan(x: float) -> float: ...
def tanh(x: float) -> float: ...
def trunc(x: float) -> int: ...
