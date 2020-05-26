import pymel.core as pm

pm.undoInfo(openChunk=True)
try:
    def deleteEmptyNulls():             
        grpsToDelete=[]
        allSiblings=[]        
        emptyGrps=[i for i in pm.ls(transforms=True,leaf=True,exactType="transform") if i.getChildren != []\
        and i.listConnections() == []]
    
        def getFirstEmptyGrp(transNode):
            parentGrp=transNode.getParent()
            siblingsGrp=transNode.getSiblings()
            
            if siblingsGrp != []:
                matches=[x for x in siblingsGrp if x in allSiblings]    
                if len(matches)== len(siblingsGrp):
                    for sibling in matches:
                        grpsToDelete.remove(sibling)
                    getFirstEmptyGrp(parentGrp)
                    
                else: 
                    grpsToDelete.append(transNode)                           
                    allSiblings.append(transNode)            
            else:
                getFirstEmptyGrp(parentGrp)
                                  
        for i in emptyGrps:
            getFirstEmptyGrp(i)
            
        print "deleted nodes: {}".format(grpsToDelete)
        pm.delete(grpsToDelete)
finally:
    cmds.undoInfo(closeChunk=True) 
              
deleteEmptyNulls()
        
    