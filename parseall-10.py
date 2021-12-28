import csv
import sys
import pandas as pd

# first handle evaluation metrics:

a = 'eval-10-01-5-16.csv'
b = 'eval-10-02-5-16.csv'
c = 'eval-10-01-5-32.csv'
d = 'eval-10-02-5-32.csv'
e = 'eval-10-01-5-64.csv'
f = 'eval-10-02-5-64.csv'
g = 'eval-10-01-5-128.csv'
h = 'eval-10-02-5-128.csv'
i = 'eval-10-01-5-256.csv'
j = 'eval-10-02-5-256.csv'

a1 = 'eval-10-01-10-16.csv'
b1 = 'eval-10-02-10-16.csv'
c1 = 'eval-10-01-10-32.csv'
d1 = 'eval-10-02-10-32.csv'
e1 = 'eval-10-01-10-64.csv'
f1 = 'eval-10-02-10-64.csv'
g1 = 'eval-10-01-10-128.csv'
h1 = 'eval-10-02-10-128.csv'
i1 = 'eval-10-01-10-256.csv'
j1 = 'eval-10-02-10-256.csv'

a2 = 'eval-10-01-15-16.csv'
b2 = 'eval-10-02-15-16.csv'
c2 = 'eval-10-01-15-32.csv'
d2 = 'eval-10-02-15-32.csv'
e2 = 'eval-10-01-15-64.csv'
f2 = 'eval-10-02-15-64.csv'
g2 = 'eval-10-01-15-128.csv'
h2 = 'eval-10-02-15-128.csv'
i2 = 'eval-10-01-15-256.csv'
j2 = 'eval-10-02-15-256.csv'

a3 = 'eval-10-01-30-16.csv'
b3 = 'eval-10-02-30-16.csv'
c3 = 'eval-10-01-30-32.csv'
d3 = 'eval-10-02-30-32.csv'
e3 = 'eval-10-01-30-64.csv'
f3 = 'eval-10-02-30-64.csv'
g3 = 'eval-10-01-30-128.csv'
h3 = 'eval-10-02-30-128.csv'
i3 = 'eval-10-01-30-256.csv'
j3 = 'eval-10-02-30-256.csv'

a4 = 'eval-10-01-60-16.csv'
b4 = 'eval-10-02-60-16.csv'
c4 = 'eval-10-01-60-32.csv'
d4 = 'eval-10-02-60-32.csv'
e4 = 'eval-10-01-60-64.csv'
f4 = 'eval-10-02-60-64.csv'
g4 = 'eval-10-01-60-128.csv'
h4 = 'eval-10-02-60-128.csv'
i4 = 'eval-10-01-60-256.csv'
j4 = 'eval-10-02-60-256.csv'

a5 = 'eval-10-01-120-16.csv'
b5 = 'eval-10-02-120-16.csv'
c5 = 'eval-10-01-120-32.csv'
d5 = 'eval-10-02-120-32.csv'
e5 = 'eval-10-01-120-64.csv'
f5 = 'eval-10-02-120-64.csv'
g5 = 'eval-10-01-120-128.csv'
h5 = 'eval-10-02-120-128.csv'
i5 = 'eval-10-01-120-256.csv'
j5 = 'eval-10-02-120-256.csv'

a6 = 'eval-10-01-180-16.csv'
b6 = 'eval-10-02-180-16.csv'
c6 = 'eval-10-01-180-32.csv'
d6 = 'eval-10-02-180-32.csv'
e6 = 'eval-10-01-180-64.csv'
f6 = 'eval-10-02-180-64.csv'
g6 = 'eval-10-01-180-128.csv'
h6 = 'eval-10-02-180-128.csv'
i6 = 'eval-10-01-180-256.csv'
j6 = 'eval-10-02-180-256.csv'

a7 = 'eval-10-01-240-16.csv'
b7 = 'eval-10-02-240-16.csv'
c7 = 'eval-10-01-240-32.csv'
d7 = 'eval-10-02-240-32.csv'
e7 = 'eval-10-01-240-64.csv'
f7 = 'eval-10-02-240-64.csv'
g7 = 'eval-10-01-240-128.csv'
h7 = 'eval-10-02-240-128.csv'
i7 = 'eval-10-01-240-256.csv'
j7 = 'eval-10-02-240-256.csv'

