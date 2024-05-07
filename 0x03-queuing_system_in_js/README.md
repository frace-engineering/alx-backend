Readme file for the 0x03-queuing_system_in_js project

Resources
Read or watch:

Redis quick start
Redis client interface
Redis client for Node JS
Kue deprecated but still use in the industry

Requirements
All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
All of your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the js extension


Required Files for the Project
package.json
.babelrc
Don't forget to run $ npm install when you have the package.json

 Install a redis instance
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/downloads/):

$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make

Start Redis in the background with src/redis-server
$ src/redis-server &
Make sure that the server is working with a ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
Kill the server with the process id of the redis-server (hint: use ps and grep)
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.
