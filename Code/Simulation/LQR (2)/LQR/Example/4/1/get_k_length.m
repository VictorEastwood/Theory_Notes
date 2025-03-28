function K = get_k_length(leg_length)
    %theta : 摆杆与竖直方向夹角            R   ：驱动轮半径
    %x     : 驱动轮位移                    L   : 摆杆重心到驱动轮轴距离
    %phi   : 机体与水平夹角                LM  : 摆杆重心到其转轴距离
    %T     ：驱动轮输出力矩                l   : 机体重心到其转轴距离
    %Tp    : 髋关节输出力矩                mw  : 驱动轮转子质量
    %N     ：驱动轮对摆杆力的水平分量      mp  : 摆杆质量
    %P     ：驱动轮对摆杆力的竖直分量      M   : 机体质量
    %Nm    ：摆杆对机体力水平方向分量      Iw  : 驱动轮转子转动惯量
    %Pm    ：摆杆对机体力竖直方向分量      Ip  : 摆杆绕质心转动惯量
    %Nf    : 地面对驱动轮摩擦力            Im  : 机体绕质心转动惯量

    syms x(t) T R Iw mw M L LM theta(t) l phi(t) mp g Tp Ip IM
    syms f1 f2 f3 d_theta d_x d_phi theta0 x0 phi0 
    %% 定义数值变量
    R1=0.0603;              %驱动轮半径
    L1=leg_length/2;        %摆杆重心到驱动轮轴距离
    LM1=leg_length/2;       %摆杆重心到其转轴距离
    l1=0.011;               %机体质心距离转轴距离
    mw1=0.6;                %驱动轮质量
    mp1=0.045;              %杆质量
    M1=1.44;                %机体质量
    Iw1=0.5*mw1*R1^2;       %驱动轮转动惯量
    Ip1=mp1*((L1+LM1)^2+0.048^2)/12.0; %摆杆转动惯量
    IM1=M1*(0.135^2+0.066^2)/12.0;     %机体绕质心转动惯量
    %% 定义运动方程
    NM = M*diff(x + (L + LM )*sin(theta)-l*sin(phi),t,2);
    N = NM + mp*diff(x + L*sin(theta),t,2);
    PM = M*g + M*diff((L+LM)*cos(theta)+l*cos(phi),t,2);
    P = PM +mp*g+mp*diff(L*cos(theta),t,2);
    eqn1 = diff(x,t,2) == (T-N*R)/(Iw/R + mw*R);
    eqn2 = Ip*diff(theta,t,2) == (P*L + PM*LM)*sin(theta)-(N*L+NM*LM)*cos(theta)-T+Tp;
    eqn3 = IM*diff(phi,t,2) == Tp +NM*l*cos(phi)+PM*l*sin(phi);
    % 通过替换变量简化运动方程，主要是将方程中对时间t求导的符号变量替换为其他辅助变量
    eqn10 = subs(eqn1,[diff(theta,t,2),diff(x,t,2),diff(phi,t,2),diff(theta,t),diff(x,t),diff(phi,t),theta,x,phi],[f1,f2,f3,d_theta,d_x,d_phi,theta0,x0,phi0]);
    eqn20 = subs(eqn2,[diff(theta,t,2),diff(x,t,2),diff(phi,t,2),diff(theta,t),diff(x,t),diff(phi,t),theta,x,phi],[f1,f2,f3,d_theta,d_x,d_phi,theta0,x0,phi0]);
    eqn30 = subs(eqn3,[diff(theta,t,2),diff(x,t,2),diff(phi,t,2),diff(theta,t),diff(x,t),diff(phi,t),theta,x,phi],[f1,f2,f3,d_theta,d_x,d_phi,theta0,x0,phi0]);
    %% 求状态空间矩阵
    % 求解由eqn10、eqn20和eqn30方程组成的三元一次代数方程组，并将解赋值给符号变量f1、f2和f3
    [f1,f2,f3] = solve(eqn10,eqn20,eqn30,f1,f2,f3);
    % 求解状态方程，并在系统的平衡点处线性化系统
    A=subs(jacobian([d_theta,f1,d_x,f2,d_phi,f3],[theta0,d_theta,x0,d_x,phi0,d_phi]),[theta0,d_theta,d_x,phi0,d_phi,T,Tp],[0,0,0,0,0,0,0]);
    % 将符号变量替换为数值变量，求解状态方程数值解
    AA=subs(A,[R,L,LM,l,mw,mp,M,Iw,Ip,IM,g],[R1,L1,LM1,l1,mw1,mp1,M1,Iw1,Ip1,IM1,9.8]);
    AA=double(AA);
    % 求解状态方程，并在系统的平衡点处线性化系统
    B=subs(jacobian([d_theta,f1,d_x,f2,d_phi,f3],[T,Tp]),[theta0,d_theta,d_x,phi0,d_phi,T,Tp],[0,0,0,0,0,0,0]);
    % 将符号变量替换为数值变量，求解状态方程数值解
    BB=subs(B,[R,L,LM,l,mw,mp,M,Iw,Ip,IM,g],[R1,L1,LM1,l1,mw1,mp1,M1,Iw1,Ip1,IM1,9.8]);
    BB=double(BB);
    %% 求LQR增益矩阵
    Q=diag([1 0.07 10 5 300 0.6]);
    R=[20 0;0,1]; %T Tp
    K=lqr(AA,BB,Q,R);
end