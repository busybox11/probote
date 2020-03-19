# probote
A Pronote Discord bot utilizing [Litharvan's API](https://github.com/Litarvan/pronote-api)

## How to use
- Install `node`, `npm`, `python3` and `pip3`
- Clone this repo
- Clone [Litharvan's API](https://github.com/Litarvan/pronote-api) repo
- Install dependencies (`pip3 install discord aiohttp` for this repo, `npm i` for Litharvan's API)
- Edit `credentials.py` with your own values (How-to under 'How to edit')
- Run Litharvan's API with `node index.js`
- Run this Bot using `python3 main.py`

## How to edit
To properly edit `credentials.py`, here are the values :
- `username` is your Pronote or CAS username
- `password` is your Pronote or CAS password
- `url` is your Pronote URL (__Without `eleve.html` !__)
- `cas` is your CAS URL (`"None"` if not using it, visit [Litharvan's API](https://github.com/Litarvan/pronote-api) if not sure)
- `token` is your Discord Bot token
- `admin` is your Probote administrator user ID
- `probote_channel` is your public Probote channel ID
