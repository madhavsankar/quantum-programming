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
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];
cx q[0],q[1];
h q[2];
t q[3];
t q[4];
t q[5];
h q[6];
tdg q[7];
h q[8];
h q[9];
t q[10];
h q[10];
h q[11];
cx q[10],q[11];
tdg q[11];