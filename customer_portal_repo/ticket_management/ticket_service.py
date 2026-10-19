from .ticket_repository import TicketRepository

class TicketService:
    def __init__(self):
        self.repo=TicketRepository()

    def create_ticket(self,email,description):
        priority="HIGH" if "login" in description.lower() else "MEDIUM"

        ticket={
            "customer":email,
            "description":description,
            "priority":priority,
            "status":"OPEN"
        }

        return self.repo.save(ticket)
