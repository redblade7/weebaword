#!/usr/bin/env python3
#
# Weeb a Word
#
# A Fediverse phrase bot generating random otaku culture inspired phrases.
#
# Copyright (c) 2020, redneonglow
# All rights reserved.
#
# Includes code from Dark Web Mystery Bot v4 stable (20200403)
# Copyright (c) 2019-20, redneonglow
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from mastodon import Mastodon,MastodonError
import argparse,json,secrets,sys

#program version
progver = "1-dev (20200706)"

#modifiers
modifier = ["anime","attacc","bishoujo","chippai","convention","cosplay","doujinshi","dubbed","ecchi","eroge","fandub","fanservice","fansub","fuku","futa","harem","hentai","husbando","idol","isekai","loli","magical girl","manga","mecha","moe","neko","oppai","otaku","pantsu","protecc","seinen","shonen","shota","shoujo","subbed","thicc","trap","visual novel","waifu","weeaboo","weeb","yaoi","yuri"]

#returns generated phrase
#filename = path/filename to dictionary file
#loli = boolean, true if loliaword mode is enabled
def genphrase(filename,loli):

   try:
        with open(filename,'r') as dictfile:
            dictionary = dictfile.read().splitlines()
   except OSError as err:
        print("ERROR:",err,file=sys.stderr)
        sys.exit(1)

   if loli:
        return str(secrets.choice(dictionary) + " loli").lower()
   else:

        coin = secrets.randbelow(2)

        if coin:
            return str(secrets.choice(modifier) + ' ' + secrets.choice(dictionary)).lower()
        else:
            return str(secrets.choice(dictionary) + ' ' + secrets.choice(modifier)).lower()

#returns the main version line as a string
#used in version and license commands
def verline():
    return str("Weeb a Word v" + progver)

#return part two of version info as string
def verpart2():
    return str("A Fediverse phrase bot by redneonglow.\nMore info: https://github.com/redblade7/weebaword")

#open json access token
def readtoken(token):
    try:
        with open(str(token)) as replyfile:
            json_obj = json.load(replyfile)
    except OSError as err:
            print("ERROR:",err,'\n')
            sys.exit(1)
    
    return json_obj["access_token"]

#shows version info
def optversion():
    print(verline())
    print(verpart2())

#shows license info
def optlicense():
    print(verline())
    print("\nCopyright (c) 2020, redneonglow\nAll rights reserved.\n")
    print("Includes code from Dark Web Mystery Bot v4-stable (20200403)\nCopyright (c) 2019-20, redneonglow\nAll rights reserved.\n")
    print("Redistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n")
    print("1. Redistributions of source code must retain the above copyright notice, this\n   list of conditions and the following disclaimer.")
    print("2. Redistributions in binary form must reproduce the above copyright notice,\n   this list of conditions and the following disclaimer in the documentation\n   and/or other materials provided with the distribution.\n")
    print("THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE\nFOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,\nOR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\nOF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.")

#post phrase to fediverse
#vis: Mastodon.py visibility setting (string)
#dictname: path/filename to dictionary file
#loli = boolean, true if loliaword mode is enabled
def optpostphrase(baseurl,token,vis,dictname,loli):

    try:
        mastodon = Mastodon(api_base_url=str(baseurl),access_token=readtoken(str(token)))
        mastodon.status_post(genphrase(str(dictname),loli),visibility=str(vis))
    except ValueError as err:
        print("ERROR:",err,'\n')
        sys.exit(2)
    except MastodonError as err:
        print("ERROR:",err,'\n')
        sys.exit(1)

    print("Successfully posted phrase to " + str(baseurl) + '!')

#prints phrase
#filename: path/filename to dictionary file
#loli = boolean, true if loliaword mode is enabled
def optprintphrase(filename,loli):
    print(genphrase(filename,loli))

#post version info to fediverse (unlisted)
def optpostver(baseurl,token):

    try:
        mastodon = Mastodon(api_base_url=str(baseurl),access_token=readtoken(str(token)))
        mastodon.status_post(verline()+'\n'+verpart2(),visibility="unlisted")
    except MastodonError as err:
        print("ERROR:",err,'\n')
        sys.exit(1)

    print("Successfully posted version info to " + str(baseurl) + '!')

#main
def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c","--license",help="Show license info",action="store_true")
    group.add_argument("-v","--version",action="store_true",help="Show version info")
    group.add_argument("-p","--printphrase",help="Print phrase to stdout NUM times",type=str,metavar="NUM")
    group.add_argument("-w","--postversion",help="Post version info once, unlisted, to Fediverse site SERVER using token file TOKEN.",type=str,nargs=2,metavar=("SERVER","TOKEN"))
    group.add_argument("-o","--postphrase",help="Post phrase once to Fediverse site SERVER using token file TOKEN and visibility value VISIBILITY.",type=str,nargs=3,metavar=("SERVER","TOKEN","VISIBILITY"))
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d","--dictionary",help="Use specified dictionary file (/usr/share/dict/words used if argument omitted)",type=str,nargs=1,metavar=("FILE"))
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--loli",help="Enable Loli a Word emulation mode",action="store_true")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)
    else:
        args = parser.parse_args()
        
        if args.license:
            optlicense()
        elif args.version:
            optversion()
        elif args.printphrase:

            try:
                times = int(args.printphrase)
            except ValueError: 
                print("ERROR: argument -p/--printphrase NUM must be whole number!\n")
                parser.print_help()
                sys.exit(2)

            if times < 1:
                print("ERROR: argument -p/--printphrase NUM must be 1 or greater!\n")
                parser.print_help()
                sys.exit(2)
            else:
                for count in range(0,times):
                    if args.dictionary:
                        optprintphrase(args.dictionary[0],args.loli)
                    else:
                        optprintphrase("/usr/share/dict/words",args.loli)
        elif args.postversion:
            optpostver(args.postversion[0],args.postversion[1])
        elif args.postphrase:
            if args.dictionary:
                optpostphrase(args.postphrase[0],args.postphrase[1],args.postphrase[2],args.dictionary[0],args.loli)
            else:
                optpostphrase(args.postphrase[0],args.postphrase[1],args.postphrase[2],"/usr/share/dict/words",args.loli)
        else:
            print("ERROR: Invalid command!\n")
            parser.print_help()
            sys.exit(2)

if __name__ == "__main__":
    main()
    sys.exit(0)
