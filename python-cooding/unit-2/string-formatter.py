# Username and Message Formatter

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message: ")

username = (first_name[0] + last_name).lower()
full_name = (first_name + " " + last_name).title()

clean_bio = bio.strip()
bio_length = len(clean_bio)
formatted_bio = clean_bio.replace("I am", "I'm")

print("\n--- User Profile ---")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {formatted_bio}")
print(f"Bio Character Count: {bio_length}")