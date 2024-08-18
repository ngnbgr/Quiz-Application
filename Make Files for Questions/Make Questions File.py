# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:48:49 2024

@author: ngnba
"""

import tomli
# import tomli
with open("questions.toml", mode="rb") as toml_file:
    questions = tomli.load(toml_file)