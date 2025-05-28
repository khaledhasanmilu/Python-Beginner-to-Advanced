# Writing contacts to a file
def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")
    print("Contacts saved successfully!")

# Reading contacts from a file
def read_contacts(filename):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(':')
                contacts[name] = number
        print("Contacts loaded successfully!")
    except FileNotFoundError:
        print("File not found. No contacts to load.")
    return contacts

# Example usage
filename = "contacts.txt"

# Create and write some contacts
my_contacts = {
    "Alice": "01700000000",
    "Bob": "01811111111",
    "Charlie": "01922222222"
}
write_contacts(filename, my_contacts)

# Read and display contacts
loaded_contacts = read_contacts(filename)
print("Your Contacts:")
for name, number in loaded_contacts.items():
    print(f"{name}: {number}")
