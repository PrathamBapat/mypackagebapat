class ListNode:
   def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:

   def __init__(self):
       self.head = None

   def getSize(self):
        curr = self.head
        s = 1
        while curr.next is not None:
          curr = curr.next
          s = s + 1
        print(str(s))
        

   def addNode(self,data):
        newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else: 
           curr = self.head
           while curr.next is not None:
             curr = curr.next
           curr.next = newNode
      
   def delete(self,value):
      curr = self.head
      prev = self.head
      while curr is not None:
       if curr.data is value:
         if curr.data == prev.data:
          curr = curr.next
          prev.next = None
          self.head = curr
         else:
          curr = curr.next
          prev.next = curr
       else:
         prev = curr
         curr = curr.next
          

   def printNode(self):
       curr = self.head
       while curr is not None:
           print(str(curr.data))
           curr = curr.next

myList = LinkedList()
value = 1
value_2 = 1;
while value>0:
 print("Press the number regarding what you want to do!\n 1 for adding the element\n 2 for printing the list\n 3 for getting the link size \n 4 for deleting the following node")
 value_1 = input()
 def switch(arg) :
  switcher = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4, 
      
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
  myList.getSize()

 elif(number == 4):
  print("Enter the number you want to delete")
  value = input()
  myList.delete(value)

 



