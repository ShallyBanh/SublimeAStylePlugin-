import sublime, sublime_plugin  
  
class TestPlugin(sublime_plugin.EventListener):  

    def on_post_save(self, view):  
        bracketCount = 0 
        new_file = ""
        with open(view.file_name(), "r") as fp:
            for line in fp:
            	offset = 0
            	beginBracket = line.find('{')
            	endBracket = line.find('}')

                #found a bracket up the count
            	if beginBracket != -1:
            		bracketCount += 1
                    #the offset ensures the bracket doesn't get indented at the next indentation level 
            		offset -= 1
                #found a closing bracket decrease the count
            	elif endBracket != -1:
                    bracketCount -= 1
                #we are in a bracket so add the proper indention to beginning of each line 
            	if bracketCount != 0:
                	numOfTabs = bracketCount + offset
                	new_line = "\t" * numOfTabs
                	new_line += line.lstrip()
                	new_file += new_line
                	continue
            	new_file += line.lstrip()       

        #Modify the file with the desired indentation 
        file = open(view.file_name(), "w")
        file.seek(0)
        file.write(new_file)
        
