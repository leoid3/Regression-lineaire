import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Button
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Regression_lineaire as rgl

gui.theme('Topanga')

titres=['X', 'Y']
nbpoint=2
defordre=2
mpl.use('TkAgg')

#################### Cronstruit la fenetre du plot ##################################
def dessiner(dessin, figure):
    fig= FigureCanvasTkAgg(figure, dessin)
    fig.draw()
    fig.get_tk_widget().pack(side='top', fill='both', expand=1)
    return fig

######################## Construit l'interface #################################
def creerInterface(nbp):
    interface=[
        [[gui.Text("Combien de points avez-vous ?", size=(23,1))]+ [gui.In(size=(14,1), enable_events=True, key="-POINT-")]+ [gui.Button("Modifier", enable_events=True, key="-MODIFIER-")]],
        [[gui.Text("Rentrez l'ordre de regression :", size=(23,1))]+ [gui.In(size=(14,1), enable_events=True, key="-ORDRE-")]],
        [gui.Text("Rentrez vos points ligne par ligne :", size=(25,1))],
        [[gui.Text('  ')]+[gui.Text(t, size=(14, 1)) for t in titres]],
        ]

    contenu = [
        [gui.In(size=(15,1),pad=(0,0), key=f"-INPUT{row}-{col}") for col in range(2)] for row in range(nbp)
        ]

    bouton = [
        [[gui.Button("Calculer", key="-CALCULER-")]+ [gui.Text('   ', size=(5,1))]+ [gui.Button("Reinitialiser", key="-REINI-")] + [gui.Text('   ', size=(5,1))]+ [gui.Button("Quitter")]]
        ]

    dessin=[
        [gui.Canvas(key="-DESSIN-")]
        ]

    layout= interface + contenu + bouton + dessin
    return layout

############################ Affiche la fenetre ##########################################

fig = plt.figure(figsize=(7,4))
ax=fig.add_subplot(111)
lay = creerInterface(nbpoint)
aff, aff2=gui.Window("Regression lineaire", lay, finalize=True), None
fig_agg = dessiner(aff["-DESSIN-"].TKCanvas, fig)

while True:
    window, event, values= gui.read_all_windows()

    if event == "Quitter" or event == gui.WIN_CLOSED: # Permet de gerer l'evenement du bouton "Quitter"
        if window==aff:
            aff.close()
        if window== aff2:
            aff2.close()      
        break
    
    elif event== "-MODIFIER-": # Permet de gerer l'evenement du bouton "Modifier"
        nbpoint=values["-POINT-"]
        if int(nbpoint) < 2:
            gui.Popup("Vous devez au minimun avoir 2 points pour faire une droite")
        else:
            if window==aff:
                aff.close()
            if window== aff2:
                aff2.close()              
            ax.cla()
            lay2 = creerInterface(int(nbpoint))       
            aff=gui.Window("Regression lineaire", lay2, finalize=True)
            fig_agg = dessiner(aff["-DESSIN-"].TKCanvas, fig)
            
            
    elif event== "-REINI-": # Permet de gerer l'evenement du bouton "Reinitialiser"
         if window==aff:
            aff.close()            
         if window== aff2:
            aff2.close()
         ax.cla()
         lay2 = creerInterface(int(nbpoint))       
         aff=gui.Window("Regression lineaire", lay2, finalize=True)
         fig_agg = dessiner(aff["-DESSIN-"].TKCanvas, fig)         
         

    elif event== "-CALCULER-": # Permet de gerer l'evenement du bouton "Calculer"      
        X=[]
        Y=[]
        ordre = defordre
        if values["-ORDRE-"]:
            ordre = int(values["-ORDRE-"])+1
        for i in range(int(nbpoint)):
            for t in range(2):
                if t== 0:
                    X.append(float(values[f"-INPUT{i}-{0}"]))
                elif t== 1: 
                    Y.append(float(values[f"-INPUT{i}-{1}"]))
        ax.cla()            
        ax=rgl.CalculMatrice(int(nbpoint), ordre, X, Y)
        fig_agg.draw()

