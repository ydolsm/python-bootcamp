"""with open("exercise.txt", "w") as file:
    name = ["Mia Anderson",
            "\nEthan Roberts",
            "\nLiam Johnson",
            "\nSophia Martinez",
            "\nOlivia Davis",
            "\nNoah Thompson"
    ]
    file.writelines(name)"""

with open("exercise.txt", "r") as file:
    file_contents = file.read().splitlines()
    print(file_contents)
