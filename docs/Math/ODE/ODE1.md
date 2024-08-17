## A. 可分离变量方程
$$
\bbox[background: Lightgrey]{\frac{\mathrm{d}y}{\mathrm{d}x}=\varphi(x)\psi(y)}$$
方法：分离变量

$$
\frac{\mathrm{d}y}{\psi(y)}=\frac{\mathrm{d}x}{\varphi(x)}$$
然后积分  

$$
\int\frac{\mathrm{d}y}{\psi(y)}=\int\frac{\mathrm{d}x}{\varphi(x)}$$

!!! warning ""
    当 $\exists y^*$, 使得 $\psi(y)=0$, 则 $y=y^*$ 也是一解
??? example "eg: $\sqrt{1-y^2}dx+y\sqrt{1-x^2}dy=0$"
    $\frac{dx}{\sqrt{1-x^2}}=-\frac{ydy}{\sqrt{1-y^2}}\Rightarrow \arcsin x+c=\sqrt{1-y^2}, \text{ and }y=\pm 1$
## B. 齐次方程
$$
\bbox[lightgrey]{\frac{\mathrm{d}y}{\mathrm{d}x}=g(\frac{y}{x})}$$
方法：

    
