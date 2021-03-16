import csv
with open('emotion.csv') as csvfile:
    reader = csv.reader(csvfile)
    with open('employee_file2.csv', mode='w') as csv_file:
        fieldnames = ['sentiment', 'content']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            url = row[1]
            if len(url.split('@')) == 2:
                x = url.replace("@", "###").split('###')[1].split(' ')[0]
                y = url.replace("@"+x, "")
                print(row[0],y)
                writer.writerow({'sentiment': row[0], 'content': y })
            if len(url.split('@')) == 1:
                print(row[0],url)
                writer.writerow({'sentiment': row[0], 'content': url })
