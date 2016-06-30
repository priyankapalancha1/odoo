from openerp.osv import fields, osv
from openerp import api

class School(osv.osv):

	_name = "school.school"
	_columns = {
	'studentid' : fields.integer('Studentid', size=10, required=True),
	'firstname' : fields.char('Firstname', size=30, required=True),
	'passpercentage' : fields.float('passpercentage', size=30, required=True),
	'result' : fields.char('result', size=30, required=True),
	'medium' : fields.char('Medium', size=30, required=True),
	'landmark' : fields.boolean('landmark', size=30, required=True),
	'timeofbirth' : fields.datetime('timeofbirth', size=10, required=True),
	'state' : fields.selection([('telangana','telangana'),('andhra','andhra'),('sec','sec')],'state', size=30, required=True),
	'admissiondate' : fields.date('Admissiondate', size=10, required=True),
	'address' : fields.text('Address', size=30, required=True),
	}
	
	
	@api.onchange('state')
	def onchage_state(self):
		print "state oncon change"
		if self.state == "telangana":
			self.address = "hyderabad"
		if self.state == "andhra":
			self.address = "kadapa"
		else:
			pass

	
	@api.onchange('passpercentage')
	def onchage_passpercentage(self):
		print "passpercentage oncon change"
		if self.passpercentage == 40:
			self.result = "pass"
		if self.passpercentage == 30:
			self.result = "fail"
		else:
			pass
	





