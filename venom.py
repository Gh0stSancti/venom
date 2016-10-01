import os
import sys
import time

def main():
	print("")
	print("venom - ARP Cache Poisoner")
	print("")
	print("Created by: Gh0st")
	print("Type help for assistance")
	aa = input("venom> ")
	if "help" in aa:
		print("")
		print("arpcp - Cache Poison")
		print("poison - Poisons chosen internet address")
		time.sleep(2)
		main()
	elif "arpcp" in aa:
		print("")
		print("Generating list...")
		time.sleep(5)
		print("")
		os.system("arp -a")
		main()
	elif "poison" in aa:
		print("")
		bb = input("venom/poison/internet-address> ")
		print("")
		print("Poisoning " + bb + "...")
		time.sleep(4)
		print(bb + " has been poisoned.")
		print("Press enter to continue")
		os.system("pause >nul")
		os.system("cls")
		main()
	else:
		print("")
		print("Not a command")
		print("Press enter to continue")
		os.system("pause >nul")
		main()
		
main()