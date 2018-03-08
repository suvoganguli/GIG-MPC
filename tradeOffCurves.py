import numpy as np
import matplotlib.pyplot as plt


# row-names = N = 4, 6, 8
# col-names = ns = 0, 1, 2
CT_data_ns4 = np.array([[0.24,	0.79,	0.70],
                    [0.68,	6.54,	6.04],
                    [1.40,	16.11,	18.76],
                    [2.77, 44.26, 48.42]])/0.24



CT_data_ns6 = np.array([[0.23,	0.60,	0.54],
                    [0.63,	3.34,	3.81],
                    [1.36,	15.93,	17.07]])/0.24


# -------------------------------------------------------------

model = 3

if model == 1:
    a = 2.0
    b = 0.5
    N0 = 3.8

    n_N = 3
    n_no = 3
    CT_model_ns4 = np.zeros((n_N, n_no))
    error_ns4 = np.zeros((n_N, n_no))

    N = np.array([4, 6, 8])
    no = np.array([0, 1, 2])

    for i in range(n_no):
        for j in range(n_N):

            CT_model_ns4[i,j] = a * (1 - np.exp(-b * (N[j] - N0))) * (no[i] + 1)**2
            error_ns4[i,j] = CT_data_ns4[i,j] - CT_model_ns4[i,j]

elif model == 2:
    a = 0.8
    b = 0.5
    N0 = 4

    n_N = 4
    n_no = 3
    CT_model_ns4 = np.zeros((n_N, n_no))
    error_ns4 = np.zeros((n_N, n_no))

    N = np.array([4, 6, 8, 10])
    no = np.array([0, 1, 2])

    for i in range(n_N):
        for j in range(n_no):
            CT_model_ns4[i, j] = a * (2**(N[i] - N0)/2) * (no[j] + 1)
            error_ns4[i, j] = CT_data_ns4[i, j] - CT_model_ns4[i, j]

elif model == 3:
    a = 0.4/3/0.24
    b = 1.2
    c = 1.5
    d = 1
    N0 = 4

    n_N = 4
    n_no = 3
    CT_model_ns4 = np.zeros((n_N, n_no))
    error_ns4 = np.zeros((n_N, n_no))

    N = np.array([4, 6, 8, 10])
    no = np.array([0, 1, 2])

    for i in range(n_N):
        for j in range(n_no):
            CT_model_ns4[i, j] = a * b**( c * (2*N[i]+3) ) * (1 - np.exp(-d*no[j]))
            error_ns4[i, j] = CT_data_ns4[i, j] - CT_model_ns4[i, j]


print(CT_data_ns4)
print('')
print(CT_model_ns4)
print('')
print(error_ns4)
print('')
print(np.linalg.norm(error_ns4))
print('')


ix_no = 1
ix_N = 2
plt.figure(1, figsize=(5, 7))
plt.subplot(211)
plt.plot(N,CT_model_ns4[:,ix_no],N,CT_data_ns4[:,ix_no])
plt.xlabel('N')
plt.ylabel('CPU Time (normalized)')
plt.grid(True)
plt.subplot(212)
plt.plot(no,CT_model_ns4[ix_N,:],no,CT_data_ns4[ix_N,:])
plt.xlabel('no')
plt.ylabel('CPU Time (normalized)')
plt.grid(True)
plt.show()

# -------------------------------------------------------------
# a = 2.0
# b = 0.5
# N0 = 3.8
#
# n_N = 3
# n_no = 3
# CT_model_ns6 = np.zeros((n_N, n_no))
# error_ns6 = np.zeros((n_N, n_no))
#
# N = np.array([4, 6, 8])
# no = np.array([0, 1, 2])
#
# for i in range(n_N):
#     for j in range(n_no):
#
#         CT_model_ns6[i,j] = a * (1 - np.exp(-b * (N[j] - N0))) * (no[i] + 1)**2
#         error_ns6[i,j] = CT_data_ns6[i,j] - CT_model_ns6[i,j]
#
#
# print(error_ns6)
# print(np.linalg.norm(error_ns6))