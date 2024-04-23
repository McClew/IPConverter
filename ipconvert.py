import os
import re
import time

# Styling classes & prebuilt variables
reset = "\033[0m"
bold = "\033[01m"
underline = "\033[04m" 
cyan = "\033[36m"
block = cyan + " █ " + reset
block_colour = cyan + " █ "

# Primary/root function
def main():
	os.system("clear")
	banner()
	selection = menu()
	menu_selection(selection)

# Displays script banner
def banner():

	banner = cyan + """

	 █████ ███████████                                                                           
	░░███ ░░███░░░░░███                                                                          
	 ░███  ░███    ░███                                                                          
	 ░███  ░██████████                                                                           
	 ░███  ░███░░░░░░                                                                            
	 ░███  ░███                                                                                  
	 █████ █████                                                                                 
	░░░░░ ░░░░░                                                                                                                                                
	                                                                                             
	   █████████     ███████    ██████   █████ █████   █████ ██████████ ███████████   ███████████
	  ███░░░░░███  ███░░░░░███ ░░██████ ░░███ ░░███   ░░███ ░░███░░░░░█░░███░░░░░███ ░█░░░███░░░█
	 ███     ░░░  ███     ░░███ ░███░███ ░███  ░███    ░███  ░███  █ ░  ░███    ░███ ░   ░███  ░ 
	░███         ░███      ░███ ░███░░███░███  ░███    ░███  ░██████    ░██████████      ░███    
	░███         ░███      ░███ ░███ ░░██████  ░░███   ███   ░███░░█    ░███░░░░░███     ░███    
	░░███     ███░░███     ███  ░███  ░░█████   ░░░█████░    ░███ ░   █ ░███    ░███     ░███    
	 ░░█████████  ░░░███████░   █████  ░░█████    ░░███      ██████████ █████   █████    █████   
	  ░░░░░░░░░     ░░░░░░░    ░░░░░    ░░░░░      ░░░      ░░░░░░░░░░ ░░░░░   ░░░░░    ░░░░░    
	                                                                                             
	""" + reset

	print(banner)

# User interface
def menu():
	print(block + "Please choose one of the below options using it's ID.")
	print(block + "[0] Convert decimal to binary.")
	print(block + "[1] Convert binary to decimal.")
	print(block + "[2] Print conversion table.")
	print(block + "[3] Exit.")
	print(block)

	user_input = input(block)

	# Validate the users input
	if user_input.isnumeric():
		return user_input
	else:
		# User feedback for invalid input
		print(block + "Please select a valid ID.")
		print(block + "Terminal reset in 3 seconds...")

		# Sleep so user can read feedback and then reset terminal
		time.sleep(3)
		os.system("clear")
		main()

# Go to function depending on user selection
def menu_selection(option_selected):
	if option_selected == "0":
		decimal_convert()
	elif option_selected == "1":
		binary_convert()
	elif option_selected == "2":
		display_table()
	elif option_selected == "3":
		print(block + "Exiting script...")
		time.sleep(2)
		quit()
	else:
		print(block + "Error finding selection.")
		print(block + "Terminal reset in 3 seconds...")

		# Sleep so user can read feedback and then reset terminal
		time.sleep(3)
		os.system("clear")
		main()

# Convert dotted decimal IP to binary
def decimal_convert():
	ip = input(block + "Please enter the IP address in a dotted decimal format: " + cyan + bold)
	regex = re.match(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)

	if not regex:
		print(block + "Please enter a valid IPv4.")
		print(block + "Terminal reset in 3 seconds...")
		time.sleep(3)
		os.system("clear")
		main()

	octets = ip.split(".")
	columns = [128,64,32,16,8,4,2,1]
	converted_ip = []

	for octet in octets:
		print(block + "Octet: " + octet)
		results = []
		holder = int(octet)

		for column in columns:
			if holder >= column:
				holder = holder - column
				results.append("1")
			else:
				results.append("0")

		table = (
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " | 128 | 64  | 32  |  16 |  8  |  4  |  2  |  1  |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " |  " + results[0] + "  |  " + results[1] + "  |  " + results[2] + "  |  " + results[3] + "  |  " + results[4] + "  |  " + results[5] + "  |  " + results[6] + "  |  " + results[7] + "  |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n")
		
		result = "".join(results)
		converted_ip.append(result)

		print(table)
		print(block + "Result: " + result)

	formatted_ip = ".".join(converted_ip)
	print(block)
	print(block + "Converted IP: " + formatted_ip)
	print(block)
	print(block + "Press enter to return to menu...")
	input(block)
	main()

# Convert binary IP to dotted decimal
def binary_convert():
	#01111111.00000000.00000000.00000001
	ip = input(block + "Please enter the IP address in a dotted decimal format: " + cyan + bold)
	regex = re.match(r"^([0|1]{8}.[0|1]{8}.[0|1]{8}.[0|1]{8})$", ip)

	if not regex:
		print(block + "Please enter a valid IPv4 in binary format.")
		print(block + "Terminal reset in 3 seconds...")
		time.sleep(3)
		os.system("clear")
		main()

	octets = ip.split(".")
	columns = [128,64,32,16,8,4,2,1]
	results = []

	for octet_index,octet in enumerate(octets):
		print(block + "Octet: " + octet)
		holder = 0

		for binary_index,binary in enumerate(octet):
			if int(binary) == 1:
				holder = holder + columns[binary_index]

		table = (
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " | 128 | 64  | 32  |  16 |  8  |  4  |  2  |  1  |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n" +
		block_colour + bold + " |  " + octet[0] + "  |  " + octet[1] + "  |  " + octet[2] + "  |  " + octet[3] + "  |  " + octet[4] + "  |  " + octet[5] + "  |  " + octet[6] + "  |  " + octet[7] + "  |\n" +
		block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+\n")

		holder = str(holder)

		print(table)
		print(block + "Result: " + holder)
		print(block)

		results.append(holder)

	formatted_ip = ".".join(results)
	print(block)
	print(block + "Converted IP: " + formatted_ip)
	print(block)
	print(block + "Press enter to return to menu...")
	input(block)
	main()

# Display conversion table
def display_table():
	table = (
	block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+-------+\n" +
	block_colour + bold + " | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 | Total |\n" +
	block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+-------+\n" +
	block_colour + bold + " | 128 | 64  | 32  |  16 |  8  |  4  |  2  |  1  |  255  |\n" +
	block_colour + bold + " +-----+-----+-----+-----+-----+-----+-----+-----+-------+\n")

	print(table)
	print(block + "Press enter to return to menu...")
	input(block)
	main()

main()