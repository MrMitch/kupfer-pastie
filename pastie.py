# -*- coding: UTF-8 -*-

__kupfer_name__ = _("Paste to pastie.org")
__kupfer_sources__ = ("ClipboardSource", )
__kupfer_actions__ = (
	"PastieObjectiveC_CPP", "PastieActionScript", "PastieRuby", "PastieRoR", "PastieDiff", "PastiePlainText",
	"PastieC_CPP", "PastieCSS", "PastieJava", "PastieJavascript", "PastieHTML_XML", "PastieHTML_ERB_Rails",
	"PastieBashShell", "PastieSQL", "PastiePHP", "PastiePython", "PastieErlang", "PastiePascal", "PastiePerl",
	"PastieYAML", "PastieCSharp", "PastieGo", "PastieApacheConfig", "PastieLua", "PastieIO", "PastieLispCommon",
	"PastieD", "PastieTeX", "PastieFortran", "PastieHaskell", "PastieLiterateHaskell", "PastieMakefile", "PastieScala",
	"PastieScheme", "PastieSmarty", "PastieINI", "PastieNu", "PastieClosure", "PastiePuppet", "PastieCoffeeScript",
)

SYNTAXES = [
	'Objective-C/C++', 'ActionScript', 'Ruby', 'Ruby on Rails', 'Diff', 'Plain text', 'C/C++', 'CSS', 'Java',
	'Javascript', 'HTML / XML', 'HTML (ERB / Rails)', 'Bash (shell)', 'SQL', 'PHP', 'Python', 'Pascal', 'Perl',
	'YAML', 'C#', 'Go', 'Apache (config)', 'Lua', 'IO', 'Lisp (common)', 'D', 'Erlang', 'Fortran', 'Haskell',
	'Literate Haskell', 'Makefile', 'Scala', 'Scheme', 'Smarty', 'INI', 'Nu', 'TeX', 'Closure', 'Puppet',
	'CoffeeScript',
]

__description__ = _("Paste the current content of your clipboard to pastie.org")
__version__ = "1"
__author__ = "Mickael GOETZ"

from kupfer.objects import Source, Leaf, Action
from urllib import urlencode
from urllib2 import urlopen, HTTPError
import gtk
import webbrowser


class PastieTextLeaf(Leaf):
	def __init__(self, text):
		if len(text) > 50:
			name = text[0:47] + '...'
		else:
			name = text
		Leaf.__init__(self, text, name)

	def get_icon_name(self):
		return "text-x-generic"


class ClipboardSource(Source):
	def __init__(self):
		Source.__init__(self, __kupfer_name__)

	def get_description(self):
		return __description__

	def is_dynamic(self):
		return True

	def get_items(self):
		yield PastieTextLeaf(gtk.Clipboard().wait_for_text())

	def provides(self):
		yield PastieTextLeaf

	def get_icon_name(self):
		return "edit-paste"


class PastieAction(Action):
	def __init__(self):
		Action.__init__(self, self.language)
		self.syntax = SYNTAXES.index(self.language) + 1

	def activate(self, obj):
		params = {
			'paste[parser_id]': self.syntax,
			'paste[body]': obj.object,
			'paste[authorization]': 'burger',
			'paste[restricted]': 1,
			'paste[access_key]': '',
			'utf8': '✓',
		}

		try:
			paste = urlopen('http://pastie.org/pastes', urlencode(params))
			webbrowser.open_new_tab(paste.geturl())
		except HTTPError:
			webbrowser.open_new_tab('http://pastie.org')

	def item_types(self):
		yield PastieTextLeaf

	def get_description(self):
		return _("Use ") + self.language + _(" syntax highlighting")

	def get_icon_name(self):
		#return "document-page-setup"
		#return "tools-check-spelling"
		return "accessories-text-editor"
		#return "applications-development"

#region Classes

class PastieObjectiveC_CPP(PastieAction):
	language = "Objective-C/C++"


class PastieActionScript(PastieAction):
	language = "ActionScript"


class PastieRuby(PastieAction):
	language = "Ruby"


class PastieRoR(PastieAction):
	language = "Ruby on Rails"


class PastieDiff(PastieAction):
	language = "Diff"


class PastiePlainText(PastieAction):
	language = "Plain text"


class PastieC_CPP(PastieAction):
	language = "C/C++"


class PastieCSS(PastieAction):
	language = "CSS"


class PastieJava(PastieAction):
	language = "Java"


class PastieJavascript(PastieAction):
	language = "Javascript"


class PastieHTML_XML(PastieAction):
	language = "HTML / XML"


class PastieHTML_ERB_Rails(PastieAction):
	language = "HTML (ERB / Rails)"


class PastieBashShell(PastieAction):
	language = "Bash (shell)"


class PastieSQL(PastieAction):
	language = "SQL"


class PastiePHP(PastieAction):
	language = "PHP"


class PastiePython(PastieAction):
	language = "Python"


class PastieErlang(PastieAction):
	language = "Erlang"


class PastiePascal(PastieAction):
	language = "Pascal"


class PastiePerl(PastieAction):
	language = "Perl"


class PastieYAML(PastieAction):
	language = "YAML"


class PastieCSharp(PastieAction):
	language = "C#"


class PastieGo(PastieAction):
	language = "Go"


class PastieApacheConfig(PastieAction):
	language = "Apache (config)"


class PastieLua(PastieAction):
	language = "Lua"


class PastieIO(PastieAction):
	language = "IO"


class PastieLispCommon(PastieAction):
	language = "Lisp (common)"


class PastieD(PastieAction):
	language = "D"


class PastieTeX(PastieAction):
	language = "TeX"


class PastieFortran(PastieAction):
	language = "Fortran"


class PastieHaskell(PastieAction):
	language = "Haskell"


class PastieLiterateHaskell(PastieAction):
	language = "Literate Haskell"


class PastieMakefile(PastieAction):
	language = "Makefile"


class PastieScala(PastieAction):
	language = "Scala"


class PastieScheme(PastieAction):
	language = "Scheme"


class PastieSmarty(PastieAction):
	language = "Smarty"


class PastieINI(PastieAction):
	language = "INI"


class PastieNu(PastieAction):
	language = "Nu"


class PastieClosure(PastieAction):
	language = "Closure"


class PastiePuppet(PastieAction):
	language = "Puppet"


class PastieCoffeeScript(PastieAction):
	language = "CoffeeScript"

#endregion