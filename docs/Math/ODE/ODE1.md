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
方法：令 $u=\frac{y}{x}$ 即 $y=ux$ , 两边对$x$微分得 $\frac{dy}{dx}=x\frac{du}{dx}+u$ , 代入原方程得：
$$
\color{red}{\frac{du}{dx}=\frac{g(u)-u}{x}}$$
即回到了“可分离变量”的情况 **(勿忘最后将y代回)**
!!! warning "分三种情况讨论"
    ① $g(u)-u\neq0$  
    ② $\exists u_0$, 使得 $g(u_0)-u_0$, 则 $u=u_0$ 也是一解  
    ③ $g(u)-u\equiv0$, 则原式变为 $\frac{dy}{dx}=\frac{y}{x}$
## C. 一阶线性方程
$$
\bbox[lightgrey]{\frac{\mathrm{d}y}{\mathrm{d}x}+p(x)y=f(x)}$$
方法：通解公式
$$
\color{red}{y=e^{-\int p(x)dx}\int f(x)e^{\int p(x)dx}dx+ce^{-\int p(x)dx}}$$
另外，对于初值问题 ($y|_{x-x_0}=y_0$)，有
$$
\color{red}{y=e^{-\int ^x_{x_0} p(s)ds}\bigg[\int ^x_{x_0} f(t)e^{\int ^t_{x_0} p(s)ds}dt+y_0\bigg]}$$
.
## D. 伯努利方程

    
