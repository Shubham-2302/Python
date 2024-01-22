import logging

# # my_log = logging.getLogger( "Baap ")

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename = "log.txt",format='%(asctime)s - %(process)d-%(levelname)s %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
logging.info("Are bhai")
logging.critical("muh me lele")

# import logging

# logging.basicConfig(format='%(asctime)s - %(message)s')
# logging.info('Admin logged in')
