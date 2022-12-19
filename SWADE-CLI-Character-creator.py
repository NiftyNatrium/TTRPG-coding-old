#Haven't added races or anything btw

#global predefined variables needed later
attributePoints=5 #points to spend on attributes
skillPoints=12 #how many points to spend on skills
hindrancePoints=0 #determines how much extra points for other catergories, dependant on how many hindrances chosen, max of 4.
edgePoints=1 #normally 0 but assumed to be a human will change later maybe

attributes= { #these are the attributes which allow derived traits, determine skills, and enable certain edges to be taken
  "Agility" : 4
  "Smarts" : 4
  "Spirit" : 4
  "Strength" : 4
  "Vigor" : 4
}

skills= { #these are the skills
  "Athletics" : 4
  "Boating" : 2
  "Common Knowledge" : 4
  "Driving" : 2
  "Performance" : 2
  "Persuasion" : 4
  #need to add the rest when I have the book  
}

#naming character
print("Welcome to your Character Creation!")
name=input("Please name your character:") #sets the name, eventually should write this to a file
decision=input("Where would you like to start? Attributes, Skills, Hindrances, Edges, or Inventory?")

#here we want a switch function to determine the choice made at the start 
match decision:
  case "Attributes": #attribute raises here
    while attributePoints>0: #loops until attributes are spent
      print("Choose to increase: Agility, Smarts. Spirit, Strength, or Vigor.")
      if attributes[userInput] + 2 > 12: #max quantity for attribute
        print("Pick a different attribute!")
      else: # the normal case
        attributes[userInput] += 2 #increases the desired stat
        attributePoints -= 1 #decreases the while loop variable
    print("Your attributes are:\n\
          \tAgility: d",attribute[Agility],"\n\
          \tSmarts: d",attribute[Smarts],"\n\
          \tSpirit: d",attribute[Spirit],"\n\
          \tStrength: d",attribute[Strength],"\n\
          \tVigor: d",attribute[Vigor],sep="") #prints the attributes, sep fixes the spacing.
        
  



