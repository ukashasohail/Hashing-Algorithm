###########################
####  CODE BY UKASHA   ####
###########################

#input of data to store in hash table
emp_num=int(input("Enter Employee Number: "))
emp_name=input("Enter Employee Name: ")
emp_llnum=int(input("Enter Landline Number (WITHOUT HYPHEN)"))
emp_mblnum=int(input("Enter Mobile Number (WITHOUT HYPHEN)"))

#input to search data
search=int(input("Enter emp num to seaerch"))

#initializing list to store data
list_details=[emp_num,emp_name,emp_llnum,emp_mblnum]

#Initializing Directory to store keys and data.
#Python Dictionary is used as a Hash table which works on key, value pairs.
#This Hash table(Dicitonary) contains 75 memory addresses
Directory={0: None, 1: None, 2: [30224,'hamza bhatti',4654654,649684,1], 3: None, 4: None, 5: None, 6: None, 7: None, 8: [12345,'sheikh anas',16546,541646,1], 9: [42786,'zeeshan khan',446464,4646488,2], 10: [21032,'amir ali',45465456,56465465,3], 11: None, 12: None, 13: [35783,'abdurrehman',4648648,464646,1], 14: [77394,'javaid khan',4646848,4648648,1], 15: [18409,'saleemullah',1614564,464646,3], 16: [94478,'talal alam bhatti',1646846,64646,1], 17: [34180,'asad alam',34341354,646465,2], 18: [38051,'ayan khan',164646,4864894,1], 19: [33520,'ajmal khan',464564,46554564,7], 20: [86744,'dabir ali',1646546,6464684,1], 21: [78642,'aleem khan',54646,646848,1], 22: [92584,'abdul ahad',516354,465454,3], 23: None, 24: None, 25: None, 26: None, 27: [22365,'shahid ali',164564,4646545,1], 28: None, 29: [45508,'saad khan',4648648,1648648,1], 30: [32150,'younis khan',13145615,1651561,1], 31: None, 32: None, 33: None, 34: None, 35: None, 36: None, 37: [78950,'abdul hadi',2161515,4546465,1], 38: None, 39: None, 40: [96692,'huzaifa ali',16131654,464646,1], 41: [36541,'umer gul',1651651,4654564,1], 42: [36250,'yasir shah',165314561,156465456,1], 43: [81000,'azam dawood',464654,4646846,1], 44: None, 45: None, 46: None, 47: None, 48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: [22100,'hasan ali',163615615,646554654,1], 55: None, 56: [32760,'sabir aleem',16344564,464646,1], 57: [12540,'saeed ajmal',165464,6456456,1], 58: None, 59: None, 60: [68826,'zaid ahmed',464646,4646848,1], 61: None, 62: None, 63: None, 64: None, 65: None, 66: [80585,'ali salam',46654654,464684,1], 67: None, 68: None, 69: [88253,'shehroz khan',464564,46464646,1], 70: [21678,'osama izhar',646848646,4646311,1], 71: [22480,'athar ali',4646545,464654,3], 72: None, 73: None, 74: None}

#function to calculate the hash key of 5-digit employee number to input
def hash_function():
	return (emp_num%73)

#function to calculate the hash key of 5-digit employee number to search
def hash_function_search():
	return (search%73)

#assigning the hash value generated by function to variable hash_address
hash_address=hash_function()

#assigning the hash value generated by function to variable search_key
search_key=hash_function_search()

#Data Entry in Directory and Collision resolution
for i in Directory.keys(): #this loop run on list of dictionary keys
	if i==hash_address: #when key matches with the correct hash address
		no_of_probes=1

		while hash_address<=(max(Directory.keys())): #this loop will run more than 1 time to resolve collision resolution
			if Directory[hash_address]== None: #check if the value of address is empty
				Directory[hash_address]=list_details #enter the list of details if the location is empty
				list_details.append(no_of_probes) #also stores the number of probes in that list
				break
			else:
				hash_address=hash_address+1 #increament in case of collision
				no_of_probes=no_of_probes+1 #increament in case of collision
		break

#Searching Data using number of probes
def search_function():
	for j in Directory.keys(): #loop on keys in dictionary
		c=search_key
		if j==search_key:
			while c<=(max(Directory.keys())):
				if Directory[c][0]==search: #check if the search data(emp num) matches with value stored in address
					print(Directory[c]) #prints that value
					print("The Number of Successful Probes is:", Directory[c][4])
					break
				else:
					c=c+1 #increament otherwise
		else:
			print("Unsuccessful Search") #otherwise it will print unsuccessful search


search_function()
# print(Directory)
