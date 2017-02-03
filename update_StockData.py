#This program will update CSV files in StockData Folder
import webbrowser
import os.path 
def update_data():
	"""
	this should do all the steps by calling this function
	"""
    pass
def add_data():
    pass
def get_current_filenames():
	"""
	get file names so we can find what symbols we need
	"""
    pass
def download_data(symbols,data_type=['p']):
	"""
    download data from yahoo finance
	"""
    url = "http://finance.yahoo.com/d/quotes.csv?s={" + symbols+ "}&f={" + data_type + "}"
    webbrowser.open(url,new=2)
def get_new_filenames():
    pass
def rm_current_files():
    pass
def add_new_files():
	pass
