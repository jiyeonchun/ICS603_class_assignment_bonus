from fasthtml.common import *
from components.user_row_entry import user_row_entry

def list_user_page(user_list):
    return user_row_entry(user_list)
