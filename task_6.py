types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def remove_duplicates(ticket_list):
    unique_tickets = []
    for ticket in ticket_list:
        if ticket not in unique_tickets:
            unique_tickets.append(ticket)
    return unique_tickets


def make_final_dict(bug_types, bug_tickets):
    final_dict = {}
    all_tickets = []

    for priority in range(1, 6):
        tickets_list = bug_tickets[priority]
        tickets_list = remove_duplicates(tickets_list)

        unique_list = []
        for ticket in tickets_list:
            if ticket not in all_tickets:
                unique_list.append(ticket)
                all_tickets.append(ticket)
        final_dict[bug_types[priority]] = unique_list
    return final_dict

