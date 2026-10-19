# Phone Directory Search Tool

contacts = {
    "Amara": "0821112222",
    "Sipho": "0833334444",
    "Lerato": "0845556666"
}

# List + Dictionary combined
names = list(contacts.keys())

search_name = input("Enter the friend's name to look up: ").strip()

if search_name in names:
    number = contacts[search_name]
    print(f"Found! {search_name}'s number is {number}")
else:
    print("Contact not found.")