#print a message to the terminal window
print("Rules that govern the state of water")

# set up a variable to hold the temp we input
current_temp = False

while current_temp is False:
	current_temp = input("Enter a temperature\n")
	# see what current temp is
	print("you input:", current_temp)

	# if the current temp is at freezing or below then water is solid
	if (int(current_temp) < 0 or (int(current_temp) == 0)):
		print("water is a solid! because it is at or below freezing")
		current_temp= False
		# else check another condition, if its not freezing, is it boilin?
	elif (int(current_temp) < 100):
		print("water is a liquid because it is above freezing but below boiling")
		current_temp= False

	elif (int(current_temp) > 100 or (int(current_temp) ==100)):
		print("water is a gas because it is hot")
		current_temp= False