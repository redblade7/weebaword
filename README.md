# weebaword

**Weeb a Word v1.24 stable (20220604)**

Weeb a Word, created by redneonglow, is a Fediverse phrase bot which generates random otaku culture inspired phrases using an external dictionary file. It is inspired by the popular Loli a Word and Free Word Extremist bots, and has a mode to emulate Loli a Word.

Example phrases using the default dictionary from bsd-games-2.17 in Slackware Linux:

* negatively oppai
* shota pharmacopoeia
* loli reconstructing
* futa objection
* subbed trip
* harasses shota
* hentai cataloged
* joys pantsu
* dubbed believable
* protecc clarified

Example phrases using the Slackware settings above, but with Loli a Word emulation mode enabled:

* awaken loli
* vagary loli
* intermingled loli
* apportion loli
* throttle loli
* cookies loli
* quit loli
* deception loli
* enders loli
* hazes loli

Example phrases using the default dictionary from miscfiles-1.5-r3 in Gentoo Linux:

* weeaboo coinhabitant
* sidewalk cosplay
* otaku unfermenting
* anime trickishly
* loli pseudococcus
* protecc laborsaving
* weeb disinterment
* manga folkloristic
* apocinchonine bishoujo
* shoujo septotomy

By default, /usr/share/dict/words is used for the dictionary file, but this can be changed with the -d option. Weeb a Word randomly chooses a word from the dictionary file and converts the word to lower case prior to output/posting.

/usr/share/dict/words is usually provided by the "miscfiles" package in most Linux distributions. A sample public domain wordlist (WORD.LST) has also been included with this software. For best results, it is recommended to use the word list included with Slackware Linux's bsd-games package. You can download it here (remember to gunzip):

`http://ftp.slackware.com/pub/slackware/slackware64-15.0/source/y/bsd-games/hangman-words.gz`

Weeb a Word can post directly to Mastodon and Pleroma instances and is great for use in an hourly cronjob.

WARNING: Weeb a Word may generate phrases which are only suitable for "free speech" instances.

**REQUIREMENTS:**

* Python 3.6 or higher
* Mastodon.py and its dependencies
* curl

**SET UP THE TOKEN FILE:**

1. Create a Fediverse account for Weeb a Word.
2. Set up a token here: https://tinysubversions.com/notes/mastodon-bot/
3. Create a token file by running this command:
   `curl <command you are given> > tokenfile.json`

Note that if you change the password on the account, you will need to create a new token file.

**VISIBILITY:**

The visibility option may be any of the following:

* `direct` (only visible to the bot account)
* `private` (only visible to the bot account's followers)
* `public` (visible to everyone)
* `unlisted` (visible to everyone, but hidden from the public timeline)

In most cases you would want to use either `public` or `unlisted` for the visibility option.

**EXAMPLE COMMANDS:**

Show help: `./weebaword.py -h`

Show license (Simplified BSD): `./weebaword.py -c`

Show version: `./weebaword.py -v`

Print 1 phrase to stdout: `./weebaword.py -p 1`

Print 4 phrases to stdout, with Loli a Word emulation mode enabled, and using custom dictionary file /usr/share/dict/cracklib-small: `./weebaword.py -p 4 -d /usr/share/dict/cracklib-small -l`

Post to an account on Pleroma instance bae.st using token file tokenfile.json and public visibility:

`./weebaword.py -o https://bae.st tokenfile.json public`

Enjoy!

-redblade7 aka redneonglow

**FEDIVERSE CONTACT INFO:**

* `@redneonglow@bae.st` / https://bae.st/redneonglow (main)
* `@redneonglow@weeaboo.space` / https://weeaboo.space/redneonglow (backup)
* `@redneonglow@gameliberty.club` / https://gameliberty.club/@redneonglow (backup)
* `@redneonglow@poa.st` / https://poa.st/@redneonglow (backup)

The author runs an instance of Weeb a Word, generating phrases every half hour, here:

* `@weebaword@bae.st` / https://bae.st/weebaword

The author runs an instance of Weeb a Word, running in Loli a Word emulation mode, generating phrases every half hour, here:

* `@loliaword@bae.st` / https://bae.st/loliaword
