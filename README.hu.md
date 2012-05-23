Coder Keymaps
=============

A Coder Keymaps project hibrid billentyűzetkiosztásokat tartalmaz elsősorban nem-angol anyanyelvű programozók részére.

A probléma
----------

Bár a programozás sokkal gyorsabb angol billentyűzetkiosztással, néha rákényszerülünk a saját kiosztásunk használatára is.  Az a probléma, hogy a natív billentyűzetkiosztásunk több angol karaktert ír felül, mint amennyi feltétlenül szükséges lenne.

Például a magyar kiosztással a '=', '[', ']' karakterek (amelyek nagyon gyakran használatosak programozás során) és még néhány tucat másik karakter csak váltóbillentyűkön keresztül érhető el.  Az angol kiosztás használatával ezek a karakterek közvetlenül, váltóbillentyű használata nélkül elérhetőek.

Ideálisan a natív karaktereink néhány angol karaktert helyettesítenének és az eredeti karakterek elérhetőek lennének valamilyen váltóbillentyű segítségével.  Egy típikus nem-angol billentyűzetkiosztás azonban sok más billentyűt is felülír, a natív billentyűkön kívül még több tucatot.  Ez fölöslegesen bonyolítja a programozók életét, mert két különböző billentyűzetkiosztást kell fejben tartaniuk vagy gyakran kell váltaniuk közöttük.

A Coder Keymaps a fent említett ideális esetet valósítja meg.

Telepítés
---------

Futtasd az install.py fájlt.  Ha root-ként futtatod, az installálás globálisan megy végbe, míg ha hagyományos felhasználóként hajtod végre, az installálás a home könyvtáradba történik.

Használat
---------

A Coder Keymaps több billentyűzetkiosztást fájlt tartalmaz, például az us--hu-101-lat1.xmodmap fájlt.  Ez a kiosztás aktiválható az "xmodmap ./us--hu-101-lat1.xmodmap" paranccsal az azt tartalmazó könyvtárban. Minden ilyen kiosztás fájl két tényleges kiosztást tartalmaz.  A fenti esetben az első US angol (amit az "us" rész jelöl a fájlnévben), a második pedig magyar Latin-1 kódtáblával 101 gombos billentyűzetek részére (erre utal a "hu-101-lat1" rész a fájlnévben).

Minden billentyűzetkiosztás fájl neve [elsődleges_kiosztás]--[másodlagos_kiosztás].xmodmap formát követ, mint ahogy azt láthatod.  A két kiosztás közül az egyik mindig angol a programozás számára, a másik pedig az angol kiosztás felülírva a natív karakterekkel és csakis azokkal.  Amikor egy ilyen kiosztás fájlra váltassz, az elsődleges lesz aktív.

A másodlagos kiosztást kétféleképpen aktiválhatod, ideiglenesen és tartósan.  Ha a Windows billentyűt nyomvatartod és azzal együtt nyomsz meg egy másik billentyűt, (ideiglenesen) elérheted az utóbbi billentyű másodlagos kiosztását.  Ez általában akkor előnyös, ha a másodlagos kiosztás csak időnként akarod elérni.  Ha hosszabb időre akarod használni, akkor tanácsos (tartósan) átváltani az aktuális kiosztás fájl inverzére, aminek a neve [másodlagos_kiosztás]--[elsődleges_kiosztás].xmodmap.  Minden kiosztás fájlnak van inverze.

A chmap beállítása és használata
--------------------------------

Ha tartósan váltassz kiosztást, érdemes használnod a chmap programot. A chmap billentyűzetkiosztás fájlok egy listáját váltja körbe, amiket megadsz neki.  A konfigurációs fájlja a chmap-keymap-list.conf.  Ezt a fájlt az alábbi könyvtárakban fogja keresni elsőbbség szerint:

~/.coder-keymaps
/usr/local/etc
/etc

Az installálás alatt alapértelmezett konfigurációs fálj lett létrehozva, amit módosíthatsz.  Ebben a fájlban megadhatod a billentyűzetkiosztás fájlok listáját, amiket használni akarsz.  Ez a fájl egy kiosztás fájlt tartalmaz soronként, csak a fáljnév részt.

Az alapértelmezet konfigurációs fájl a következőt tartalmazza:

us--hu-101-lat1.xmodmap
hu-101-lat1--us.xmodmap

A munkamenet indulás beállítása
-------------------------------

GNOME alatt könnyen beállítható a munkamenet indulásakor a kezdeti billentyűzetkiosztás (az, ami a chmap-keymap-list.conf fájl elején szerepel):

1) Indítsd el a gnome-session-properties alkalmazást.

2) Válaszd ki az "Induló Programok" fület.

3) Nyomd meg a "Hozzáadás" gombot.

4) Írd be a "chmap -i" sort az "Induló parancs" mezőbe.

A chmap hozzárendelése az ablakkezelődhöz
-----------------------------------------

Miután minden úgy működik ahogy azt elvártad, hozzárendelheted a chmap-ot az ablakkezelőd egy gyorsbillentyűjéhez.

Én GNOME-ot használok, így csak az ezzel kapcsolatos megoldást tudom leírni.  A chmap szkriptnek az útvonaladban kell lennie ahhoz hogy működjön ebben az esetben.  Ahhoz hogy egy gyorsbillentyűhöz, például a Ctrl-Alt-Shit-J-hez rendeld, csináld a következőt:

1) Indítsd el a gconf-editor alkalmazást.

2) Nyisd meg az útvonalat: /apps/metacity/global_keybindings

3) Keress "run_command"-dal kezdődő kulcsnevet, ami egy számmal ér véget (hívjuk ezt a számot N-nek), amely kulcsnak az értéke "disabled".

4) Állítsd be a /apps/metacity/keybinding_commands/command_N (helyettesítsd N-t az előző számmal) kulcsot a "chmap" értékre.
