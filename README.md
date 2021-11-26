<h2 align="centre">Yukki Music Player</h2>

<h3>Requirements 📝</h3>

- FFmpeg (Latest)
- NodeJS [nodesource.com](https://nodesource.com/) (NodeJS 17+)
- Python (3.10+)
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls) (0.8.1rc1)
- [MongoDB](https://cloud.mongodb.com/) (3.12.1)
- [2nd Telegram Account](https://telegram.org/blog/themes-accounts#multiple-accounts) (needed for userbot)

### Commands 🛠
#### For all in group
- `/play` - reply to youtube url or song file to play song
- `/ytp <song name>` - play song without youtube url or song file (best method)
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details

#### Admins only
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play

### Commands for Sudo Users ⚔️
- `/userbotleaveall` - remove assistant from all chats
- `/gcast <reply to message>` - globally brodcast replied message to all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
- You can add a custom pmpermit message by adding var `PMMSG` and adding your message through env vars (for heroku, Settings/Edit vars)

+ Sudo Users can execute any command in any groups

# Yukki's music op

# DEPLOY

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/918127726/Yukki">
  <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-aqua?style=flat&logo=heroku" width="325" height="50.100" /></a></p>


