class pokeTypeFormatter:
    '''
    Constructs a string with type strengths and weaknesses
    '''
    def __init__(self, type):
        self.finalDict = {}
        self.finalString = ''
        self.type = str(type)
        self.relevantKeys = ['ineffective', 'super_effective', 'resistance', 'weakness', 'no_effect']
        
        typeResult = self.queryType()
        typeList = typeResult['hits']['hits']
        for singleType in typeList:
            singleType = singleType['_source']
            for key in self.relevantKeys:
                tempList = []
                for x in singleType[str(key)]:
                    tempList.append(x['name'])
                self.finalDict[str(key)] = tempList
                
        self.formatter()
           
    def queryType(self):
        '''
        Query type in elasticsearch
        '''
        return es.search(index="type",body={"query":{"match":{"name":self.type}}})
    
    def formatter(self):
        '''
        Makes the information look pretty for printing purposes
        '''
        self.finalString = ''
        for mult in self.relevantKeys:
            multTitle = '\n' + mult.title().replace('_' , ' ') + ':\n'
            self.finalString += multTitle
            if len(self.finalDict[mult]) == 0:
                self.finalString += '\tNone\n'
            else:
                for type in self.finalDict[mult]:
                    self.finalString += self.typeToString(type)
                    
        
    def typeToString(self, type):
        '''
        Takes type and converts it's contents in the finalDict to a pretty string
        '''
        stringToReturn = ''
        stringToReturn += '\t' + type.capitalize() + '\n'
        return stringToReturn
        
    def __str__(self):
        return self.finalString