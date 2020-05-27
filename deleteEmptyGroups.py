import pymel.core as pm

pm.undoInfo(openChunk=True)
try:
    def deleteEmptyNulls():             
        grpsToDelete=[]
        allSiblings=[]        
        emptyGrps=[]
        for i in pm.ls(transforms=True,leaf=True,exactType="transform"):
            boundig=i.getBoundingBoxInvisible() 
            area=6*(boundig[3]-boundig[0]**2)

            if i.getChildren != [] and i.listConnections() == []:
                emptyGrps.append(i)

            elif area == 0:
                emptyGrps.append(i)
                    
        def getFirstEmptyGrp(transNode):
            parentGrp=transNode.getParent()
            siblingsGrp=transNode.getSiblings()
            
            if parentGrp != None:
                if siblingsGrp != []:
                    matches=[x for x in siblingsGrp if x in allSiblings]    
                    if len(matches)== len(siblingsGrp):
                        getFirstEmptyGrp(parentGrp)
                        for sibling in matches:
                            grpsToDelete.remove(sibling)                       
                    else: 
                        grpsToDelete.append(transNode)                           
                        allSiblings.append(transNode)            
                else:
                    getFirstEmptyGrp(parentGrp)
            else:
                grpsToDelete.append(transNode)
                                
        for i in emptyGrps:
            getFirstEmptyGrp(i)
            
        print "deleted nodes: {}".format(grpsToDelete)
        pm.delete(grpsToDelete)
finally:
    cmds.undoInfo(closeChunk=True) 
              
deleteEmptyNulls()
