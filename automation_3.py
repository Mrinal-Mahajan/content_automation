import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # We don't want first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append("{}{}".format(line['FirstName'],line['LastName']))
	print names

html_output += '<p>There are currently {} public contributors. Thank You!</p>'.format(len(names))

html_output += '\n<ul>'

for name in names:
    html_output += '\n\t<li>{}</li>'.format(name)

html_output += '\n</ul>'

print(html_output)