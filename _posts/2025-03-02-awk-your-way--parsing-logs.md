---
title: AWK Your Way Parsing Logs
layout: post
date: 2025-03-02
permalink: /2025/03/02/awk-your-way-parsing-logs/
category:
    - Shell
    - AWK
excerpt: |
    Learn how to use AWK in practice! Let's parse Quake 3 logs to display players in a match, 
    player score card, and death cause report.
---

It is a [common][1] [challenge][2] for _technical interviews_ to parse Quake 3 
server logs and display:

1. Players in a match
2. Player score card, listing player names and kill count:
	1. Ignore `<world>` as a _player_
	2. If `<world>` kills a _player_, add `-1` to _player_'s kill count
3. (optional) Group _outputs_ above by _match_
4. (optional) Death cause report by _match_

Working with files is a common practice for any developer. Using [awk][] not so 
much, even though it is IMHO one of the best tools for doing so:

- The language is built for (1) text matching and (2) manipulation.
- Working with small files is as easy as it is working with very large files.

Intending to spread the knowledge of the [tool][awk] to more people, let's solve 
the challenge with [AWK][] and get to know how you can effectively start using it 
today in your workflow. I assume you know well a programming language, your way 
around a (\*nix) CLI and that we are using [GNU awk][awk].

[1]: https://gist.github.com/augustohp/029f20ec3dd97377666cf8ed1e5361e7
[2]: https://github.com/misaku/QuakeLogParser/blob/master/DOC/DESAFIO.md
[awk]: https://www.gnu.org/software/gawk/manual/gawk.html

## The beginning of a not so usual program

As it is common with other Unix tools, it is better to break the program into 
smaller pieces, [Awk][] programs [bigger than ~150 lines are difficult to 
maintain][3]. 
Here are the different programs we are going to create:

1. `clean.awk` will read _input_ files, which are the original [log][] files, 
   and _output_ a cleaner version of their content. 
   Containing just the data we need to manipulate and use.
2. `scoreboard.awk` will use the _output_ from the previous _program_ to produce 
   the score boards for each game.

[3]: https://www.gnu.org/software/gawk/manual/html_node/When.html#:~:text=If%20you%20find%20yourself%20writing%20awk%20scripts%20of%20more%20than%2C%20say%2C%20a%20few%20hundred%20lines%2C%20you%20might%20consider%20using%20a%20different%20programming%20language.
[log]: https://gist.githubusercontent.com/cloudwalk-tests/be1b636e58abff14088c8b5309f575d8/raw/df6ef4a9c0b326ce3760233ef24ae8bfa8e33940/qgames.log

Let's create a _walking skeleton_ to run and debug our progress while tackling 
the challenge:

```bash
$ mkdir /tmp/awk-quake
$ cd !$
$ curl --remote-name -L https://gist.githubusercontent.com/cloudwalk-tests/be1b636e58abff14088c8b5309f575d8/raw/df6ef4a9c0b326ce3760233ef24ae8bfa8e33940/qgames.log
$ tail qgames.log
 13:55 Kill: 3 4 6: Oootsimo killed Dono da Bola by MOD_ROCKET
 13:55 Exit: Fraglimit hit.
 13:55 score: 20  ping: 8  client: 3 Oootsimo
 13:55 score: 19  ping: 14  client: 6 Zeh
 13:55 score: 17  ping: 1  client: 2 Isgalamido
 13:55 score: 13  ping: 0  client: 5 Assasinu Credi
 13:55 score: 10  ping: 8  client: 4 Dono da Bola
 13:55 score: 6  ping: 19  client: 7 Mal
 14:11 ShutdownGame:
 14:11 ------------------------------------------------------------
$ cat clean.awk
{ print }
$ watch gawk -f parse.awk qgames.log
```

Above we:

1. Downloaded `qgames.log`
2. Created `clean.awk` that prints everything passed to it
3. Executed the program every couple of seconds (with `watch`) to see its result 
   while we change it in another session (to stop `watch`, use <kbd>CTRL-C</kbd>)

Let's change `clean.awk` to filter just the lines useful to us, and help us debug 
what to do with them:

```awk
BEGIN {
    FS = " "
    LFS = "\n"
}
/Init/ { print }
/kill/ { debug_fields() }

function debug_fields()
{
    for (i = 1; i <= NF; i++) {
        printf("%d: %s\n", i, $i)
    }
}
```

Don't despair yet, it is pretty simple what we are doing:

1. `BEGIN` is a _special block_, that gets executed **once** at the start 
   of the parsing:
	1. We use it to (re-)define some _special variables_:
		1. `FS` defines the **field separator** (space). It is used to break 
		   a _matching line_ into a smaller array of objects.
		2. `LFS` defines the **line separator** (new line). Everything until 
		   that character will be treated as a _line_.
2. `/match/ { action }` blocks execute a set of `actions` when a `match` (regex supported) is found:
	1. `/Init/ { print }` prints every line that has `Init` on it, without doing anything more.
	2. `/kill/ { debug_fields() }` executes the `debug_fields()` function for every line that has a matching `kill` string on it.
	3. Every line that doesn't match the rules above is ignored.
