# Can't currently make a hotkey for a builtin named command
#
# import pymel.core as pm
#
# Basic Usage
# x = hotkey('g')
# x.setup('whSetZero')
#
# Set Modifiers
# x = hotkey('g', alt=True, ctl=True, cmd=True)
# x.setup('whSetZero', name='SetZeroCommand', sourceType='mel', annotation='This is a command to set selected channels to their default values')
#
# Other Useful Functions
# pm.runtime.SavePreferences()
# pm.hotkey(factorySettings=True)

import pymel.core as pm

class hotkey:

	key = None
	alt = False
	ctl = False
	cmd = False
	shift = False
	release = False
	name = None
	command = None
	commandName = None
	sourceType = None
	annotation = None

	def __init__(self, key, alt=False, ctl=False, cmd=False, shift=False, release=False):

		from pydev import pydevd
		pydevd.settrace('localhost', port=7720, suspend=False)

		if not shift:
			if key.isupper():
				shift = True

		if shift:
			key = key.upper()

		self.alt = alt
		self.ctl = ctl
		self.cmd = cmd
		self.shift = shift
		self.release = release
		self.key = key

	def setup(self, command, name=None, sourceType='mel', annotation=''):
		"""Sets up hotkey linking the hotkey instance to the command."""
		
		if not name: # Default using first part of command if name is not explicitly given
			name = command.split()[0]

		self.name = name
		self.command = command
		self.sourceType = sourceType
		self.annotation = annotation

		# Build
		self.setupHotkey(self.name, sourceType)
		self.setupCommand(command, name, sourceType, annotation)

	def setupHotkey(self, name, sourceType='mel'):
		"""Sets up the hotkey and nameCommand only. This is useful when linking to a maya runtimeCommand."""
		
		self.name = name
		self.commandName = name + 'NameCommand' # Make names consistant with Maya's convention 
		self.sourceType=sourceType

		if self.release:
			pm.hotkey(k=self.key, alt=self.alt, ctl=self.ctl, cmd=self.cmd, rn=self.commandName)
		else:
			pm.hotkey(k=self.key, alt=self.alt, ctl=self.ctl, cmd=self.cmd, n=self.commandName)

		pm.nameCommand(self.commandName, ann=self.commandName, c=self.name, stp=self.sourceType)

	def setupCommand(self, command, name, sourceType, annotation):
		"""Makes the nameCommand and the runtimeCommand that is linked to by the hotkey"""

		pm.runTimeCommand(self.name, ann=self.annotation, cat='User', c=self.command, cl=self.sourceType)