from numpy import eye


def laplaciana(N, dtype):
	A = eye(N, dtype=dtype)*2 + eye(N, k=1, dtype=dtype)*-1 + eye(N, k=-1, dtype=dtype)*-1
	return A

