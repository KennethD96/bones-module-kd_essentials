# encoding: utf-8

module_name = "bones-module-kd"
module_version = "v0.0.2-NSFW"
module_date = "08.Feb 2014 16:50"

import os
import string, random
import time, datetime

import bones.event, logging
from bones.bot import Module, urlopener

mod_path = os.path.dirname(__file__)
etc_path = mod_path + "/etc/"
cache_path = mod_path + "/cache/"

arg_separator = ","

today = datetime.datetime.today()
logger = logging.getLogger(module_name)

def msg(event, string1, string2=False):
	"""If string2 is supplied string1 will be
	used as a prefix for the output.
	Note that empty lines will be ignored.
	Use a space if you need a empty line."""
	prefix = "\x0312[KD]"
	if len(string1.strip("\n")) >= 1:
		if string2 != False:
			for line in string2.split("\n"):
				if len(line) != 0:
					event("%s\x0315[%s]\x03 %s" % (prefix, string1, line))
		else:
			for line in string1.split("\n"):
				if len(line) != 0:
					event("%s\x03 %s" % (prefix, line))

def error(event, string):
	errPrefix = "\x034[Error]\x03 "
	for line in string.split("\n"):
		event.channel.msg(errPrefix + line)
	
def warn(event, string):
	warnPrefix = "\x038[Warning]\x03 "
	for line in string.split("\n"):
		event.channel.msg(warnPrefix + line)