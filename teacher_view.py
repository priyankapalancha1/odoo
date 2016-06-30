from openerp.osv import fields, osv
from openerp import api

class Teacher(osv.osv):

	_name = "teacher"
	_description="teacher details"
	_columns = {
	'name' : fields.char('name', size=20, required=True),
	'age' : fields.char('age', size=20, required=True),
	'address' : fields.char('address', size=20, required=True),
	'phone' : fields.char('phone', size=20, required=True),
	'free' : fields.boolean("free"),
	'fee' : fields.float("fee"),

	'teacher_id' : fields.many2one('school.school', 'teacher_id'),

	'teach_id' : fields.many2many('student','teacher_id','branch',string='student details'),
	}

	
	@api.onchange('free')
	def onchage_free(self):
		print "free oncon change"
		if self.free == True:
			self.fee = 0
		if self.free == False:
			self.fee = 10000

	@api.onchange('name')
	def onchage_name(self):
		print "name oncon change"
		if self.name == True:
			self.age = 0
		if self.name == False:
			self.age = 21



	def create(self, cursor, user, vals, context=None):
		print "valsssss",vals
		vals['phone'] = '+91-'+vals['phone']
		print "modified vals ",vals
		rec = super(Teacher, self).create(cursor, user, vals, context=context)
		
		return rec

	


 	


 	
 	

