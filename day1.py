snacks = open('dataset.txt',"r")
def compute_elf_calory(snacks):
    calories=[]
    current_elf=[]
    for snack in snacks:
        snack=snack.strip()
        if snack =="":
            calories.append(current_elf)
            current_elf=[]
        else:
            current_elf.append(int(snack))
        calories.append(current_elf)
        most_calories=0
        for elf in calories:
            total_calories=sum(elf)
            if total_calories>most_calories:
                most_calories=total_calories

    print(most_calories)

compute_elf_calory(snacks)
