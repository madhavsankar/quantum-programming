OPENQASM 2.0;
include "qelib1.inc";
qreg q[16];
creg c[16];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[6];
h q[5];
h q[4];
t q[3];
h q[2];
h q[1];
cx q[0],q[3];
tdg q[4];
