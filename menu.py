import

tb = nuke.toolbar("Nodes")
m = tb.addmemu("Lazypic")
m.addMenu("Draw")
m.addMenu("Draw/rimecode_burnin","nuke.createNode(''timecode_burnin')")

