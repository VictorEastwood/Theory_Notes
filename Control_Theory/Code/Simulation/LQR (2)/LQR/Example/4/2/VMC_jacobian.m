syms phi0(t) phi1(t) phi2(t) phi3(t) phi4(t) d_phi_1 d_phi_4 l1 l2 l3 l4 l5 L0
%% 定义变量
x_B = l1*cos(phi1);
y_B = l1*sin(phi1);
x_C = x_B+l2*cos(phi2);
y_C = y_B+l2*sin(phi2);
x_D = l5+l4*cos(phi4);
y_D = l4*sin(phi4);
d_x_B = diff(x_B,t);
d_y_B = diff(y_B,t);
d_x_C = diff(x_C,t);
d_y_C = diff(y_C,t);
d_x_D = diff(x_D,t);
d_y_D = diff(y_D,t);
d_phi_2 = ((d_x_D-d_x_B)*cos(phi3)+(d_y_D-d_y_B)*sin(phi3))/l2/sin(phi3-phi2);
%% 利用 subs 函数将表达式中对时间t求导的符号变量替换为基本符号变量
d_x_C = subs(d_x_C,diff(phi2,t),d_phi_2);
d_x_C = subs(d_x_C,[diff(phi1,t),diff(phi4,t)],[d_phi_1,d_phi_4]);
d_y_C = subs(d_y_C,diff(phi2,t),d_phi_2);
d_y_C = subs(d_y_C,[diff(phi1,t),diff(phi4,t)],[d_phi_1,d_phi_4]);
%% 求雅可比矩阵
d_x = [d_x_C; d_y_C];
d_q = [d_phi_1; d_phi_4];
% 对d_x中包含d_q的项进行合并,simplify简化矩阵表达式
d_x = simplify(collect(d_x,d_q));
J = simplify(jacobian(d_x,d_q));
%% 求关节力矩与虚拟力映射关系
R=[cos(phi0-pi/2) -sin(phi0-pi/2);
   sin(phi0-pi/2)  cos(phi0-pi/2)];
M=[0 -1/L0;
   1     0];
T=simplify(J.'*R*M);
disp(T);