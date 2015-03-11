import sublime, sublime_plugin

#
# run: view.run_command("example")
#
class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
