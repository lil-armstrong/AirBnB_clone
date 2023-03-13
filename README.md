# 0x00. AirBnB clone - The console

## Table of content

- [0x01 Introduction](#0x01-Introduction)
- [0x02 Environment](#0x02-Environment)
- [0x03 Installation](#0x03-Installation)
- [0x04 Testing](#0x04-Testing)
- [0x05 Usage](#0x05-Usage)
- [0x06 Resources](#0x06-Resources)

## 0x01 Introduction
Team project to build a clone of [AirBnB](https://www.airbnb.com/).
The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw).

### Commandline interpreter

The commandline interpreter is a tool buil for developers to manage the project objects. It is expected to be enable its users do the following:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object
For a funcdamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

### Storage
Storage of objects are handled by the `Storage` engine in the `FileStorage` Class.

## 0x02 Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

## 0x03 Installation
```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```
The commandline can be executed two modes: interactive and non-interactive mode
```bash
# Interactive mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
To execute the commandline program in non-interactive mode, do that following
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 0x04 Testing

All the test are defined in the `tests` folder. You can run all test using the following command

```bash
python3 -m unittest discover tests
```
You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`

## 0x05 Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Commands

**All commands use the following format: `COMMAND / usage / example with output`**
* Create
--

Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

```bash
create <class>
```
Example:
```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

* Show
--
Show stored class information
```bash
show <class> <id>
```
Example:
```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

* Destroy
--
Deletes an instance of a given class with a given ID.
```bash
destroy <class> <id>
```
> This action updates the file.json
Example:
```bash
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

* all
--
Print all string representation of all instances of a given class.
```bash
all [<class>]
```
> If no class is passed, all classes are printed.
Example:
```bash
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```

* count
--
Prints the number of instances of a given class.
```bash
count <class>
```
Example:
```bash
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```

* Update
--
Updates an instance based on the class name, id, and kwargs passed.
> Update the file.json
```bash

```
Example:
```bash

```

## 0x06 Resources

-   Use [`hack/generate-authors.sh`](https://github.com/moby/moby/blob/master/hack/generate-authors.sh) to generate authors
-   [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
-   [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
-   [Python packages concept page](https://intranet.alxswe.com/concepts/66)
-   [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
-   [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
-   [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
-   [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
-   [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
-   [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
-   [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
