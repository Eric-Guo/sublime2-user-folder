import sublime, sublime_plugin, os, subprocess

class OpenUrlInBrowserCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				if s.find('.') == -1 and s.find('://') == -1 :
					s = 'http://google.com/search?q='+s.replace(' ','+')
				command = "C:\\Program Files\\Mozilla Firefox\\firefox.exe " + s
				subprocess.Popen(command)