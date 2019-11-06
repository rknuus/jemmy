=====
jemmy
=====


An experimental decryption assistant supporting you in solving GeoCaching mysteries based
on encryption. Use at own risk.


Description
===========

Some GeoCaching mystery caches require you to crack encrypted data to find the final
coordinates (see http://www.geocaching.com). The tool eventually should support cracking of
some simple (and inherently insecure) codes and ciphers. Some procedures might be fully
automated, others interactive, and some require the correct key.


Usage
=====
* to list all available plugins: `jemmy -l`
* to run an analysis operation for a specific plugin: `jemmy -p GuessCipher -c "abcdef01234567" -a`
* to encrypt or decrypt using a specific plugin:
  * `jemmy -p Vigenere -m "abcdef01234567" -e -k "ba"`
  * `jemmy -p Vigenere -c "abcdef01234567" -d -k "ba"`
  * `jemmy -p Reverse -c "abcdef01234567" -d`


License
=======
Don't Be a Jerk: The [simple] Open Source [free-as-in-beer] Software License, see LICENSE.txt.


Note
====

This project has been set up using PyScaffold 2.2.1. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
