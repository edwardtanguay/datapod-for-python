print("Making backup...")

number_of_files = 6
time_expected = 10.5
time_taken = 12

# get value from the first line of "backup_data.txt"
name_of_backup = open("backup_data.txt", "r").readline().strip()

if number_of_files == 6:
	print(f"Backing up {name_of_backup}...")
	print(f"Backing up {number_of_files} files...")
	for i in range(number_of_files):
		print(f"Backing up file {i+1}...")
	print(f"Overtime: {time_taken - time_expected}")
else:
	print("There must be 6 files to backup")