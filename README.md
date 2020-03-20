# probote
A Pronote Discord bot using [Litarvan's API](https://github.com/Litarvan/pronote-api)

## How to use
- Install `node`, `npm`, `python3` and `pip3`
- Clone this repo
- Clone [Litarvan's API](https://github.com/Litarvan/pronote-api) repo
- Install dependencies (`pip3 install discord aiohttp` for this repo, `npm i` for Litharvan's API)
- Edit `credentials.py` with your own values (How-to under 'How to edit')
- Run Litharvan's API with `node index.js`
- Run this Bot using `python3 main.py`

## How to edit
To properly edit `credentials.py`, here are the values :
- `username` is your Pronote or CAS username
- `password` is your Pronote or CAS password
- `url` is your Pronote URL (__Without `eleve.html` !__)
- `cas` is your CAS URL (`"none"` if not using it, visit [Litarvan's API](https://github.com/Litarvan/pronote-api) if not sure)
- `token` is your Discord Bot token
- `admin` is your Probote administrator user ID
- `probote_channel` is your public Probote channel ID
You need to add double or single quotes for all values __except__ for `admin` and `probote_channel` !

## Bot features
This bot has a main feature : which is channel notifications for new homeworks. It is enabled by default.
However, it has some more command : actual trimester average retrieving, using the `pro moy` or `pro moyenne` command.
Last (at the moment), but not least, you can debug the bot, using the `pro debug` command (undocumented at the moment, sorry).

## Future improvements
- Using a more modular approach
- Adding a config file
- __More documentation__ (I know)
- Easy customization
