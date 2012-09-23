Coder Keymaps
=============

The Coder Keymaps project consists of hybrid keyboard maps intended chiefly for non-English programmers.

_Note_: This project has been closed.  [See why](http://monda.hu/blog/2009/11/09/coder-keymaps-closed/).

The Problem
-----------

Note: The rest of this document relates to programmers whose mother tongue is other than English.

However programming is far more faster with English keymaps, sometimes we must use our native keyboard maps too.  The problem is that our native keymaps overdefine more English characters than necessarily sufficient.

For examle using the Hungarian mapping one can only reach the '=', '[', ']', characters (which are essential in programming) and dozens of other characters via alternate keys (Shift, Alt).  With the English keymap these keys are accessible instantly without any alternating keys.

Ideally our native characters should replace some English characters and the original English characters would be accessible via some alternate key.  A typical non-English keyboard map however rebinds dozens of other keys over the native ones, including almost every non-alfanumeric characters.  This unneccesarily complicates our job because we need to learn two distinct keyboard maps or we need to change often between them.

Coder Keymaps implements the above mentioned ideal solution for us.

Installation
------------

Run install.py.  Running it as root the installation will be global and if you run it as an ordinary user it will install itself locally to your home directory.

Use
---

There are a set of keymap files included in Coder Keymaps.  For example us--hu-101-lat1.xmodmap.  This keymap can be activated with "xmodmap ./us--hu-101-lat1.xmodmap" in its directory.  Every such keymaps contain two actual mappings.  In the above case, the first is US English (signifies the "us" part in the filename), and the second is Hungarian with Latin-1 coding table for 101 character keyboards (the "hu-101-lat1" part).

The filename of a keymap file is [primary_keymap]--[secondary_keymap].xmodmap as you can see.  One of the two mappings is always English for programming and the other is the English keymap overdefined with non-english native characters and only with those.  When you change to such a keymap, the primary keymap will be active.

You can activate the secondary keymap in two ways, temporarily and permamently.  If you keep a Windows key pressed while pressing a key, you can reach the second map (temporarily).  This is generally useful if you use the secondary mapping for a shorter period.  You can also reach the second keymap for a longer period (permamently) by changing to the invert keymap file of the map you are currently using named [secondary_keymap]--[primary_keymap].xmodmap.  Every map file has its invert.

Using and configuring chmap
---------------------------

For permamently changing maps, you can use the chmap utility.  chmap rotates a list of maps you define.  It has a configuration file called chmap-keymap-list.conf.  It will look for this file in the following directories by priority:

~/.coder-keymaps
/usr/local/etc
/etc

During the installation a default configuration file had been created which you can alter.  In this configuration file you can list the map files that you want to use.  This file consist one map per line, only the filename part.

The default configuration file looks like this:

us--hu-101-lat1.xmodmap
hu-101-lat1--us.xmodmap

Configuring session startup
---------------------------

In GNOME, one can initialize his/her preferred keyboard map (the first entry in chmap-keymap-list.conf) at session startup in the following way:

1. Start the gnome-session-properties application.

2. Select the "Startup Programs" tab.

3. Press the "Add" button.

4. Type "chmap -i" in the "Startup Command" text entry.

Binding chmap to your window manager
------------------------------------

After everything works as you expected, you can finally bind chmap to
a hotkey of your window manager.

I use GNOME, so I can only show you the GNOME way.  The chmap script
must be in your path in order to work in this case.  To bind chmap to
a hotkey, like Ctrl-Alt-Shift-J, do the following:

1. Execute the gconf-editor application.

2. Open the path: /apps/metacity/global_keybindings

3. Search for a key with a name that begins with "run_command" and ends with a number (let's call it N) whose value is "disabled".  Change its value to "j".

4. Change the key /apps/metacity/keybinding_commands/command_N (replace N with the number above) to the value "chmap".
