def load_knowledge():

    with open("data/hr_policy.txt","r") as f:
        return f.read()


knowledge_base = load_knowledge()


def chatbot_response(query):

    query = query.lower()

    if "leave" in query:
        return "Employees are entitled to 20 casual leaves per year."

    if "vpn" in query:
        return "To reset VPN password contact IT support or use internal portal."

    if "event" in query:
        return "Next company event: Annual Tech Meet – September 15."

    return "Sorry, I could not find relevant information."