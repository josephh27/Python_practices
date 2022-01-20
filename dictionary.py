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
    
print(monthConversions.get("Oct"))
citext = " "
list(monthConversions.keys())[list(monthConversions
                .values()).index(citext)]





