# AirBnB clone
## Installation

Simply git clone this repository.
## Opening The Console

The console can be opened at the project-level directory with the following command:

```sh
./console.py
```

A new console with the prefix `(hbnb) ` will open.

## Using The Console

The console has the following existing classes:

- Amenity
- BaseModel
- City
- Place
- Review
- State
- User

`<class>` used below, is meant to be substituted for the class names above.
The console can perform the following commands:

- `create <class>`
    - Creates a new instance in the `file.json` file. Its ID will be printed.
- `show <class> <id>`
    - Shows all data of this instance as found in `file.json`.
- `destroy <class> <id>`
    - Deletes all data pertaining to this instance from `file.json`.
- `all`
    - Shows all data for all instances in `file.json`.
- `all <class>`
    - Shows all data for all instances of `<class>` in `file.json`.
-  `update <class> <id> <attribute> <value>`
    - Updates the instance with the specified attribute and value. The attribute and the value are not restricted in terms of what they can be.

Use `help <command>` for additional information on the commands above.
