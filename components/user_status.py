from fasthtml.common import *

def user_status(user_list):
    return Div(
        H2("Activity & Status"),
        Div(f"Currently DB contains {len(user_list)} entries"),
        Div(
            A("View All Entries", href="/list")
        )
    )
