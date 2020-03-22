<img src="https://github.com/busybox11/probote/blob/master/Banner Probote.png?" alt="Banner" width="600px">

# probote
Un bot Discord pour Pronote qui utilise [l'API de Litarvan](https://github.com/Litarvan/pronote-api)

## Comment l'utiliser
- Installez `node`, `npm`, `python3` et `pip3`
- Clonez ce répertoire
- Clonez [l'API de Litarvan](https://github.com/Litarvan/pronote-api) repo
- Installez les dépendances (`pip3 install discord aiohttp html2text` pour ce répertoire, `npm i` pour celui de Litarvan)
- Modifiez `credentials.py` avec vos propres valeurs (comment le faire dans 'Comment modifier `credentials.py`')
- Démarrez l'API de Litarvan avec `node index.js`
- Démarrez ce bot avec `python3 main.py`

## Comment modifier `credentials.py`
Pour bien modifier `credentials.py`, voici les valeurs :
- `username` est votre nom d'utilisateur PRONOTE ou de votre ENT
- `password` est votre mot de passe PRONOTE ou de votre ENT
- `url` est votre URL PRONOTE (__SANS `eleve.html` !__)
- `cas` est l'URL de l'ENT (`"none"` si vous n'en avez pas, allez sur la page GitHub de [l'API de Litarvan](https://github.com/Litarvan/pronote-api) si vous n'êtes pas sûr de quoi mettre)
- `token` est votre token Discord
- `admin` est l'identifiant Discord de l'administrateur de Probote
- `probote_channel` est l'identifiant du salon public de Probote
Vous devez mettre ces valeurs entre des guillemets ou des apostrophes __sauf__ pour `admin` et `probote_channel` !

## Fonctionnalités
Ce Bot a une fonctionnalité principale, qui est la publication de messages dans le salon Probote lors d'ajout de devoirs. Elle est activée par défaut.
Cependant, il y a quelques commandes : Probote permet d'envoyer la moyenne de la classe pour la période actuele en utilisant les commandes `pro moy` ou `pro moyenne`.
Enfin (pour le moment), mais pas des moindres, vous pouvez "débugger" le bot, en utilisant les commandes `pro debug` (non documentées pour le moment, désolé).

## Fonctionnalités et améliorations futures
- Utiliser une approche plus modulaire dans le code
- Ajouter des fichiers et des commandes de configuration
- __Plus de documentation__ (je sais, désolé)
- Customiser certains aspects du bot

## Contact
En cas de besoin, vous pouvez me contacter sur Discord à `@busybox#2540`
