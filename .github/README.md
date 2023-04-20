<p align="center">
    <a href=""><img src="https://github.com/devliftz/cover.src/blob/main/.github/hi.png?raw=true" alt=" " width="540"/></a>
</p>

<h1 align="center"><code>Cover 👻 (codename C0VR)</code></h1>

<h3 align="center"> A <b>free</b> and <b>open-source</b> multi-purpose discord bot. </h3>

<p id="badges" align="center">

</p>

## About

<h4 align="center">Development Stages</h4>

<p id="stages" align="center">

<a href="https://github.com/devliftz/C0VR/tree/dev">
  <kbd> <br> Nightly <br> <br> </kbd>
</a>
->
<a href="https://github.com/devliftz/C0VR/tree/overhaul">
  <kbd> <br> Canary <br> <br> </kbd>
</a>
->
<a href="https://github.com/devliftz/C0VR/releases">
  <kbd> <br> Stable <br> <br> </kbd>
</a>

</p>

**`Cover 👻`** (codename **`C0VR`**) is a **free** and **open-source** multi-purpose discord bot, that uses [lift](https://github.com/devliftz/lift.py) by DevLift Studios and Moderators, created for fun.

### Features

- Custom Command: allow your mods or member to create a custom command,  
  Custom command modes:
  - `0`: Only mods can add **and** manage custom commands
  - `1`: Member can add custom command but can only manage their own command
- Flags/Options: better specify your needs by using flags! (example: `?command disable category: info` will disable all command inside Information category)
- Fun commands: games, meme and other fun stuff.
- Powerful moderation command.
- Image manipulation/filters.
- Useful utility command such as `execute` (execute python/other programming language code), `google`, `calc` / `math`, and more!
- And more!

## Usage

### Quick Setup (Hosted)

Invite the officially hosted bot from this [invite link](https://discord.com/api/oauth2/authorize?client_id=1096484859477754008&permissions=8&scope=bot).

For information on how to use the bot, see https://bot.palembani.xyz/docs

### Self-Hosting

> **Note**
>
> If you're planning to self-host the bot, I'll assume you already have a
> decent knowledge of Python, discord.py and hosting bot in general. I will
> **NOT** give support for basic issue such as "Where do I get bot token", "How
> to install Python", etc.
>
> Hosting from free hosting such as Heroku is not supported either! It's
> recommended to get a proper VPS/Cloud Server to host a bot.

#### Manual

> **Warning**
>
> Python 3.10+ (3.10.9 is recommended) is required to host this bot!

- Download this repository by executing `git clone https://github.com/devliftz/cover.git`
  or click "Code" -> "Download ZIP"

   ```zsh
   # Windows
   pip install -r requirements.txt

   # Linux
   pip3 install -r requirements.txt
   ```

- Copy and paste (or rename) [`config.py-example`](../config.py-example) to `config.py`
- Edit all the necessary config value (`token` and `ownerid`)
- Run the bot by executing this command, `py main.py`
- If everything is setup properly, the bot should be online!

## Plans

>**Add YouTube music player**

## License

This bot is licensed under [**Mozilla Public License, v. 2.0 (MPL-2.0)**](/LICENSE)
