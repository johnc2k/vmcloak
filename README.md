VMCloak
=======

Automated Virtual Machine Generation and Cloaking for Cuckoo Sandbox.

Introduction
------------

VMCloak is a tool to fully create and prepare Virtual Machines that can be
used by Cuckoo Sandbox. In order to create a new Virtual Machine one should
prepare a few configuration values that will be used later on by the tool.

Dependencies
------------

VMCloak relies on a couple of tools and libraries that are required during
the process of generating a new VM.

* Python 2.6+
* mkisofs/genisoimage
* VirtualBox

Usage
-----

For a quick walkthrough on the general usage of VMCloak, please refer to the
following blogpost: [http://jbremer.org/vmcloak3][blogpost].

[blogpost]: http://jbremer.org/vmcloak3

Custom Mods
-----------

Mods added to the custom folder, I will eventually add these into the vmcloak
packages, manually applied for now.

* Win7
* Office 2010