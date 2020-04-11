<img src="https://github.com/busybox11/probote/blob/master/Banner Probote.png?" alt="Banner" width="600px">

# probote
Un bot Discord qui informe de ce qu'il se passe sur Pronote grâce à [l'API de Litarvan](https://github.com/Litarvan/pronote-api).

## Comment l'utiliser
- Installez `node`, `npm`, `python3` et `pip3`.
- Clonez ce répertoire.
- Clonez le repo de [l'API de Litarvan](https://github.com/Litarvan/pronote-api).
- Installez les dépendances (`pip3 install discord aiohttp html2text validators` pour ce répertoire, `npm i` pour celui de Litarvan).
- Modifiez `credentials.py` avec vos propres valeurs (voir la section suivante).
- Démarrez l'API de Litarvan avec `node index.js`.
- Démarrez ce bot avec `python3 main.py`.

## Comment modifier `credentials.py`
Pour bien modifier `credentials.py`, voici les valeurs :
- `username` est votre nom d'utilisateur PRONOTE ou de votre ENT
- `password` est votre mot de passe PRONOTE ou de votre ENT
- `url` est votre URL PRONOTE (__SANS `eleve.html` !__)
- `cas` est l'URL de l'ENT (`None` si vous n'en avez pas, voir la page GitHub de [l'API de Litarvan](https://github.com/Litarvan/pronote-api) pour plus de détails)
- `token` est le token de votre bot Discord
- `admin` est l'identifiant Discord de l'administrateur de Probote
- `probote_channel` est l'identifiant du salon public de Probote
Vous devez mettre ces valeurs entre des guillemets ou des apostrophes __sauf__ pour `admin` et `probote_channel` !

## Fonctionnalités
Ce bot envoit un message à chaque fois qu'un nouveau travail à faire est ajouté ou qu'une information est envoyée au compte Pronote qui est connecté.

## Fonctionnalités et améliorations futures
- Envoyer les longs textes sur plusieurs messages au lieu de les tronquer pour respecter la limite de cractères sur Discord.
- Prévenir quand du "Contenu de cours" est ajouté sur Pronote.
- Publier les messages envoyés dans l'onglet "Discussions" de Pronote.

## Contact
En cas de besoin, vous pouvez me contacter (`busybox#2540` sur Discord) ou un ami qui m'aide dans ce projet (`ribt#9334`).
