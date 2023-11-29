# JavaScript - Web scraping
Scripting
API
JavaScript

## Resources

* [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
* [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
* [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)

## Learning Objectives

* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use <code>request</code> and fetch API
* How to read and write a file using <code>fs</code> module
### Tasks

| Task | File |
| ---- | ---- |
| 0. Readme | [0-readme.js](./0-readme.js) |
| 1. Write me | [1-writeme.js](./1-writeme.js) |
| 2. Status code | [2-statuscode.js](./2-statuscode.js) |
| 3. Star wars movie title | [3-starwars_title.js](./3-starwars_title.js) |
| 4. Star wars Wedge Antilles | [4-starwars_count.js](./4-starwars_count.js) |
| 5. Loripsum | [5-request_store.js](./5-request_store.js) |
| 6. How many completed? | [6-completed_tasks.js](./6-completed_tasks.js) |
| 7. Who was playing in this movie? | [100-starwars_characters.js](./100-starwars_characters.js) |
| 8. Right order | [101-starwars_characters.js](./101-starwars_characters.js) |

### Tasks/file Usage

0. Readme
a script that reads and prints the content of a file.

The first argument is the file path
The content of the file is read in utf-8
If an error occurred during the reading, print the error object
Ex:
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 

1. Write me
A script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file is written in utf-8
If an error occurred during while writing, print the error object

guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 

2. Status code
A script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code is printed like this: code: <status code>
Use the module request

guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$

3. Star wars movie title
A script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
Use the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA) with the endpoint https://swapi-api.alx-tools.com/api/films/:id
Use the module request

guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 

4. Star wars Wedge Antilles
A script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA): https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - the script uses this ID for filtering the result of the API
Use the module request

guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$ 

5. Loripsum
A script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
Use the module request

guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>...

6. How many completed?
A script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
Use the module request

guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$

7. Who was playing in this movie?
A script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
Use the Star wars API
Use the module request

guillaume@ubuntu:~/0x14$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
guillaume@ubuntu:~/0x14$ 

8. Right order
A script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line in the same order of the list “characters” in the /films/ response
Use the Star wars API
Use the module request

guillaume@ubuntu:~/0x14$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
guillaume@ubuntu:~/0x14$ 
