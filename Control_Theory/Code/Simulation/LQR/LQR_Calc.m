clear all;
clc;
A = [0 1; 10 0];
B = [0; -1];
Q = [1 0; 0 1];
R = 100;
K = lqr(A, B, Q, R)