3. `function debug_fields()` prints all fields identified after breaking the _line_ with `FS`:
	1. `NF` is a _special variable_ containing the _number of fields_ parsed for the current line.
	2. `$n` is the _field_ `n` parsed. Inside the _loop_ `$i` will become `$1`, 
	   `$2` and `$3` allowing us to retrieve the contents of every field on that 
	   line, displaying something like:

		```
		1: 20:54                                     
		2: Kill:
		3: 1022
		4: 2
		5: 22:
		6: <world>
		7: killed
		8: Isgalamido
		9: by
		10: MOD_TRIGGER_HURT
		```
	3. The _output_ above is useful to debug the current line contents we can work with. 
       Try changing `debug_fields()` _action_ to `print $6 " killed " $8`.

With little changes, we can use `$6` (killer) and `$8` (killed) to display who 
killed who, which is pretty much everything we need.

🐛 If player names would not contain spaces we'd be ready. But `Assassinu Credi`, for example, 
breaks our algorithm because we use _spaces_ to separate fields. 
When he kills someone `$8` will `killed` instead of the other player name. 

Let's see this happening:

```awk
BEGIN {
    FS = " "
    LFS = "\n"
}
/Init/ { next }
/Assas/ { print $6 " killed " $8 }
```

The program above ignores (with `next` action) lines matching `Init` and prints 
just lines matching `Assas`.

```bash
$ awk -f clean.awk qgames.log
Zeh killed Assasinu
<world> killed Assasinu
Isgalamido killed Assasinu
Zeh killed Assasinu
Assasinu killed killed
```

Note that `Assasinu killed killed` line is wrong. It doesn't have the name of 
the _killed_ player. Let's fix this!

## Making things more reliable with regex

The end `clean.awk` program is below. It _substitutes_ some strings by `nfs` 
(new file separator) variable and removes the prefix on lines that notifies 
of a kill:

```awk
BEGIN {
    FS = " "
    LFS = "\n"
    nfs = "|"
    current_game = 0
}
/Init/ { current_game++ }
/kill/ {
    sub(/^[ 0-9:]+ Kill: [0-9: ]+/, "", $0)
    sub(/ killed /, nfs, $0)
    sub(/ by /, nfs, $0)
    print $0 nfs current_game
}
```

1. On the `BEGIN` section, declares 2 new variables:
	1. `nfs` to separate output by something other than spaces, so next programs 
	    easily support player names with them.
	2. `current_game` is a variable that gets incremented every time a new game starts.
2. `/Init/` marks a new game:
	1. Increments the variable `current_game` for the next time it gets used
3. For every `/kill/`:
	1. `sub(regex, replacement, target)` will put `replacement` into every matching 
	   `regex` on `target`, replacing `target`. `$0` is the whole current line.
	2. `sub(/^[ ...` removes the prefix of the line until the player name.
	3. `sub(/ by...` and `sub(/ killed...` replaces these matches by `nfs` (the 
	    new field separator), allowing us to easily identify (`$1`) the killer, 
		(`$2`) who got killed and (`$3`) how he got killed.
	4. `print` will print the current line (`$0`) with the _current game_ as a suffix:
		- As every `sub()` replaces the current line (`$0`), we now have only 
		  what we needed.
		- As [awk][] programs operate on lines, it is easier to have everything 
		  we need on them. That is why we add _current game_ to every line.

Executing the program above, produces:

```bash
$ awk -f clean.awk qgames.log | tee qgames-clean.log
<world>|Isgalamido|MOD_TRIGGER_HURT|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
Isgalamido|Mocinha|MOD_ROCKET_SPLASH|2
Isgalamido|Isgalamido|MOD_ROCKET_SPLASH|2
Isgalamido|Isgalamido|MOD_ROCKET_SPLASH|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
<world>|Isgalamido|MOD_FALLING|2
<world>|Isgalamido|MOD_TRIGGER_HURT|2
Isgalamido|Mocinha|MOD_ROCKET|3
<world>|Zeh|MOD_TRIGGER_HURT|3
```

With the `qgames-clean.log` file we can now easily achieve every objective of 
the original challenge without having to deal with:

- Unneeded context.
- Space separators. With `FS = "|"` we use `|` as _field separator_ and have:
	- `$1` as the killer
	- `$2` who got killed
	- `$3` how _killer_ killed _killed_
	- `$4` in which game that happened
- A "checkpoint". If the log changes format, or we discover a bug, as long we 
  produce an _output_ conforming the current format we are good to use the next 
  programs.

## Next steps

How about you try to figure out the rest? I will post my solution and, if you 
learned something from this, I promise you will learn something else on the next 
one as well.

The [Gnu awk's manual][awk] is **really** good - from a time technical documents 
were worth reading. You don't need to read everything, the _index_ will take you 
where you need. Pinky promise! 

I won't leave you without anything though, here is a beginning for `scoreboard.awk`:

```awk
BEGIN {
    FS = "|"   
}
{
    # Sets a player as a key in the players array
    players[$1] = $1
    players[$2] = $2
}
END {
    # Removes <world> from players
    for (name in players) {
        if (name == "<world>")
            continue
        print name
    }
}
```

Let me know of your solution, suggestions or doubts in the comments! ❤️

<!--
vim: spell spelllang=pt
-->
