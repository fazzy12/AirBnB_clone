
<div style="display: flex; justify-content: space-between;">
    <img src="image1.jpg" alt="Image 1" width="400" height="300" />
    <img src="image2.jpg" alt="Image 2" width="400" height="300" />
</div>

# AirBnB Clone

## Welcome to the AirBnB Clone project! 

This meticulously crafted Python application replicates the core functionalities of the renowned AirBnB platform. Dive into this README to explore the architecture, usage, and advanced features of this project.

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Implemented Classes](#implemented-classes)
- [Console Commands](#console-commands)
- [Advanced Features](#advanced-features)
- [Contributing](#contributing)
- [License](#license)

### Installation

Let's embark on this journey by setting up the project on your local machine. Follow these steps:

1. **Clone the Repository**: Begin by cloning this repository to your local environment using Git:
```
git clone https://github.com/your-username/AirBnB_clone.git
```
2. **Navigate to Project Directory**: Access the project directory:
```
cd AirBnB_clone
```
3. **Run the Console Application**: Execute the console application to interact with the system:
```
./console.py
```
### Usage
Our AirBnB Clone boasts a command-line interface (CLI) designed for effortless management of objects and data. The CLI enables you to interact with the application through various commands. Here's a quick overview of essential commands to kickstart your exploration:

* `create <class_name>`: Create a new instance of the specified class.
* `show <class_name> <id>`: Display details of a specific instance.
* `all <class_name>`: List all instances of a particular class.
* `update <class_name> <id> <attribute_name> "<new_value>"`: Update an attribute of an instance.
* `destroy <class_name> <id>`: Delete an instance.

For an in-depth look, please refer to the [Advanced Features](#advanced-features) section.

### Project Structure
To comprehend the inner workings of our `AirBnB Clone`, let's explore its structure:

* `models/`: Houses Python class definitions for various objects.
* `models/engine/`: Contains the FileStorage class responsible for data storage.
* `tests/`: Home to unit tests ensuring the project's integrity.
* `console.py`: The primary command-line interface for the application.

## Implemented Classes
Our `AirBnB Clone` project presents a range of classes that inherit from the `BaseModel` class. These classes include:

* `User`: Represents a user entity, featuring attributes like email, password, first name, and last name.
* `State`: Models a state entity, encapsulating a name attribute.
* `City`: Represents a city entity, complete with name and state_id attributes referencing the State class.
* `Amenity`: Encapsulates an amenity entity, characterized by a name attribute.
* `Place`: Represents a place entity, incorporating attributes such as city_id, user_id, name, description, and more.
* `Review`: Models a review entity with place_id, user_id, and text attributes.

### Console Commands
Unlock the full potential of our application with an array of console commands. Here are examples to guide you:

* `create User`: Generate a new User instance.
* `show User <user_id>`: Reveal details of a specific `User`.
* `all User`: List all User instances.
* `update User <user_id> email "new_email@example.com"`: Update a `User` instance's email.
* `destroy User <user_id>`: Eradicate a `User` instance.

For a comprehensive list of commands and detailed instructions, please visit the  [Usage](#usage) section.

### Advanced Features
Our `AirBnB Clone project` encompasses advanced features that enhance the user experience. These functionalities include:

* Retrieving all instances of a class using `<class_name>.all()`.
* Counting instances of a class using `<class_name>.count()`.
* Showing an instance by ID using `<class_name>.show(<id>)`.
* Destroying an instance by ID using `<class_name>.destroy(<id>)`.
* Updating an instance using `<class_name>.update(<id>`, `<attribute_name>`, `<attribute_value>)`.
* Updating an instance using a dictionary representation with `<class_name>.update(<id>`, `<dictionary>)`.

These advanced features empower you to manage objects with unparalleled flexibility and efficiency.

### Contributing
We embrace contributions from the community! If you're eager to contribute, please follow these well-defined steps:

* `Fork the Repository`: Begin by forking the repository to your GitHub account.
* `Create a New Branch`: Establish a new `branch` for your feature or bug fix: `git checkout -b feature/new-feature`.
* `Make Your Changes`: Implement your changes and `commit` them: `git commit -m "Add new feature`".
* `Push Your Branch`: Push your branch to your GitHub repository: `git push origin feature/new-feature.`
* `Submit a Pull Request`: Finally, submit a `pull request` detailing your changes.

Please ensure that your code adheres to the project's coding style and conventions.

License
This project operates under the MIT License. Consult the LICENSE file for comprehensive license details.
