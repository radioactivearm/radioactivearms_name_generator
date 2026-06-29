import pandas as pd
import typer

num_random_names = 10

surname_file_path = "cleaned_data/surnames.csv"
boy_forenames_file_path = "cleaned_data/forenames_boy.csv"
girl_forenames_file_path = "cleaned_data/forenames_girl.csv"

app = typer.Typer()

@app.command()
def boy():
    surnames =  pd.read_csv(surname_file_path)
    forenames = pd.read_csv(boy_forenames_file_path)

    Rsurnames = surnames.sample(n=num_random_names)
    Rforenames = forenames.sample(n=num_random_names)

    surname_array = Rsurnames["Surname"].to_numpy()
    forename_array = Rforenames["Name"].to_numpy()

    print("Random Boy Names")
    print("----------------")

    add_str = ""

    for i in range(0, num_random_names -1):
        name = f"{forename_array[i]} {surname_array[i]}"
        add_str += name + "\n"
        print(name)
    print("")

    add_str += "-----------------\n"

    with open('Names.txt', 'a') as file:
        file.write(add_str)

@app.command()
def girl():
    surnames =  pd.read_csv(surname_file_path)
    forenames = pd.read_csv(girl_forenames_file_path)

    Rsurnames = surnames.sample(n=num_random_names)
    Rforenames = forenames.sample(n=num_random_names)

    surname_array = Rsurnames["Surname"].to_numpy()
    forename_array = Rforenames["Name"].to_numpy()

    print("Random Girl Names")
    print("-----------------")

    add_str = ""

    for i in range(0, num_random_names -1):
        name = f"{forename_array[i]} {surname_array[i]}"
        add_str += name + "\n"
        print(name)
    print("")

    add_str += "-----------------\n"

    with open('Names.txt', 'a') as file:
        file.write(add_str)


if __name__ == "__main__":
    app()