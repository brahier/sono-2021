import jukebox

def main():
    j = jukebox.Jukebox()
    j.setVolume(10)
    j.playUri("http://rougefm.ice.infomaniak.ch:80/rougefm-high")

if __name__ == "__main__":
    main()
