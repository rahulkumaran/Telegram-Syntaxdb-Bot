from options import *
import os

if __name__=='__main__':
	TOKEN = '<ADD_ACCESS_TOKEN_HERE>'
	PORT = int(os.environ.get('PORT', '8443'))

	updater = Updater(TOKEN)



	#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

	#logger = logging.getLogger(__name__)

	updater = Updater(token=TOKEN)
	
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start',start))

	dispatcher.add_handler(CommandHandler('help',help))

	dispatcher.add_handler(CommandHandler('search', search, pass_args = True))

	updater.start_polling()
