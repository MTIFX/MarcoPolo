# cloud -> distributed 

'''
The cloud is the end of the pipe. 
node -> feed -> cloud -> candlebuilder -> database -> api 
'''

import feed
feed = feed.feed()

import node
node = node.node() # for checking status of node, whether up or down, true or false 



class cloud():
        
    
    def State(self):
        # determine which nodes are up, and which ones are down
        # each instance writes to a shared state parameter 
        pass
    
    
    
    def Write(self):
        pass
    
    
    
    def Read(self):
        pass
    
    
    
    def CheckConsistency(self):
        # percent deviation 
        pass
    
    
    

    
    
    
    
    
