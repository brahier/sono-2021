from flask import Flask, render_template
import requests
import json
from jukebox import Jukebox

app = Flask(__name__)
jukebox = Jukebox()

VOL_RADIO = 10
VOL_JINGLE = 80

music = {
    "fribourg": ("http://radiofribourg.ice.infomaniak.ch:80/radiofribourg-high", VOL_RADIO),
    "swisspop": ("http://stream.srg-ssr.ch/m/rsp/mp3_128", VOL_RADIO),
    "rougefm": ("http://rougefm.ice.infomaniak.ch:80/rougefm-high", VOL_RADIO),

    "fusee": ("file:///home/pi/server/music/brahier-fusee.ogg", int(VOL_JINGLE * 0.6)),
    "formule": ("file:///home/pi/server/music/brahier-formule-magique.ogg", VOL_JINGLE),
    "psr": ("file:///home/pi/server/music/brahier-psr.ogg", VOL_JINGLE),
    "vite1": ("file:///home/pi/server/music/brahier-plus-vite-1.ogg", VOL_JINGLE),
    "vite2": ("file:///home/pi/server/music/brahier-plus-vite-2.ogg", VOL_JINGLE),
    "vite3": ("file:///home/pi/server/music/brahier-plus-vite-3.ogg", VOL_JINGLE),

    "entree": ("file:///home/pi/server/music/entree.mp3", VOL_JINGLE),
    "debut": ("file:///home/pi/server/music/debut.mp3", VOL_JINGLE),
    "distribution": ("file:///home/pi/server/music/distribution.mp3", VOL_JINGLE),
    "tour": ("file:///home/pi/server/music/tour.mp3", VOL_JINGLE),

    "feelgood": ("file:///home/pi/server/music/feelgood.mp3", VOL_JINGLE),
    "hennissement": ("file:///home/pi/server/music/hennissement.mp3", VOL_JINGLE),
    "thebest": ("file:///home/pi/server/music/thebest.mp3", VOL_JINGLE),

    "noel": ("file:///home/pi/server/music/noel.mp3", VOL_JINGLE),

    "ic-debut": ("file:///home/pi/server/music/intercantonal-debut.mp3", VOL_JINGLE),
    "ic-entree": ("file:///home/pi/server/music/intercantonal-entree.mp3", VOL_JINGLE),
    "ic-jingle": ("file:///home/pi/server/music/intercantonal-jingle-cypress.mp3", VOL_JINGLE),
    "ic-desole": ("file:///home/pi/server/music/intercantonal-jingle-desole.mp3", VOL_JINGLE),
    "ic-friend": ("file:///home/pi/server/music/intercantonal-jingle-friend.mp3", VOL_JINGLE),
    "ic-hennisssement": ("file:///home/pi/server/music/intercantonal-jingle-hennissement.mp3", VOL_JINGLE),
    "ic-mia": ("file:///home/pi/server/music/intercantonal-jingle-mia.mp3", VOL_JINGLE),
    "ic-ranz": ("file:///home/pi/server/music/intercantonal-jingle-ranz.mp3", VOL_JINGLE),
    "ic-tour": ("file:///home/pi/server/music/intercantonal-tour.mp3", VOL_JINGLE),
}

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/stop")
def stop():
    jukebox.stop()
    return "OK"

@app.route("/play/<name>")
def play(name):
    if name in music:
        m = music[name]
        jukebox.setVolume(m[1])
        jukebox.playUri(m[0])
        return "OK"
    else:
        return "NOT FOUND"
