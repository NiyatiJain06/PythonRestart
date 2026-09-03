def find_paper(papers, names):
    for paper in papers:
        if paper == names:
            return True
    return False

papers = ["Anita", "Bharat", "Karan", "Niya", "Isha"]

searsh_name = "Karan"

result = find_paper(papers, searsh_name)

if result:
    print("Paper found!")
else:
    print("Paper not found!")    