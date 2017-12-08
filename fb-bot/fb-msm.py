from fbchat import log, Client
import random
import sys
def meme(word):
  new_word = ""
  prob = 0.4
  for i in word:
    if random.random() < 0.4:
      new_word+=i.upper()
    else:
      new_word+=i.lower()
  return new_word
# Subclass fbchat.Client and override required methods
# prev_two = ["",""]
all_chats = {}
pos = 0
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        if(message_object.text == "meme"):
            msg = meme(all_chats["thread_id"])
            nm = message_object
            nm.text = msg

            self.send(nm, thread_id=thread_id, thread_type=thread_type)

        all_chats["thread_id"] = message_object.text
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo


client = EchoBot("MSMgeneratorbot@gmail.com", "msmbot123")
client.listen()
