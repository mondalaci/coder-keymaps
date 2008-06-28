#!/usr/bin/env python

from os import *
from os.path import *
from shutil import *

# autodetect directories

if geteuid() == 0:
    print 'Installing as super user.'
    print 'Defaulting to global installation.'
    shared_dir = '/usr/local/share/coder-keymaps'
    bin_dir = '/usr/local/bin'
    config_dir = '/usr/local/etc'
    doc_dir = '/usr/local/doc/coder-keymaps'
else:
    print 'Installing as normal user.'
    print 'Defaulting to local installation.'
    shared_dir = '~/.coder-keymaps'
    bin_dir = '~/bin'
    config_dir = '~/.coder-keymaps'
    doc_dir = '~/.coder-keymaps/doc'

# install

def install(type, sources, dest):
    print 'Installing', type, 'files to "' + dest + '":'

    if not isdir(expanduser(dest)):
        print '    Creating directory: "' + dest + '"'
        makedirs(expanduser(dest))

    for source in sources:
        copy(source, join(dest, source))

def copy(source, dest):
    if isdir(expanduser(source)):

        if not isdir(expanduser(dest)):
            print '    Creating directory: "' + dest + '".'
            makedirs(expanduser(dest))

        for file in listdir(source):
            copy(join(source, file), join(dest, file))

    elif isfile(source):
        print '    Installing file: "' + dest + '".'
        copyfile(source, expanduser(dest))
        chmod(expanduser(dest), stat(source).st_mode)

print

install('shared', ['keymaps'], shared_dir)
install('binary', ['chmap'], bin_dir)
install('configuration', ['chmap-keymap-list.conf'], config_dir)
doc_files = ['AUTHORS', 'COPYING', 'ChangeLog', 'README', 'README.hu', 'TODO']
install('documentation', doc_files, doc_dir)

print
print 'Installation successfully finished.'
print 'Open up your beer and enjoy the ride!'
