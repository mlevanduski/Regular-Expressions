import re

class ChatSession:

    def __init__(self,filename):
        #Initialize empty lists and variables
        self.filename = filename
        self.numlines = 0
        self.TagsList = []
        self.MembersList = []
        self.TimesList = []
        self.UniqueMembersList = [] #second step of filtering MembersList
        self.UniqueTagsList = [] #second step of filtering TagsList
        self.MessageList = []
        self.UserSysList = []
        #Open File
        with open(filename, 'r') as f:
            records = f.readlines()
            for record in records: 
                self.numlines += 1 #numlines counter
                record = record.strip('\n')
                
                Tag = re.findall('^T.+?\s',record) #Tag extraction for tag list
                Tag = [x.rstrip(' ') for x in Tag]
                self.TagsList.append(Tag)
                if Tag not in self.UniqueTagsList: #Unique Tags
                    self.UniqueTagsList.append(Tag)

                Member = re.split('\s',record, 3) #Member extraction for MembersList 
                Member = Member[2]
                self.MembersList.append(Member)
                if Member not in self.UniqueMembersList: #Unique Members
                    self.UniqueMembersList.append(Member)
        
                Message = re.split('[:*]',record, 1) #Message extraction
                Message = [x.lstrip(' ') for x in Message]
                Message = Message[1]
                Message = Message.lower()
                Message = re.sub('[.,*"-;:<>^]',"", Message)
                self.MessageList.append(Message)
            
                Timestamp = re.split('\s',record, 2) #Timeslist extraction
                Timestamp = Timestamp[1]
                self.TimesList.append(Timestamp)

                UserSysSymbol = re.findall('[*:]|$',record)[0]
                self.UserSysList.append(UserSysSymbol)

    def GetNumLines(self):
        return("The Number of lines in the file are:",self.numlines)

    def GetTagsList(self):
        return("The Tags with redundancies are:",self.TagsList)

    def GetUniqueTagsList(self):
        return("The Unique Tags are:",self.UniqueTagsList)

    def GetTimesList(self):
        return("The Times List is:",self.TimesList)

    def GetMembersList(self):
        return("The members list with redundancies is:",self.MembersList)

    def GetUniqueMembersList(self):
        return("The unique members are:",self.UniqueMembersList)

    def GetMessageList(self):
        return("The messages are:",self.MessageList)

    def GetUserSysList(self):
        return("The user system symbol list is:",self.UserSysList)

