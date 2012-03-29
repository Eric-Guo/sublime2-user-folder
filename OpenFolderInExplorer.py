import sublime, sublime_plugin, os, subprocess

class OpenFolderInExplorerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            folder_name, file_name = os.path.split(self.view.file_name())
        command = "explorer " + folder_name
        subprocess.Popen(command)