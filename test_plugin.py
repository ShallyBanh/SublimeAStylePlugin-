import sublime, sublime_plugin  

class StyleCode( ):
    def __init__( self ):
        self.brackets = 0
        self.new_file = ""
        self.line = ""

    def ParseLine( self, line ):
        self.line = line

    def StyleSpaces( self ):
        #Spaces for brackets ( )
        begin = self.line.find( '(' )
        if( begin != -1 and self.line[begin +1: begin +2 ] != ' ' ):
            self.line = self.line[:begin+1] + " " + self.line[begin+1:]

        end = self.line.find( ')')
        if( end != -1 and self.line[end -1 : end ] != ' ' ):
            self.line = self.line[:end] + " " + self.line[end:]

        #Spaces for equal signs
        equal = self.line.find( '=' )
        while( True ):
            if( self.line[equal +1 : equal +2] != ' ' and self.line[equal +1 : equal +2] != '=' ):
                self.line = self.line[:equal+1] + " " + self.line[equal+1:]
            equal = self.line.find( '=', equal + 1 );
            if(equal == -1):
                break
            
        lequal = self.line.find( '=' )
        if( lequal != -1 and self.line[lequal - 1: lequal]!= ' ' ):
            self.line = self.line[:lequal] + " " + self.line[lequal:]

    def StyleBrackets( self ):
        offset = 0
        ifbrackets = self.line.find( '{' )
        endbracket = self.line.find( '}' )

        if ifbrackets != -1:
            self.brackets += 1
            offset -= 1

        if endbracket != -1:
            self.brackets -= 1

        if self.brackets != 0:
            spaces = self.brackets + offset
            new_line = "\t" * spaces
            new_line += self.line.lstrip( )
            self.new_file += new_line
            return

        self.new_file += self.line

    def MakeItBetter( self, filename ):
        with open( filename, "r" ) as fp:
            for line in fp:
                self.ParseLine( line )
                self.StyleSpaces( )
                self.StyleBrackets( )             

        file = open( filename, "w" )
        file.seek( 0 )
        file.write( self.new_file )

class EventDump( sublime_plugin.EventListener ):  

    def on_post_save( self, view ): 
        style = StyleCode( )
        style.MakeItBetter( view.file_name( ))
        
