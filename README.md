# POKEDEX 

___

## Pour les utilisateurs :zap:

### Information sur l'application :speech_balloon:

Application développer en python avec le framework django.
Ce framework étais à approfondir après les cours de python, nous somme donc parie sur cette technologie.

Réalisant une application WEB nous avons utilisé du SASS avec npm afin générer le CSS.
Cela permet de simplifier le development du CSS.

### Start de l'application :fire:

Lancer l'application il vous faut cloner le de depot git 

Pour du SSH
```shell
git clone git@github.com:Romain-Dfs/pokedex.git
```

pour du HTTPS
```shell
git clone https://github.com/Romain-Dfs/pokedex.git
```

Il vous faut lancer l'application par la suite
plusieurs commande sont possible, suivant comment votre python est installé

```shell
python3.8 pokedex/manage.py runserver

python pokedex/manage.py runserver

py pokedex/manage.py runserver
```


### Les routes 

Pour naviguer dans l'application vous pouvez utiliser les routes suivantes :

- la liste des Pokémons => http://127.0.0.1:8000/

- la liste des teams => http://127.0.0.1:8000/teams

- information sur un pokemon => http://127.0.0.1:8000/pokemon/<id>

- information sur une teams => http://127.0.0.1:8000/teams/<id>


___

## Pour les développeurs :construction_worker:

### Information sur l'application :speech_balloon:

L'application a été développée avec python3.8, en utilisant le framework django.

Les pages html utilise Gabarits, afin d'utiliser les variables.

Le CSS est généré avec SASS, utilisé avec npm.

### Environnement de travail :hammer:
Pour travailler sur l'application, il faut deux shells.

Le premier pour run le serveur

```shell
python3.8 pokedex/manage.py runserver
```

Le deuxième pour run le npm
```shell
nmp istall

npm start
```

