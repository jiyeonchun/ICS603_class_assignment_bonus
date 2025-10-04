from fasthtml.common import *
from components.user_entry_form import user_entry_form
from components.user_status import user_status

def add_user_page(user_list):
    return (
        user_entry_form(),
        user_status(user_list)
    )

