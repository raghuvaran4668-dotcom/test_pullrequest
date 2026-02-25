def room_members(members: list) -> list:
    
      members.pop() # remove the second member from the list
      return members # return the list of members
      
list_of_members = ["raghuvendra", "sai", "kumar", "rohith"]

room_members(list_of_members)
print(list_of_members[1]) # should return "sai"
