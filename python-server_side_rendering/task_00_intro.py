import os

def generate_invitations(template, attendees):
    # Validar tipo de template
    if not isinstance(template, str):
        print("Error: template should be a string.")
        return

    # Validar tipo de attendees
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return

    # Validar contenido del template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Validar si la lista está vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Procesar cada asistente
    for index, attendee in enumerate(attendees, start=1):
        # Reemplazar cada placeholder
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace("{" + key + "}", str(value))

        # Escribir a archivo
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as f:
            f.write(filled_template)
