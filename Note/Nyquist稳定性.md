# NYQUIST STABILITY CRITERION
# Nyquist稳定性判据
---
## 定义

对于一个开环传递函数$G(s)$，其Nyquist曲线是其频率响应曲线$G(j\omega)$在复平面上的轨迹。Nyquist稳定性判据是通过Nyquist曲线的形状来判断系统的稳定性。

令
$$
\begin{aligned}
G(s) &= \frac{N_G}{D_G}\\
H(s) &= \frac{N_H}{D_H}\\
G(s)H(s) &= \frac{N_GN_H}{D_GD_H}\\
1+G(s)H(s) &= \frac{D_GD_H+N_GN_H}{D_GD_H}\\
\frac{G(s)}{1+G(s)H(s)} &= \frac{N_GD_H}{D_GD_H+N_GN_H}
\end{aligned}
$$
结论1：$G(s)H(s)$的极点和$1+G(s)H(s)$的极点相同。$\frac{G(s)}{1+G(s)H(s)}$的极点与$1+G(s)H(s)$的零点相同。

## 柯西辐角定理
结论：s平面内顺时针画一条闭合曲线A，B曲线是A通过F(s)后F(s)平面上的映射。A曲线包含一个F(s)的零点，。B曲线就绕(0,0)点顺时针一圈。A曲线包含一个F(s)的极点B曲线就绕(0,0)点逆时针一圈。

## Nyquist稳定性判据推导
$$
P - Z = N
$$
其中P是$1+G(s)H(s)$的极点个数，Z是$1+G(s)H(s)$的零点个数，N是B Contour的逆时针绕原点的圈数。
