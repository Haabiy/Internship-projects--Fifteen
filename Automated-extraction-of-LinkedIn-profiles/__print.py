from __home import filteredname, filteredposition, filteredlocation, filteredgetlinklist
import csv, codecs

# Finally print stored values
def _print():
    print("------------")
    # Saves the lists in a .CSV file to make it more readable for any user
    with codecs.open(r"LinkedIn.csv", 'w', encoding='utf-8') as f:
        for p in range(0, len(filteredname)):
            try:
                print(p + 1, filteredname[p], filteredposition[p], filteredlocation[p], filteredgetlinklist[p])
                wr = csv.writer(f)
                wr.writerow([filteredname[p], filteredposition[p], filteredlocation[p], filteredgetlinklist[p]])
            except Exception:
                pass
    print("------------")
