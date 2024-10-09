from rich.console import Console
import json
import os

console = Console()

def show_initial_data():
    console.print("Here is some initial data:", style="bold cyan")
    # Example data to show
    console.print("[bold yellow]User Data Collection Example:[/bold yellow]")
    console.print("Name: Cindy Liang, Age: 22, Email: Cindyl3@illinois.edu, Hobby: Reading")

def collect_user_data():
    user_data = []
    while True:
        console.print("\n[bold cyan]Please enter your details:[/bold cyan]")

        name = console.input("Enter your name: ")
        age = console.input("Enter your age: ")
        email = console.input("Enter your email: ")
        hobby = console.input("Enter your favorite hobby: ")

        console.print("\n[bold yellow]You entered the following data:[/bold yellow]")
        console.print(f"Name: {name}\nAge: {age}\nEmail: {email}\nHobby: {hobby}")

        confirm = console.input("[bold green]Is this data correct? (yes/no): ").strip().lower()
        if confirm == 'yes':
            user_data.append({
                "name": name,
                "age": age,
                "email": email,
                "hobby": hobby
            })

            another_entry = console.input("[bold green]Do you want to enter another person's data? (yes/no): ").strip().lower()
            if another_entry != 'yes':
                break
        else:
            console.print("[bold red]Please re-enter the data.[/bold red]")

    return user_data

def save_data_to_file(data):
    file_path = os.path.join(os.path.dirname(__file__), "user_data.json")  # Save in the same directory
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    return os.path.abspath(file_path)

def main():
    show_initial_data()
    user_data = collect_user_data()

    if user_data:
        file_path = save_data_to_file(user_data)
        console.print(f"\n[bold green]Data has been saved to: {file_path}[/bold green]")

if __name__ == "__main__":
    main()
