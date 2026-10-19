from user_management.user_controller import UserController
from ticket_management.ticket_controller import TicketController

if __name__ == "__main__":
    user_ctrl = UserController()
    ticket_ctrl = TicketController()

    user = user_ctrl.register_user({"name":"John","email":"john@company.com"})
    ticket = ticket_ctrl.create_ticket(user["user"]["email"], "Login issue")

    print(ticket)
