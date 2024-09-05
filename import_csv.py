import datetime

# Open the text file
with open('file.txt', 'r') as file:
    # Skip the first 4 lines
    for _ in range(4):
        next(file)
    
    # Initialize an empty list to store the extracted data
    data = []
    
    # Read each line from line 5 onwards
    for line in file:
        # Split the line by comma
        columns = line.strip().split(',')
        
        # Extract the required columns
        index = columns[0]
        surname = columns[1]
        name = columns[2]
        special_number = columns[3]
        
        # Extract the birthdate from the special number
        year_born = int(special_number[:4])
        month_born = int(special_number[4:6])
        day_born = int(special_number[6:8])
        
        # Calculate the age based on today's date
        today = datetime.date.today()
        birthdate = datetime.date(year_born, month_born, day_born)
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        # Add the extracted data to the list
        data.append([name, surname, age])

# Print the list
for item in data:
    print(f'{item[0]}, {item[1]}, {item[2]}')