a8 = 'eval-10-01-300-16.csv'
b8 = 'eval-10-02-300-16.csv'
c8 = 'eval-10-01-300-32.csv'
d8 = 'eval-10-02-300-32.csv'
e8 = 'eval-10-01-300-64.csv'
f8 = 'eval-10-02-300-64.csv'
g8 = 'eval-10-01-300-128.csv'
h8 = 'eval-10-02-300-128.csv'
i8 = 'eval-10-01-300-256.csv'
j8 = 'eval-10-02-300-256.csv'

a9 = 'eval-10-01-600-16.csv'
b9 = 'eval-10-02-600-16.csv'
c9 = 'eval-10-01-600-32.csv'
d9 = 'eval-10-02-600-32.csv'
e9 = 'eval-10-01-600-64.csv'
f9 = 'eval-10-02-600-64.csv'
g9 = 'eval-10-01-600-128.csv'
h9 = 'eval-10-02-600-128.csv'
i9 = 'eval-10-01-600-256.csv'
j9 = 'eval-10-02-600-256.csv'

k = 'eval-10-01-5-16-f.csv'
l = 'eval-10-02-5-16-f.csv'
m = 'eval-10-01-5-32-f.csv'
n = 'eval-10-02-5-32-f.csv'
o = 'eval-10-01-5-64-f.csv'
p = 'eval-10-02-5-64-f.csv'
q = 'eval-10-01-5-128-f.csv'
r = 'eval-10-02-5-128-f.csv'
s = 'eval-10-01-5-256-f.csv'
t = 'eval-10-02-5-256-f.csv'

k1 = 'eval-10-01-10-16-f.csv'
l1 = 'eval-10-02-10-16-f.csv'
m1 = 'eval-10-01-10-32-f.csv'
n1 = 'eval-10-02-10-32-f.csv'
o1 = 'eval-10-01-10-64-f.csv'
p1 = 'eval-10-02-10-64-f.csv'
q1 = 'eval-10-01-10-128-f.csv'
r1 = 'eval-10-02-10-128-f.csv'
s1 = 'eval-10-01-10-256-f.csv'
t1 = 'eval-10-02-10-256-f.csv'

k2 = 'eval-10-01-15-16-f.csv'
l2 = 'eval-10-02-15-16-f.csv'
m2 = 'eval-10-01-15-32-f.csv'
n2 = 'eval-10-02-15-32-f.csv'
o2 = 'eval-10-01-15-64-f.csv'
p2 = 'eval-10-02-15-64-f.csv'
q2 = 'eval-10-01-15-128-f.csv'
r2 = 'eval-10-02-15-128-f.csv'
s2 = 'eval-10-01-15-256-f.csv'
t2 = 'eval-10-02-15-256-f.csv'

k3 = 'eval-10-01-30-16-f.csv'
l3 = 'eval-10-02-30-16-f.csv'
m3 = 'eval-10-01-30-32-f.csv'
n3 = 'eval-10-02-30-32-f.csv'
o3 = 'eval-10-01-30-64-f.csv'
p3 = 'eval-10-02-30-64-f.csv'
q3 = 'eval-10-01-30-128-f.csv'
r3 = 'eval-10-02-30-128-f.csv'
s3 = 'eval-10-01-30-256-f.csv'
t3 = 'eval-10-02-30-256-f.csv'

k4 = 'eval-10-01-60-16-f.csv'
l4 = 'eval-10-02-60-16-f.csv'
m4 = 'eval-10-01-60-32-f.csv'
n4 = 'eval-10-02-60-32-f.csv'
o4 = 'eval-10-01-60-64-f.csv'
p4 = 'eval-10-02-60-64-f.csv'
q4 = 'eval-10-01-60-128-f.csv'
r4 = 'eval-10-02-60-128-f.csv'
s4 = 'eval-10-01-60-256-f.csv'
t4 = 'eval-10-02-60-256-f.csv'

k5 = 'eval-10-01-120-16-f.csv'
l5 = 'eval-10-02-120-16-f.csv'
m5 = 'eval-10-01-120-32-f.csv'
n5 = 'eval-10-02-120-32-f.csv'
o5 = 'eval-10-01-120-64-f.csv'
p5 = 'eval-10-02-120-64-f.csv'
q5 = 'eval-10-01-120-128-f.csv'
r5 = 'eval-10-02-120-128-f.csv'
s5 = 'eval-10-01-120-256-f.csv'
t5 = 'eval-10-02-120-256-f.csv'

