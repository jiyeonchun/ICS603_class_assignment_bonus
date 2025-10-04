from fasthtml.common import *

def user_row_entry(user_list):
    return (
        Table(
            Thead(Tr(Th("First Name"), Th("Last Name"), Th(""))),
            Tbody(
                *[Tr(
                    Td(u['firstname']),
                    Td(u['lastname']),
                    Td(A("X", href=f"/delete/{u['id']}"))
                ) for u in user_list]
            )
        ),
        A("< Back to Input", href="/")
    )
