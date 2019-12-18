# Reversi
Le projet Reversi a été réalisé aux mois de Novembre et Decembre 2019. C'est un projet réalisé par [Louis Sicardon](https://github.com/louissicardon) et [Louis Jolliet](https://github.com/ljolliet/). Le [dépot](https://github.com/ljolliet/Reversi) de ce projet 
sera rendu public après le rendu de celui ci au *20 Décembre 2019*.

### Todo
- [x] basic weights
- [x] corners
- [x] mobility
- [ ] stability
- [x] parity
- [x] diff
- [x] Opening Book
- [ ] hashTable that remember some moves calculation
- [x] game phases with different heuristic for each
- [ ] change depth with game time
- [ ] use threads
##Heuristique
###Calcul
Notre heuristique prend en paramètre les facteurs suivants : 
- **Les coins** 
- **La mobilité** 
- **La parité**
- **Le score** :  essentiellement utilisé à la fin du jeu, cette heuristique retourner la différence de score entre les deux joueurs.

Notre heurisitique finale est un ensemble de toutes ces sous-heuristiques avec des poids différents. Ces poids évoluent en fonction du temps de jeu.

###Phases de jeu
- Debut de partie : Au tout début du jeu, on utilise une **bibliothèque d'ouverture**, puis nous évaluons .. #TODO
- Milieu de partie :
- Fin de partie :
 
## Exploration de l'arbre de jeu
### Algorithme
Nous avons commencé par utiliser un simple MiniMax que nous avons ensuite amélioré en Alpha-Beta.
Nous utilisons par défaut une profondeur de 3 mais elle peut évoluer dans le temps.

### Raccourcis
Pour essayer de diminuer la complexité nous avons ajouté des raccourcis. En effet, lorsqu'un coin est prenable ou qu'il est possible de bloquer l'adversaire lors de son prochain coup, on ne parcours pas l'arbre de jeu
et le coup en question est directement retourné. Cela évite des parcours inutiles, pour des coups qu'un humain trouverait "évident". 
### Bibliographie
Voici un lien vers l'ensemble de nos insprations pour ce projet.
- http://play-othello.appspot.com/files/Othello.pdf
- https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
- https://github.com/kartikkukreja/blog-codes/blob/master/src/Heuristic%20Function%20for%20Reversi%20(Othello).cpp
- https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/
- https://github.com/arminkz/Reversi/
- https://studylibfr.com/doc/6062702/algorithme-minmax-%E2%80%93-%C3%A9lagage-alphabeta-1-introduction-2-mi... page 8
- https://digitalcommons.lsu.edu/cgi/viewcontent.cgi?article=1766&context=gradschool_theses pages 18-20
