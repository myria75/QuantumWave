OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
h q[0];
t q[1];
s q[2];
y q[3];
z q[3];

measure q[0] -> c[0];

rx(pi/2) q[2];
ry(pi/2) q[3];
rz(pi/2) q[2];
u(pi/2, pi/2, pi/2) q[0];

ch q[1], q[0];
cy q[1], q[0];
cz q[3], q[2];

cu(pi/2, pi/2, pi/2, 0) q[1], q[0];
crx(pi/2) q[1], q[0];
cry(pi/2) q[1], q[3];
crz(pi/2) q[1], q[0];