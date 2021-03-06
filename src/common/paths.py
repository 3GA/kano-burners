#!/usr/bin/env python

# paths.py
#
# Copyright (C) 2014,2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
#
# Paths used throughout the project
#
# We create path constants for resources and windows tools, as well as
# detecting whether we are running from source or a PyInstaller bundle.
# This is important when setting the base path of the project.


import os
import sys


# the current working directory differs when we are running from a PyInstaller bundle
if getattr(sys, 'frozen', False):
    # running from PyInstaller bundle
    base_path = os.path.abspath(sys._MEIPASS)
else:
    # running from source
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


# setting a Temp directory path
temp_path = os.path.join(base_path, 'temp')
if not os.path.exists(temp_path):
        os.makedirs(temp_path)

# setting Resources paths - css and images
res_path = os.path.join(base_path, 'res')
images_path = os.path.join(res_path, 'images')
anim_path = os.path.join(res_path, 'animations')
css_path = os.path.join(res_path, 'CSS')

# setting Windows Tools paths
win_tools_path = os.path.join(base_path, 'win')
_7zip_path = os.path.join(win_tools_path, '7zip')
_dd_path = os.path.join(win_tools_path, 'dd')
_nircmd_path = os.path.join(win_tools_path, 'nircmd')
_aria2_win_path = os.path.join(win_tools_path, 'aria2', 'aria2c.exe')

# setting OSx Tools paths
osx_tools_path = os.path.join(base_path, 'osx')
_aria2_osx_path = os.path.join(osx_tools_path, 'aria2', 'aria2c')
