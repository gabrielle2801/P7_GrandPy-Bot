# READ ME
### GrandPy Bot
Les grands-pères ont toujours une histoire à nous raconter autour d'un seul mot.
Une adresse, un lieu et les voilà parti dans de longues discours concernant la destination.

_______________________________
**Cahier des charges**

Créer un GrandPyBot, une sorte de Papy-Robot qui raconterai l'histoire selon une adresse ou un lieu.
_______________________________
**Comment installer le programme**
Il faut tout d'abord créer un environnement virtuel
``` shell
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate
```
Puis installer les paquets Python
``` shell
pip install -r requirements.txt
```
_______________________________

**Description du parcours utilisateur**

*Customer Journey*

L'utilisateur ouvre son navigateur et découvre la page avec un formulaire.
Il tape une question conernant le lieu ou l'adresse qu'il désire dans le champ du formulaire.
**Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?**
Il clique sur le bouton envoyer (le bouton tourne qui indique que GrandPy est en train de réfléchir)
Un message apparaît **Bien sûr mon poussin ! La voici : 10 Quai de la Charente, 75019 Paris, France**
Puis le lieu est indiqué sur une carte. Un nouveau message est indiqué concernant l'histoire du lieu.
**Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?...**

________________________________
**Fonctionnalités**

* Intéraction en AJAX
* Utilisation API google Maps et celle de Media Wiki
* Tests utilisant des mocks pour les API
* Mise en ligne avec Heroku
_____________________________

Méthode Agile -> Users Stories / Tableau de tâches et sous tâches sur Trello :
https://trello.com/b/rek6xyIl/p7-grandpy-bot

Heroku -> https://grandpy-bot-gabrielle.herokuapp.com/



