class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True
         
   def printNode(self):
       curr = self.head
       for x in range(0,self.size):
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
value = 1
value_2 = 1;
while value>0:
 print("Press the number regarding what you want to do!\n 1 for adding the element\n 2 for printing the list\n 3 for getting the link size")
 value_1 = input()
 def switch(arg) :
  switcher = {
    1 : 1,
    2 : 2,
    3 : 3,
      
  }

  return switcher.get(arg,"invalid argument")
 number = switch(value_1)
 if(number == 1):
  print("Enter the total number of numbers you want to add")
  total_number = input()
  for x in range(0,total_number):
    string = str(x+1) 
    print "Enter the {} number".format(string)
    number = input()
    myList.addNode(number) 
    value+=1

 elif(number == 2):
  myList.printNode()

 elif(number == 3):
  print(myList.getSize())

 



