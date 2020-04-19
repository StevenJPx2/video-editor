import math

# t - current time
# b - start value
# c - change in value
# d - duration


def linear(t, b, c, d):
    "simple linear tweening - no easing, no acceleration"
    return (c * t / d) + b


# Quadratic


def ease_in_quad(t, b, c, d):
    "easing in quadratic"
    t /= d
    return (c * t * t) + b


def ease_out_quad(t, b, c, d):
    "easing in quadratic"
    t /= d
    return -c * t * (t - 2) + b


def ease_in_out_quad(t, b, c, d):
    "easing in quadratic"
    t /= d / 2
    if t < 1:
        return (c / 2 * t * t) + b
    t -= 1
    return (-c / 2) * (t * (t - 2) - 1) + b


# Cubic


def ease_in_cubic(t, b, c, d):
    "easing in cubic"
    t /= d
    return (c * t * t * t) + b


def ease_out_cubic(t, b, c, d):
    "easing out cubic"
    t /= d
    t -= 1
    return c * (t * t * t + 1) + b


def ease_in_out_cubic(t, b, c, d):
    "easing in out cubic"
    t /= d / 2
    if t < 1:
        return (c / 2 * t * t * t) + b
    t -= 2
    return (c / 2) * (t * t * t + 2) + b


# Quartic


def ease_in_quartic(t, b, c, d):
    "easing in quartic"
    t /= d
    return c * t * t * t * t + b


def ease_out_quartic(t, b, c, d):
    "easing out quartic"
    t /= d
    t -= 1
    return -c * (t * t * t * t - 1) + b


def ease_in_out_quartic(t, b, c, d):
    "easing in out quartic"
    t /= d / 2
    if t < 1:
        return (c / 2 * t * t * t * t) + b
    t -= 2
    return (-c / 2) * (t * t * t * t - 2) + b


# Quintic


def ease_in_quintic(t, b, c, d):
    "easing in quintic"
    t /= d
    return c * t * t * t * t * t + b


def ease_out_quintic(t, b, c, d):
    "easing out quintic"
    t /= d
    t -= 1
    return c * (t * t * t * t * t + 1) + b


def ease_in_out_quintic(t, b, c, d):
    "easing in out quintic"
    t /= d / 2
    if t < 1:
        return (c / 2 * t * t * t * t * t) + b
    t -= 2
    return (c / 2) * (t * t * t * t * t + 2) + b


# Sinusoidal


def ease_in_sine(t, b, c, d):
    return -c * math.cos(t / d * (math.pi / 2)) + c + b


def ease_out_sine(t, b, c, d):
    return c * math.sin(t / d * (math.pi / 2)) + b


def ease_in_out_sine(t, b, c, d):
    return -c / 2 * (math.cos(math.pi * t / d) - 1) + b


# Exponential


def ease_in_expo(t, b, c, d):
    return c * math.pow(2, 10 * (t / d - 1)) + b


def ease_out_expo(t, b, c, d):
    return c * (-math.pow(2, -10 * t / d) + 1) + b


def ease_in_out_expo(t, b, c, d):
    t /= d / 2
    if t < 1:
        return c / 2 * math.pow(2, 10 * (t - 1)) + b
    t -= 1
    return c / 2 * (-math.pow(2, -10 * t) + 2) + b


# Circular


def ease_in_circ(t, b, c, d):
    t /= d
    return -c * (math.sqrt(1 - t * t) - 1) + b


def ease_out_circ(t, b, c, d):
    t /= d
    t -= 1
    return c * math.sqrt(1 - t * t) + b


def ease_in_out_circ(t, b, c, d):
    t /= d / 2
    if t < 1:
        return -c / 2 * (math.sqrt(1 - t * t) - 1) + b
    t -= 2
    return c / 2 * (math.sqrt(1 - t * t) + 1) + b
