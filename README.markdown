My sublime text 2 user folder context, you can following below step to setting up.

Installation Guide in Windows 7
-------------------------------
* Install Sublime Text as normal way in Windows 7
* Add Sublime Text Path to Path in
* Startup the Sublime Text in first time and pin it in Windows 7 Taskbar
* Open cmd and locate your Sublime User profile folder, %USERPROFILE%\AppData\Roaming\Sublime Text 2\Packages\User
* git clone https://github.com/Eric-Guo/sublime-user-folder.git .
* Open the Sublime Text again and install Sublime Package Control by running below code in console line (Ctrl+`)
> import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'
* Close and Reopen the Sublime Text Editor, Ctrl+Shift+P and type 'Upgrade/Overwrite All Packages'
* Waiting enough time to let Package Control download all the relative package.
* Remove line '{ "keys": ["ctrl+b"], "command": "build" },' in Default (Windows).sublime-keymap file (bug for Build 2210?)