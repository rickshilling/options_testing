import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random
from functools import partial

key = random.key(0)

def K_S(S):
    K_S = (S(1)-S(0))/S(0)
    return K_S

def K_A(A):
    K_A = (A(1)-A(0))/A(0)
    return K_A

def V(x,S,y,A,t):
    return x*S(t)+y*A(t)