k6 = 'eval-10-01-180-16-f.csv'
l6 = 'eval-10-02-180-16-f.csv'
m6 = 'eval-10-01-180-32-f.csv'
n6 = 'eval-10-02-180-32-f.csv'
o6 = 'eval-10-01-180-64-f.csv'
p6 = 'eval-10-02-180-64-f.csv'
q6 = 'eval-10-01-180-128-f.csv'
r6 = 'eval-10-02-180-128-f.csv'
s6 = 'eval-10-01-180-256-f.csv'
t6 = 'eval-10-02-180-256-f.csv'

k7 = 'eval-10-01-240-16-f.csv'
l7 = 'eval-10-02-240-16-f.csv'
m7 = 'eval-10-01-240-32-f.csv'
n7 = 'eval-10-02-240-32-f.csv'
o7 = 'eval-10-01-240-64-f.csv'
p7 = 'eval-10-02-240-64-f.csv'
q7 = 'eval-10-01-240-128-f.csv'
r7 = 'eval-10-02-240-128-f.csv'
s7 = 'eval-10-01-240-256-f.csv'
t7 = 'eval-10-02-240-256-f.csv'

k8 = 'eval-10-01-300-16-f.csv'
l8 = 'eval-10-02-300-16-f.csv'
m8 = 'eval-10-01-300-32-f.csv'
n8 = 'eval-10-02-300-32-f.csv'
o8 = 'eval-10-01-300-64-f.csv'
p8 = 'eval-10-02-300-64-f.csv'
q8 = 'eval-10-01-300-128-f.csv'
r8 = 'eval-10-02-300-128-f.csv'
s8 = 'eval-10-01-300-256-f.csv'
t8 = 'eval-10-02-300-256-f.csv'

k9 = 'eval-10-01-600-16-f.csv'
l9 = 'eval-10-02-600-16-f.csv'
m9 = 'eval-10-01-600-32-f.csv'
n9 = 'eval-10-02-600-32-f.csv'
o9 = 'eval-10-01-600-64-f.csv'
p9 = 'eval-10-02-600-64-f.csv'
q9 = 'eval-10-01-600-128-f.csv'
r9 = 'eval-10-02-600-128-f.csv'
s9 = 'eval-10-01-600-256-f.csv'
t9 = 'eval-10-02-600-256-f.csv'

# now fit metrics:

aa = 'fit-10-01-5-16.csv'
bb = 'fit-10-02-5-16.csv'
cc = 'fit-10-01-5-32.csv'
dd = 'fit-10-02-5-32.csv'
ee = 'fit-10-01-5-64.csv'
ff = 'fit-10-02-5-64.csv'
gg = 'fit-10-01-5-128.csv'
hh = 'fit-10-02-5-128.csv'
ii = 'fit-10-01-5-256.csv'
jj = 'fit-10-02-5-256.csv'

aa1 = 'fit-10-01-10-16.csv'
bb1 = 'fit-10-02-10-16.csv'
cc1 = 'fit-10-01-10-32.csv'
dd1 = 'fit-10-02-10-32.csv'
ee1 = 'fit-10-01-10-64.csv'
ff1 = 'fit-10-02-10-64.csv'
gg1 = 'fit-10-01-10-128.csv'
hh1 = 'fit-10-02-10-128.csv'
ii1 = 'fit-10-01-10-256.csv'
jj1 = 'fit-10-02-10-256.csv'

aa2 = 'fit-10-01-15-16.csv'
bb2 = 'fit-10-02-15-16.csv'
cc2 = 'fit-10-01-15-32.csv'
dd2 = 'fit-10-02-15-32.csv'
ee2 = 'fit-10-01-15-64.csv'
ff2 = 'fit-10-02-15-64.csv'
gg2 = 'fit-10-01-15-128.csv'
hh2 = 'fit-10-02-15-128.csv'
ii2 = 'fit-10-01-15-256.csv'
jj2 = 'fit-10-02-15-256.csv'

aa3 = 'fit-10-01-30-16.csv'
bb3 = 'fit-10-02-30-16.csv'
cc3 = 'fit-10-01-30-32.csv'
dd3 = 'fit-10-02-30-32.csv'
ee3 = 'fit-10-01-30-64.csv'
ff3 = 'fit-10-02-30-64.csv'
gg3 = 'fit-10-01-30-128.csv'
hh3 = 'fit-10-02-30-128.csv'
ii3 = 'fit-10-01-30-256.csv'
jj3 = 'fit-10-02-30-256.csv'

