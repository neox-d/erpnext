# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Employee1(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aadhaar_card_no: DF.Data | None
		date_of_birth: DF.Date | None
		first_name: DF.Data | None
		full_name: DF.Data | None
		last_name: DF.Data | None
		pan_card_no: DF.Data | None
	# end: auto-generated types
	pass
