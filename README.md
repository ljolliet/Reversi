# Reversi
Le projet Reversi a été réalisé aux mois de Novembre et Decembre 2019 par [Louis Sicardon](https://github.com/louissicardon) 
et [Louis Jolliet](https://github.com/ljolliet/). Le [dépot](https://github.com/ljolliet/Reversi) de ce projet 
sera rendu public après le rendu de celui ci soit au *20 Décembre 2019*.

## Heuristique
### Calcul
Notre heuristique prend en paramètre les facteurs suivants : 
- **Les coins**  : la capture des coins est essentielle dans le reversi. Capturer un coin, même si 
cela ne garantit rien, est un fort avantage pour la suite du jeu. L'heuristique calcul le nombre de coins pour chaque joueur
- **La mobilité** :  le but de cette heuristique est de maximiser notre nombre de coups possibles et minimiser le nombre de coups
de l'adversaire. Dans les meilleurs cas, cela peut amener à empêcher totalement l'adversaire de jouer. Pour ce faire, on calcul le 
nombre de coup possible pour chaque joueur.
- **La parité** : essentiellement utilisé à la fin du jeu, cette heuristique calcul le nombre de pions pour chaque joueur.
- **La stabilité** : on compte le nombre de pièces stables et non stables et on souhaite maximiser la différence. Une pièce stable est 
une pièce qui ne pourra pas être capturée par l'adversaire jusqu'à la fin du jeu. Cet algorithme effectue le calcul de manière naïve

Pour chacune des heuristiques, on calcul une valeur à partir d'une valeur amie et une valeur ennemie qui sera renvoyer.
L'heuristique finale exécute ces heuristiques et applique des coefficients aux valeurs obtenues. Les heuristiques et les coefficients
utilisés évoluent en fonction du temps de jeu.

### Phases de jeu
- Debut de partie : Au tout début du jeu, nous utilisons une **bibliothèque d'ouverture**, puis nous évaluons uniquement la mobilité et le nombre de coins. En effet, le score n'importe que très peu au début, tout comme la stabilité qui n'intervient que plus tard car il n'y a quasiment aucune pièce stable en début de partie. De plus, c'est l'heurisitque qui demande le plus de calcul, de ce fait, il est bon de ne pas l'utiliser inutilement en début de partie.
- Milieu de partie : Au milieu de la partie, on utilise les heuristiques de coin, de mobilité, de score et de stabilité.
- Fin de partie : A la fin de la partie, nous utilisons les mêmes heuristiques que précédemment mais avec des coefficients différents.
 
## Exploration de l'arbre de jeu
### Algorithme
Nous avons commencé par utiliser un simple MiniMax que nous avons ensuite amélioré en Alpha-Beta.
Nous utilisons par défaut une profondeur de 3 mais elle peut évoluer dans le temps.

### Raccourcis
Pour essayer de diminuer la complexité nous avons ajouté des raccourcis. En effet, lorsqu'un coin est prenable ou qu'il est possible de bloquer l'adversaire lors de son prochain coup, on ne parcours pas l'arbre de jeu
et le coup en question est directement retourné. Cela évite des parcours inutiles, pour des coups qu'un humain trouverait "évident". 

### Utilisation de Threads
Pour réduire le temps de calcul nous avons implémenté une **solution de multithreading**, qui calcule l'alphabeta à travers différents threads, séparé lors du premier niveau de l'algorithme. A priori, pour le tournoi c'est inutile car il n'y aura qu'un coeur disponible, mais pour nos tests, on obtient une rapidité supérieur de quasiment 40%.
Pour le rendu nous allons désactiver cette option pour éviter des copies inutiles qui coûtent cher en temps.

## Méthode de travail
### Evaluateurs
Pour comparer un maximum les heuristiques, nous avons créé une classe abstraite Evaluator que nous dérivons avec plusieurs évaluateurs utilisant différentes métadonnées comme poids des heuristiques. 
De ce fait nous pouvions les faire s'affronter pour déterminer la plus efficace. Nous avons déterminé les poids en nous documentant, puis par tâtonnement.
### Benchmark
Nous avons créé un fichier permettant de faire s'affronter plusieurs fois 2 joueurs, en aller-retour. C'est ce qui nous a permis de comparer réellement deux évaluateurs, mais aussi de constater nos performances face au joueur de nos camarades.
## Bibliographie
Voici un lien vers l'ensemble de nos insprations pour ce projet.
- http://play-othello.appspot.com/files/Othello.pdf
- https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
- https://github.com/kartikkukreja/blog-codes/blob/master/src/Heuristic%20Function%20for%20Reversi%20(Othello).cpp
- https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/
- https://github.com/arminkz/Reversi/
- https://studylibfr.com/doc/6062702/algorithme-minmax-%E2%80%93-%C3%A9lagage-alphabeta-1-introduction-2-mi... page 8
- https://digitalcommons.lsu.edu/cgi/viewcontent.cgi?article=1766&context=gradschool_theses pages 18-20