aa4 = 'fit-10-01-60-16.csv'
bb4 = 'fit-10-02-60-16.csv'
cc4 = 'fit-10-01-60-32.csv'
dd4 = 'fit-10-02-60-32.csv'
ee4 = 'fit-10-01-60-64.csv'
ff4 = 'fit-10-02-60-64.csv'
gg4 = 'fit-10-01-60-128.csv'
hh4 = 'fit-10-02-60-128.csv'
ii4 = 'fit-10-01-60-256.csv'
jj4 = 'fit-10-02-60-256.csv'

aa5 = 'fit-10-01-120-16.csv'
bb5 = 'fit-10-02-120-16.csv'
cc5 = 'fit-10-01-120-32.csv'
dd5 = 'fit-10-02-120-32.csv'
ee5 = 'fit-10-01-120-64.csv'
ff5 = 'fit-10-02-120-64.csv'
gg5 = 'fit-10-01-120-128.csv'
hh5 = 'fit-10-02-120-128.csv'
ii5 = 'fit-10-01-120-256.csv'
jj5 = 'fit-10-02-120-256.csv'

aa6 = 'fit-10-01-180-16.csv'
bb6 = 'fit-10-02-180-16.csv'
cc6 = 'fit-10-01-180-32.csv'
dd6 = 'fit-10-02-180-32.csv'
ee6 = 'fit-10-01-180-64.csv'
ff6 = 'fit-10-02-180-64.csv'
gg6 = 'fit-10-01-180-128.csv'
hh6 = 'fit-10-02-180-128.csv'
ii6 = 'fit-10-01-180-256.csv'
jj6 = 'fit-10-02-180-256.csv'

aa7 = 'fit-10-01-240-16.csv'
bb7 = 'fit-10-02-240-16.csv'
cc7 = 'fit-10-01-240-32.csv'
dd7 = 'fit-10-02-240-32.csv'
ee7 = 'fit-10-01-240-64.csv'
ff7 = 'fit-10-02-240-64.csv'
gg7 = 'fit-10-01-240-128.csv'
hh7 = 'fit-10-02-240-128.csv'
ii7 = 'fit-10-01-240-256.csv'
jj7 = 'fit-10-02-240-256.csv'

aa8 = 'fit-10-01-300-16.csv'
bb8 = 'fit-10-02-300-16.csv'
cc8 = 'fit-10-01-300-32.csv'
dd8 = 'fit-10-02-300-32.csv'
ee8 = 'fit-10-01-300-64.csv'
ff8 = 'fit-10-02-300-64.csv'
gg8 = 'fit-10-01-300-128.csv'
hh8 = 'fit-10-02-300-128.csv'
ii8 = 'fit-10-01-300-256.csv'
jj8 = 'fit-10-02-300-256.csv'

aa9 = 'fit-10-01-600-16.csv'
bb9 = 'fit-10-02-600-16.csv'
cc9 = 'fit-10-01-600-32.csv'
dd9 = 'fit-10-02-600-32.csv'
ee9 = 'fit-10-01-600-64.csv'
ff9 = 'fit-10-02-600-64.csv'
gg9 = 'fit-10-01-600-128.csv'
hh9 = 'fit-10-02-600-128.csv'
ii9 = 'fit-10-01-600-256.csv'
jj9 = 'fit-10-02-600-256.csv'

kk = 'fit-10-01-5-16-f.csv'
ll = 'fit-10-02-5-16-f.csv'
mm = 'fit-10-01-5-32-f.csv'
nn = 'fit-10-02-5-32-f.csv'
oo = 'fit-10-01-5-64-f.csv'
pp = 'fit-10-02-5-64-f.csv'
qq = 'fit-10-01-5-128-f.csv'
rr = 'fit-10-02-5-128-f.csv'
ss = 'fit-10-01-5-256-f.csv'
tt = 'fit-10-02-5-256-f.csv'

kk1 = 'fit-10-01-10-16-f.csv'
ll1 = 'fit-10-02-10-16-f.csv'
mm1 = 'fit-10-01-10-32-f.csv'
nn1 = 'fit-10-02-10-32-f.csv'
oo1 = 'fit-10-01-10-64-f.csv'
pp1 = 'fit-10-02-10-64-f.csv'
qq1 = 'fit-10-01-10-128-f.csv'
rr1 = 'fit-10-02-10-128-f.csv'
ss1 = 'fit-10-01-10-256-f.csv'
tt1 = 'fit-10-02-10-256-f.csv'

