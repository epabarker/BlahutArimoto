# BlahutArimoto
Python implementation of the Blahut-Arimoto algorithm to compute the Rate-Distortion of an i.i.d distribution 

Requirements: numpy

"""Compute the rate-distortion function of an i.i.d distribution
    Inputs :
        'dist_mat' -- (numpy matrix) representing the distoriton matrix between the input 
            alphabet and the reconstruction alphabet. dist_mat[i,j] = dist(x[i],x_hat[j])
        'p_x' -- (1D numpy array) representing the probability mass function of the source
        'beta' -- (scalar) the slope of the rate-distoriton function at the point where evaluation is 
                    required
        'max_it' -- (int) maximal number of iterations
        'eps' -- (float) accuracy required by the algorithm: the algorithm stops if there
                is no change in distoriton value of more than 'eps' between consequtive iterations
    Returns :
        'Iu' -- rate (in bits)
        'Du' -- distortion
    """

Run the example by:
$ python example.py 

