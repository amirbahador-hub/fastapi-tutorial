from jinja2 import Environment, FileSystemLoader


def main():
    animals = [
        {
            "name": "emma",
            "gender": "female",
            "type": "dog"
        },
        {
            "name": "nemo",
            "gender": "male",
            "type": "fish"
        },
    ]
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('hello_world.txt')
    output = template.render(animals=animals)
    print(output)


if __name__ == "__main__":
    main()
