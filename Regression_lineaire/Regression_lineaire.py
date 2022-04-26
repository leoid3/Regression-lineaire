import numpy as np
import matplotlib.pyplot as plt

################ Affichage des points et de l'équition de droite ##################

def plotaff(correlation, o, P=np.array([]), X=[], Y=[]):
    plt.scatter(X, Y, marker="o", color="blue")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Droite d'equation : {P[1]:.1f}*x + {P[0]:.1f} avec une correlation lineaire de : {correlation:.3f}")
    Xm=max(X)
    y= P[0]
    i=1
    x= np.linspace(-Xm-5, Xm+5, 50)
    for i in range(o):
        y= y + (P[i]*np.power(x, i))
    plt.ylim(-max(Y)-5, max(Y)+5)
    plt.plot(x, y, color='green', ls="--")
    plt.grid()

    return plt


############# Calcul des matrices M, Q, s, P et de la corrélation linéaire ##############

def CalculMatrice(nbp, ordr, X=[], Y=[]):

    M = np.ones((int(nbp), ordr))
    for i in range(len(X)):
        for j in range(ordr):
            M[i][j]=np.power(X[i], j)
            
        
    
    Q= np.array(np.dot(M.T, M))
    s= np.array(np.dot(M.T, Y))
    temp = np.dot(np.linalg.inv(Q), s)
    P= np.array(temp)

    covariance= np.cov(X, Y)[0][1]
    X_ecart_type= np.std(X)
    Y_ecart_type= np.std(Y)
    correlation= (covariance/(X_ecart_type*Y_ecart_type))/2
    fig = plotaff(correlation, ordr, P, X, Y)
    return fig
