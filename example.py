#example for the use of Blahut-Arimoto algothm in BlahutArimoto.py

from BlahutArimoto import BlahutArimato
import numpy as np

def BlahutArimotoExample() :
    
    def hamming_dist(x,y) :
        return (x!=y)+0.0
    
    def quad_dist(x,y) :
        return (x-y)**2

    def bin_ent(x) :
        return -x*np.log2(x)-(1-x)*np.log2(1-x)

    def Gauss_pdf(x) :
        return 1/(2*np.pi) * np.exp(-x ** 2 / 2)
    

    beta = 0.3

    # Example 1: Bernuolli input with Hamming distortion
    xx = np.array([0,1]) #binary input
    xx_hat = np.array([0,1]) #binary reconstruction
    al = 0.4  # P(X=1) = al
    p_x = np.array([1-al, al])
    
    X, X_hat = np.meshgrid(xx, xx_hat)  #creat distortion matrix
    dist_mat = hamming_dist(X,X_hat)
    R, D = BlahutArimato(dist_mat, p_x, beta) #evaluate at beta = 0.3
    #check against true R(D) :
    print "Hamming Binary:"
    print "at beta = {}: D = {}, R = {}".format(beta,D,R)
    print "Difference between true R(D) (binary):",
    print np.abs(bin_ent(al)-bin_ent(D) - R) #difference between true and estimated
    
    # Example 2: (truncated) Gaussian input with quadratic distortion
    xx = np.linspace(-5,5,1000) #source alphabet
    xx_hat = np.linspace(-5,5,1000) #reconstruction alphabet
    p_x = Gauss_pdf(xx) #source pdf
    
    X, X_hat = np.meshgrid(xx, xx_hat)  #creat distortion matrix
    dist_mat = quad_dist(X,X_hat)
    R, D = BlahutArimato(dist_mat, p_x, beta) #evaluate at beta = 0.3
    
    print "Quadratic Gaussian:"
    print "at beta = {}: D = {}, R = {}".format(beta,D,R)
    print "Difference between true R(D) (quadratic Gaussian):",
    print np.abs(D - 2 ** (-2 * R)) #difference between true and estimated

if __name__ == "__main__":
    print "Starting Blahut-Arimoto example..."
    BlahutArimotoExample()