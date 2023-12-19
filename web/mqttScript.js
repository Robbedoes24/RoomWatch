const mqtt = require('mqtt');
const WebSocket = require('ws');
const dotenv = require('dotenv');
dotenv.config();

// MQTT configuration
const mqttBrokerUrl = process.env.MQTTBROKER;
const mqttBrokerPort = process.env.MQTTBROKERPORT;
const mqttTopic = process.env.MQTTTOPIC;

// WebSocket server configuration
const wss = new WebSocket.Server({ port: process.env.WEBSOCKETPORT });

// MQTT client
const mqttClient = mqtt.connect(`mqtt://${mqttBrokerUrl}:${mqttBrokerPort}`);

mqttClient.on('connect', () => {
  console.log('Connected to MQTT broker and subscribed to', mqttTopic);
  mqttClient.subscribe(mqttTopic);
});

// WebSocket connection handler
wss.on('connection', (ws) => {
  console.log('WebSocket connected');

  // MQTT message handler
  mqttClient.on('message', (topic, message) => {
    message = JSON.parse(message);
    msg = { topic: topic.split('/')[1], people: message.people };
    console.log(msg);
    ws.send(JSON.stringify(msg));
  });

  // Handle WebSocket disconnection
  ws.on('close', () => {
    console.log('WebSocket disconnected');
    mqttClient.end();
  });
});

// Handle MQTT connection errors
mqttClient.on('error', (error) => {
  console.error('MQTT connection error:', error);
});

// Handle SIGINT (Ctrl+C) to gracefully disconnect from the MQTT broker
process.on('SIGINT', () => {
  mqttClient.end(() => {
    mqttClient.unsubscribe(mqttTopic);
    console.log('Disconnected from MQTT broker due to SIGINT');
    process.exit();
  });
});
