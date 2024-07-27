import frappe

def full_name(doc, event):

    doc.full_name = f"{doc.first_name}  {doc.last_name}"