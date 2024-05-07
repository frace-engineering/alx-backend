import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
