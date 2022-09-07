from jinja2 import Environment, FileSystemLoader


def main():
    data = [
        {
            "fname": "ali",
            "lname": "qasemi"
        },
        {
            "fname": "hasan",
            "lname": "safari"
        }
    ]

    fileLoader = FileSystemLoader("templates")
    env = Environment(loader=fileLoader)
    userTemplate = env.get_template("users.html")
    output = userTemplate.render(users=data)
    print(output)


if __name__ == "__main__":
    main()
