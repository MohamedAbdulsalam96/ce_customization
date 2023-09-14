# Copyright (c) 2023, ce construction and contributors
# For license information, please see license.txt

import frappe

def get_context(context):
    context.name = "Prasant"
    return context

def execute(filters=None):
	#if not filters: filters = {}

	# message = [
    # "'<b>Filter</b>' is <span style='color:Red;'>not working</span>",
   
#]

	return get_columns(), get_data(filters), #message
   

# 	query = """
#     SELECT
# 	    so.name AS my_id,
#         so.user_name,
#         so.subject,
#         so.department,
#         si.item_code
#     FROM
#         `tabIssue` AS so
#     LEFT JOIN
#         `tabSupport Item` AS si
#     ON
#         so.name = si.parent
	
# """

	#data = get_all_data_from_list("Issue")
	# data2 = get_child_table_data("Support Item")
	#data = frappe.db.sql(query, as_dict=True)
	
	#return columns, data
	# if not cs_data:
	# 	msgprint(_('no record found'))
	# 	return columns, cs_data
	# #return columns, data
	# data = []

def get_data(filters):
    print(f"\n\n{filters}\n\n")
   # _from, to = filters.get('from'), filters.get('to')

    #conditions = " WHERE creation BETWEEN '" + filters_from+ "' AND '" + filters.to+ "'"
    from_date = filters.get('_from')
    to_date = filters.get('to') 
    
    sql_query = """
    SELECT so.name, DATE(so.resolution_date),  CONCAT(si.item_name_ ,CASE WHEN si.type = 'old' THEN CONCAT(' (', si.type, ')') ELSE '' END) as item_name_,si.quantity,CONCAT(so.site ,CASE WHEN so.department IS NOT NULL THEN CONCAT(' - ', so.department) ELSE '' END) as site,so.user_name, so.closed_by,so.subject
    FROM `tabIssue` AS so 
    JOIN `tabSupport Item` AS si ON so.name = si.parent
    WHERE {from_filter}
    {to_filter}
    """
    from_filter = ""
    to_filter = ""

    if from_date:
        from_filter = f" (DATE(so.resolution_date) >= '{from_date}')"

    if to_date:
        to_filter = f" AND (DATE(so.resolution_date) <= '{to_date}')"

    # Insert the 'from_filter' and 'to_filter' into the SQL query
    sql_query = sql_query.format(from_filter=from_filter, to_filter=to_filter)

    

    for fieldname, value in filters.items():
        if fieldname == '_from':
            pass
        elif fieldname == 'to':
            pass
        else:
            sql_query += f" AND {fieldname} = '{value}'"

#    # if filters.get('subject'): conditions += f" AND subject='{filters.get('subject')}' "
       

#     #print(f"\n\n{conditions}\n\n")
    all_data = frappe.db.sql(sql_query)

    return all_data 

def get_columns():
	return[
        {
            'fieldname': 'name',
            'label': ('ID'),
            'fieldtype': 'Link',
            'options': 'Issue',
			'width':'130'
            
        },
        {
			'fieldname': 'resolution_date',
            'label': ('Date'),
            'fieldtype': 'Date',
            'width':'110'
        },
        {
			'fieldname': 'item_name_',
            'label': ('Particulars'),
            'fieldtype': 'Data',
            'align':'left',
			'width':'120'
        },
        {
			'fieldname': 'quantity',
            'label': ('Quantity'),
            'fieldtype': 'Float',
            #'align':'left',
			'width':'90'
        },
        {
			'fieldname': 'site',
            'label': ('Site/Department'),
            'fieldtype': 'Link',
        	'options': 'Branch',
            'align':'left',
			'width':'130'
        },
		{
            'fieldname': 'user_name',
            'label': ('User name'),
            'fieldtype': 'Data',
			'width':'120',
            'color': 'blue !important;',
            'align':'left',
            #'options': 'Account'
        },
        # {
		# 	'fieldname': 'department',
        #     'label': ('Department'),
        #     'fieldtype': 'Link',
        # 	'options': 'Department',
        #     'align':'left',
		# 	'width':'120'
        # },
        {
			'fieldname': 'closed_by',
            'label': ('Entered By'),
            'fieldtype': 'Data',
			'width':'120',
            'align':'left'
            #'options': 'Account'
        },
      
        {
			'fieldname': 'subject',
            'label': ('Remarks'),
            'fieldtype': 'Data',
			'width':'120',
            'align':'left'
            #'options': 'Account'
        },
		# {
		# 	'fieldname': 'starting_date',
        #     'label': ('Starting Date'),
        #     'fieldtype': 'Datetime',
		# 	'width':'120'
        #     #'options': 'Account'
        # },
		# {
		# 	'fieldname': 'resolution_date',
        #     'label': ('Resolution Date'),
        #     'fieldtype': 'Datetime',
		# 	'width':'120'
        #     #'options': 'Account'
        # },
        # {
		# 	'fieldname': 'item_code',
        #     'label': ('Item Code'),
        #     'fieldtype': 'Link',
        #     'options': 'Item',
        #     'align':'left',
		# 	'width':'90'
        # },
      
        # {
		# 	'fieldname': 'type',
        #     'label': ('Status'),
        #     'fieldtype': 'Select',
        #     'align':'left',
		# 	'width':'120'
        # },
       
        # {
		# 	'fieldname': 'rate',
        #     'label': ('Rate'),
        #     'fieldtype': 'Currency',
        #     #'align':'left',
		# 	'width':'90'
        # },
        # {
		# 	'fieldname': 'amount',
        #     'label': ('Amount'),
        #     'fieldtype': 'Currency',
        #     #'align':'left',
		# 	'width':'90'
        # }
     
	]

# def get_cs_data(filters):

# 	data = frappe.get_all(
# 		doctype = 'Issue',
# 		fields = ['user_name', 'department','subject'],
# 		order_by = 'user_name desc'
# 	)
# 	return data


# def get_all_data_from_list(doctype):
#    data_all = frappe.get_all(doctype, fields=["subject", "department","item.item_code","item.item_name_"])
#    return data_all


# def get_child_table_data(parent_name):
#     # Fetch the child table records related to the parent record
#     child_records = frappe.get_all(parent_name, fields=["item_code"])
#     return child_records
