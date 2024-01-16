# # importing module
# import logging
#
# # Create and configure logger
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# # Creating an object
# logger = logging.getLogger()
#
# # Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
#
# # Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
#
#
#
#
#
# # import logging
# # logging.warning('Watch out!')  # will print a message to the console
# # logging.info('I told you so')  # will not print anything



import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')