kk2 = 'fit-10-01-15-16-f.csv'
ll2 = 'fit-10-02-15-16-f.csv'
mm2 = 'fit-10-01-15-32-f.csv'
nn2 = 'fit-10-02-15-32-f.csv'
oo2 = 'fit-10-01-15-64-f.csv'
pp2 = 'fit-10-02-15-64-f.csv'
qq2 = 'fit-10-01-15-128-f.csv'
rr2 = 'fit-10-02-15-128-f.csv'
ss2 = 'fit-10-01-15-256-f.csv'
tt2 = 'fit-10-02-15-256-f.csv'

kk3 = 'fit-10-01-30-16-f.csv'
ll3 = 'fit-10-02-30-16-f.csv'
mm3 = 'fit-10-01-30-32-f.csv'
nn3 = 'fit-10-02-30-32-f.csv'
oo3 = 'fit-10-01-30-64-f.csv'
pp3 = 'fit-10-02-30-64-f.csv'
qq3 = 'fit-10-01-30-128-f.csv'
rr3 = 'fit-10-02-30-128-f.csv'
ss3 = 'fit-10-01-30-256-f.csv'
tt3 = 'fit-10-02-30-256-f.csv'

kk4 = 'fit-10-01-60-16-f.csv'
ll4 = 'fit-10-02-60-16-f.csv'
mm4 = 'fit-10-01-60-32-f.csv'
nn4 = 'fit-10-02-60-32-f.csv'
oo4 = 'fit-10-01-60-64-f.csv'
pp4 = 'fit-10-02-60-64-f.csv'
qq4 = 'fit-10-01-60-128-f.csv'
rr4 = 'fit-10-02-60-128-f.csv'
ss4 = 'fit-10-01-60-256-f.csv'
tt4 = 'fit-10-02-60-256-f.csv'

kk5 = 'fit-10-01-120-16-f.csv'
ll5 = 'fit-10-02-120-16-f.csv'
mm5 = 'fit-10-01-120-32-f.csv'
nn5 = 'fit-10-02-120-32-f.csv'
oo5 = 'fit-10-01-120-64-f.csv'
pp5 = 'fit-10-02-120-64-f.csv'
qq5 = 'fit-10-01-120-128-f.csv'
rr5 = 'fit-10-02-120-128-f.csv'
ss5 = 'fit-10-01-120-256-f.csv'
tt5 = 'fit-10-02-120-256-f.csv'

kk6 = 'fit-10-01-180-16-f.csv'
ll6 = 'fit-10-02-180-16-f.csv'
mm6 = 'fit-10-01-180-32-f.csv'
nn6 = 'fit-10-02-180-32-f.csv'
oo6 = 'fit-10-01-180-64-f.csv'
pp6 = 'fit-10-02-180-64-f.csv'
qq6 = 'fit-10-01-180-128-f.csv'
rr6 = 'fit-10-02-180-128-f.csv'
ss6 = 'fit-10-01-180-256-f.csv'
tt6 = 'fit-10-02-180-256-f.csv'

kk7 = 'fit-10-01-240-16-f.csv'
ll7 = 'fit-10-02-240-16-f.csv'
mm7 = 'fit-10-01-240-32-f.csv'
nn7 = 'fit-10-02-240-32-f.csv'
oo7 = 'fit-10-01-240-64-f.csv'
pp7 = 'fit-10-02-240-64-f.csv'
qq7 = 'fit-10-01-240-128-f.csv'
rr7 = 'fit-10-02-240-128-f.csv'
ss7 = 'fit-10-01-240-256-f.csv'
tt7 = 'fit-10-02-240-256-f.csv'

kk8 = 'fit-10-01-300-16-f.csv'
ll8 = 'fit-10-02-300-16-f.csv'
mm8 = 'fit-10-01-300-32-f.csv'
nn8 = 'fit-10-02-300-32-f.csv'
oo8 = 'fit-10-01-300-64-f.csv'
pp8 = 'fit-10-02-300-64-f.csv'
qq8 = 'fit-10-01-300-128-f.csv'
rr8 = 'fit-10-02-300-128-f.csv'
ss8 = 'fit-10-01-300-256-f.csv'
tt8 = 'fit-10-02-300-256-f.csv'

kk9 = 'fit-10-01-600-16-f.csv'
ll9 = 'fit-10-02-600-16-f.csv'
mm9 = 'fit-10-01-600-32-f.csv'
nn9 = 'fit-10-02-600-32-f.csv'
oo9 = 'fit-10-01-600-64-f.csv'
pp9 = 'fit-10-02-600-64-f.csv'
qq9 = 'fit-10-01-600-128-f.csv'
rr9 = 'fit-10-02-600-128-f.csv'
ss9 = 'fit-10-01-600-256-f.csv'
tt9 = 'fit-10-02-600-256-f.csv'

