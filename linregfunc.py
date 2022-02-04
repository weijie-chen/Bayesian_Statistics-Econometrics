def gen_X(n, k):
    """
    Parameters
    ----------
    n, k: int
        generate a random explanatory matrxi with constant term of size n by k, n is the sample size,
        k is the number of parameters.
    Returns
    ----------
    X: ndarray
        matrix styled n by k random array generated by np.random.randn().
    """
    const = np.ones(n)
    const = const[np.newaxis, :]
    X_inde = np.random.randn(k-1, n)
    X = np.concatenate((const.T, X_inde.T), axis=1)
    return X

def gen_beta(params = [2, 3, 4, 5]):
    """
    Parameters
    ----------
    params: list
        input a list of beta parameters
    
    Returns
    ----------
    beta_array: ndnarry
        an array of beta coefficients, no nothing input, default value
        params = [2, 3, 4, 5]
    """
    beta_array = np.array(params)
    beta_array = beta_array[np.newaxis, :].T
    return beta_array

def gen_u(n):
    """
    Parameters
    ----------
    params: int
        input a integer for the size of disturbance term
    
    Returns
    ----------
    u: ndnarry
        an array of disturbance term
    """
    u = np.random.randn(n)
    u = u[np.newaxis, :].T
    return u