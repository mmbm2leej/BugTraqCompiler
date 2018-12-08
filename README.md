# BugTraqCompiler
For scraping data from the BugTraq mailing list

WHAT THIS DOES/CAN DO:
    Scrapes data from the securityfocus archives- bugtraq mailing list.
        The info it selects and retrieves:
              - CVE IDs
              - Post Author
              - Post Date
              - Post Title
              - Message Body
              
    Retrieves the description of each CVE that it finds from the mitre website.
    
    Saves a text file in the given path directory for each message.
        The text is shown after rearranging the information.
        CVE IDs fetched and crossed with mitre-given descriptions are shown.
       
HOW THIS CAN BE IMPROVED:
    The program uses one function to do everything, is very slow(relatively).
    It can be much faster, if:
        Class of spiders are created and are made to run the function for each link in Archive Links.
        These spider objects work in parallel but update the queue as they work, so there are no conflictions/collisions/overlaps.
        
    Presentation:
        The program just uses the terminal and text documents to display the info.
        Readability can be further improved with some implemented GUI system compatible(or designed) for using it.
    
    Further Parsing and Human Language Metadata Manipulation:
        As of this writing, the program is at its foundation. Key terms are parsed and represented to the user, however parsing key terms
        of interest in the body and meta-analysis display for large groups of messages between given timeframes could be incredibly useful
        cybersecurity specialists.
