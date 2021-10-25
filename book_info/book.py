# def get_book_info(isbn):
#     # get book info
saved_dict = {}
MAX_N = 10

def store_mem(isbn, saved_dict, N, get_book_info):
    if(len(saved_dict) < N):
        saved_dict[isbn] = get_book_info(isbn)

get_book_info = store_mem(isbn, saved_dict, MAX_N, get_book_info)

get_book_info()