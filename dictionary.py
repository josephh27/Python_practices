monthConversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": ("October", "october"),
    "Nov": "November",
    "Dec": "December"
}
    
print(monthConversions.get("Oc", "Invalid Key"))

i = 240
while i >= 20:
    print(i)
    i /= 3
    
print("Done with loop")


running = True
while running:
    try:
        input("Input: ")
        break

