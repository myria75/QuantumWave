OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
h q[0];
t q[1];
s q[2];
y q[3];
z q[0];
measure q[1] -> c[1];
rx(pi/2) q[0];
ry(pi/2) q[1];
rz(pi/2) q[2];
u(pi/2, pi/2, pi/2) q[0];
