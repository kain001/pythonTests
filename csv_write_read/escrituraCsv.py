import csv

with open('gamers.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'league']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Kain', 'league': 'Gold'})
    writer.writerow({'player_name': 'Nelson', 'league': 'Diamond'})
    writer.writerow({'player_name': 'Guti', 'league': 'Platinum'})