csv_files = [a,b,c,d,e,f,g,h,i,j,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,
a3,b3,c3,d3,e3,f3,g3,h3,i3,j3,a4,b4,c4,d4,e4,f4,g4,h4,i4,j4,a5,b5,c5,d5,e5,f5,g5,h5,i5,j5,a6,
b6,c6,d6,e6,f6,g6,h6,i6,j6,a7,b7,c7,d7,e7,f7,g7,h7,i7,j7,a8,b8,c8,d8,e8,f8,g8,h8,i8,j8,a9,b9,
c9,d9,e9,f9,g9,h9,i9,j9,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,aa1,bb1,cc1,dd1,ee1,ff1,gg1,hh1,ii1,jj1,
aa2,bb2,cc2,dd2,ee2,ff2,gg2,hh2,ii2,jj2,aa3,bb3,cc3,dd3,ee3,ff3,gg3,hh3,ii3,jj3,aa4,bb4,cc4,dd4,
ee4,ff4,gg4,hh4,ii4,jj4,aa5,bb5,cc5,dd5,ee5,ff5,gg5,hh5,ii5,jj5,aa6,bb6,cc6,dd6,ee6,ff6,gg6,hh6,
ii6,jj6,aa7,bb7,cc7,dd7,ee7,ff7,gg7,hh7,ii7,jj7,aa8,bb8,cc8,dd8,ee8,ff8,gg8,hh8,ii8,jj8,aa9,bb9,
cc9,dd9,ee9,ff9,gg9,hh9,ii9,jj9]
out_files = [k,l,m,n,o,p,q,r,s,t,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,k2,l2,m2,n2,o2,p2,q2,r2,s2,t2,
k3,l3,m3,n3,o3,p3,q3,r3,s3,t3,k4,l4,m4,n4,o4,p4,q4,r4,s4,t4,k5,l5,m5,n5,o5,p5,q5,r5,s5,t5,k6,
l6,m6,n6,o6,p6,q6,r6,s6,t6,k7,l7,m7,n7,o7,p7,q7,r7,s7,t7,k8,l8,m8,n8,o8,p8,q8,r8,s8,t8,k9,l9,
m9,n9,o9,p9,q9,r9,s9,t9,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,kk1,ll1,mm1,nn1,oo1,pp1,qq1,rr1,ss1,tt1,
kk2,ll2,mm2,nn2,oo2,pp2,qq2,rr2,ss2,tt2,kk3,ll3,mm3,nn3,oo3,pp3,qq3,rr3,ss3,tt3,kk4,ll4,mm4,nn4,
oo4,pp4,qq4,rr4,ss4,tt4,kk5,ll5,mm5,nn5,oo5,pp5,qq5,rr5,ss5,tt5,kk6,ll6,mm6,nn6,oo6,pp6,qq6,rr6,
ss6,tt6,kk7,ll7,mm7,nn7,oo7,pp7,qq7,rr7,ss7,tt7,kk8,ll8,mm8,nn8,oo8,pp8,qq8,rr8,ss8,tt8,kk9,ll9,
mm9,nn9,oo9,pp9,qq9,rr9,ss9,tt9]

o_counter = 0
for i in csv_files:
	outfile = open(out_files[o_counter],"w")
	with open(i,'r') as infile:
		reader = csv.reader(infile, delimiter = ",")
		for row in reader:
			# final line will be [ram,totcpu%,avgcpufreq,gpu%,gpufreq]
			# handle ram
		
			ram = int(row[20])
			ram = ram / 1048576
	

			# handle the 4 cpus
			cpu0u = float(row[0])
			cpu0s = float(row[1])
			cpu0 = cpu0u + cpu0s

			cpu1u = float(row[5])
			cpu1s = float(row[6])
			cpu1 = cpu1u + cpu1s

			cpu2u = float(row[10])
			cpu2s = float(row[11])
			cpu2 = cpu2u + cpu2s

			cpu3u = float(row[15])
			cpu3s = float(row[16])
			cpu3 = cpu3u + cpu3s

	

			# create values for total and average across all cores
			cputot = cpu0 + cpu1 + cpu2 + cpu3
		


			# create the line
			line = "{},{}\n".format(ram,cputot)
			outfile.write(line)
	o_counter+=1