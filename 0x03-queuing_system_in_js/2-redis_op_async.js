import redis from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
