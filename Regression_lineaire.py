import numpy as np
import matplotlib.pyplot as plt

################ Affichage des points et de l'equition de droite ##################

def plotaff(correlation, o, P=np.array([]), X=[], Y=[]):
    plt.scatter(X, Y, marker="o", color="blue")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Regression lineaire d'ordre  {o-1:f}")
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


############# Calcul des matrices M, Q, s, P et de la correlation lineaire ##############

def CalculMatrice(nbp, ordr, X=[], Y=[]):

    M = np.ones((int(nbp), ordr))
    for i in range(len(X)):
        for j in range(ordr):
            M[i][j]=np.power(X[i], j)
            
        
    
    Q= np.array(np.dot(M.T, M))
    s= np.array(np.dot(M.T, Y))
    P= Gauss(Q, s) #Permet d'inverser une matrice par la methode de Gauss

    covariance= np.cov(X, Y)[0][1]
    X_ecart_type= np.std(X)
    Y_ecart_type= np.std(Y)
    correlation= (covariance/(X_ecart_type*Y_ecart_type))/2
    fig = plotaff(correlation, ordr, P, X, Y)
    return fig


def Gauss(A=np.array([]), B=np.array([])):
    x = np.zeros(np.size(B))
    n = np.size(x)

    for k in range(0, n): #Permet de trigonaliser la matrice par la methode du pivot de Gauss
        for i in range(k+1,n):
            B[i] = B[i] - (A[i][k]/A[k][k])*B[k]
            for j in range(k+1, n):
                A[i][j] = A[i][j] - (A[i][k]/A[k][k])*A[k][j]
            A[i][k]=0

    x[n-1]=B[n-1]/A[n-1][n-1]
    u=np.array([n-1])
    for i in range(n-2, -1, -1): #Resout le systeme precedement trouve
        x[i] = (1/A[i][i])*(B[i]- np.sum(A[i][u]*x[u]))
        u = np.append(u, i)

    return x

