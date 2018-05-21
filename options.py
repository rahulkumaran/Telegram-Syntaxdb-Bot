from telegram.ext import CommandHandler, Updater
from telegram import *
import syntaxdb


def start(bot, update):
	bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
	
	bot.sendMessage(chat_id = update.message.chat_id, text = '''
		Hey %s %s! Welcome to SyntaxDB Bot! Type /help for more information regarding the functionalities of this particular bot.
	''' %(update.message.from_user.first_name,update.message.from_user.last_name))

def search(bot, update, args):
	topic = ""
	i = 0
	count = 0
	if(len(args) == 0):
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text = '''
			Please make sure that you enter a valid search query for me to help you.
		''')
	for arg in args:
		if(i < (len(args) - 1)):
			topic += arg + " "
		else:
			topic += arg
		i += 1
	print("\""+ topic + "\"")
	syntax = syntaxdb.Syntaxdb(choice = 0, search_query = topic, language = "")
	content = syntax.getContent()
	
	for i in range(0,len(content)):
		print("here")
		count += 1
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text = content[i])

	if(count==0):
		bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
		bot.sendMessage(chat_id = update.message.chat_id, text =  '''
		There are no related searches to the topic you entered! Make sure your search query was right and try again! Check for spelling mistakes and follow the format in /help
		''')



def help(bot, update):
	bot.sendChatAction(chat_id = update.message.chat_id, action = ChatAction.TYPING)
	bot.sendMessage(chat_id = update.message.chat_id, text = '''
		To use this bot, look at the format below!
		/search <concept_name> <language>
		Example : Suppose you want to use how to use the concept for in java,
		/search for in java
	''')



