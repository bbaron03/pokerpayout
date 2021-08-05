class lastGame:
  def __init__(self):
    self.userIn = ""
    self.creditors = []
    self.debtors = []
    self.owes = {}

  def enterCreditors(self):#Enter the winners
    killPhrase = "no more"
    name = ""
    print("Enter your creditors here, type \"no more\" in the name slot to stop")
    while(name.lower()!= killPhrase):
      name = input("Name of creditor: ")
      if name.lower() == killPhrase:#Double the redundancy to ensure killphrase entry
        break
      amount = float(input("Amount Due:"))
      self.creditors.append({"Name" : name, "due": amount})
      print("Added to the list\n")
  
  def enterDebtors(self): #Enter the losers
    killPhrase = "no more"
    name = ""
    print("\nNow, enter your debtors here, type \"no more\" in the name slot to stop")
    while(name.lower() != killPhrase):
      name = input("Name of debtor: ")
      if name.lower() == killPhrase:#Double the redundancy to ensure killphrase entry
        break
      amount = float(input("Amount Owed:"))
      self.debtors.append({"Name" : name, "owed" : amount})
      print("Added to the list\n")
    for debtor in self.debtors:
      #Prepares self.owes with debtor names as keys to empty arrays
      self.owes[debtor["Name"]] = []


  '''Loops through every creditor for each debtor. If the debtor - creditor is less than zero, then the debtor is released and the creditors amount due changes to the leftover. If debtor - creditor is greater than zero, keep the debtor, creditor is now due 0. If the debtor - creditor is equal to zero, creditor is due 0 and the debtor is released. Self.owes uses the debtors names as the keys and the value is an array that stores tuples of the creditor's name and how much the debtor owes them.'''


  def calculate(self):
    for i in range(0, len(self.debtors)):
      for j in range(0, len(self.creditors)):
        self.debtors[i]["owed"] -= self.creditors[j]["due"]
        if self.debtors[i]["owed"] < 0:
          self.owes[self.debtors[i]["Name"]].append((self.creditors[j]["Name"], self.creditors[j]["due"] + self.debtors[i]["owed"]))
          self.creditors[j]["due"] = -self.debtors[i]["owed"]
          break
        elif self.debtors[i]["owed"] > 0:
            self.owes[self.debtors[i]["Name"]].append((self.creditors[j]["Name"], self.creditors[j]["due"]))
            self.creditors[j]["due"] = 0
        else:
          self.owes[self.debtors[i]["Name"]].append((self.creditors[j]["Name"], self.creditors[j]["due"]))
          self.creditors[j]["due"] = 0
          break

  def printFinal(self):#Prints the owed money neatly
    for debtor in self.owes:
      sum = 0
      print(debtor + " owes: ")
      for creditorTuple in self.owes[debtor]:
        #Only prints amount if the amount owed from the debtor is not 0
        if(creditorTuple[1] != 0):
          sum += creditorTuple[1]
          print("\t" + creditorTuple[0] + " $" + str(creditorTuple[1]))
      print("TOTAL = " + str(sum))
      print("\n")
    
  def complete(self):
    self.enterCreditors()
    self.enterDebtors()
    self.calculate()
    self.printFinal() 