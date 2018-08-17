def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as lines:
        for line in lines:
            cast_list.append(line.split(",")[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)