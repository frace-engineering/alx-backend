import { createClient } from "redis";


const redisClient = createClient();

redisClient.on("error", (error) => {
  console.error(`Redis client not connected to the server: ${error}`)
});

redisClient.on('connect', () => {
  console.log("Redis client connected to the server");
});
