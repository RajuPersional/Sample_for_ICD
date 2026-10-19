class TicketRepository:
    tickets=[]

    def save(self,ticket):
        ticket["id"]=len(self.tickets)+1
        self.tickets.append(ticket)
        return ticket
