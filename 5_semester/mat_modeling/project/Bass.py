def bass(M,p,q,iterations,step):
    t_array = [0]
    n_array = []
    Big_n_array = [p*M]
    ad_array = [p*M]
    for i in range(1,round(iterations/step)):
        t_array.append(i)
        n_array.append((p+q*Big_n_array[-1]/M)*(M-Big_n_array[-1]))
        Big_n_array.append(Big_n_array[-1]+n_array[-1])
        ad_array.append(p*(M-Big_n_array[-1]))
    return t_array, n_array, ad_array, Big_n_array
        
M = 100000
p = 0.02
q = 0.05
ex = bass(M,p,q,100,1)
