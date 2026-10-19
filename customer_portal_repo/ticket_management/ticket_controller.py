from .ticket_service import TicketService

class TicketController:
    def __init__(self):
        self.service=TicketService()

    def create_ticket(self,email,description):
        return self.service.create_ticket(email,description)
