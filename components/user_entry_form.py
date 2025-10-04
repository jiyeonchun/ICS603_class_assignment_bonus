from fasthtml.common import *

def user_entry_form():
    return Div(
        H2("User Entry"),
        Form(
            Input(type="text", name="firstname", placeholder="First Name", required=True),
            Input(type="text", name="lastname", placeholder="Last Name", required=True),
            Button("Submit >", type="submit"),
            method="post", action="/add"
        )
    )
