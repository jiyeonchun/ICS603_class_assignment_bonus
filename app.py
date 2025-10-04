from fasthtml.common import *
from pages.add_user_page import add_user_page
from pages.list_user_page import list_user_page

app, rt = fast_app()

user_list = [
    {'id': 1, 'firstname': 'Jiyeon', 'lastname': 'Chun'},
    {'id': 2, 'firstname': 'Kylie', 'lastname': 'Higashionna'},
    {'id': 3, 'firstname': 'Ivan', 'lastname': 'Wu'}
]

@rt("/")
def home():
    return Titled(
        "",
        add_user_page(user_list)
    )

@rt("/add", methods=['POST'])
def add_user(firstname: str, lastname: str):
    new_id = max([u['id'] for u in user_list], default=0) + 1
    user_list.append({'id': new_id, 'firstname': firstname, 'lastname': lastname})
    return RedirectResponse(url="/", status_code=303)


@rt("/list")
def list():
    return Titled(
        "User Records",
        list_user_page(user_list)
    )

@rt("/delete/{user_id}", methods=['GET'])
def delete(user_id: int):
    global user_list
    user_list = [u for u in user_list if u['id'] != user_id]
    return RedirectResponse("/list")
    

if __name__ == "__main__":
    serve()