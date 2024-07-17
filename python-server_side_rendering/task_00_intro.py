import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if template == "":
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", attendee.get("name", "N/A"))
        output = output.replace("{event_title}", attendee.get("event_title", "N/A"))
        output = output.replace("{event_date}", attendee.get("event_date", "N/A") if attendee.get("event_date") else "N/A")
        output = output.replace("{event_location}", attendee.get("event_location", "N/A"))

        output_filename = f"output_{idx}.txt"

        with open(output_filename, 'w') as file:
            file.write(output)
        
        print(f"Generated file: {output_filename}")

if __name__ == "__main__":
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
