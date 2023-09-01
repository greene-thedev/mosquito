import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    client.subscribe("greenethedev")
    
def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io")

client.loop_forever()