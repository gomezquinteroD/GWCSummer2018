import school_scores

list_of_scores = school_scores.get_all()

for item in list_of_scores[0]:
    print("----KEY ", item, " ----")
    print(list_of_scores[0][item])
    print('\n')

for item in list_of_scores:
    print("State: ", item["State"]["Name"])
    print("Year: ", item["Year"])
