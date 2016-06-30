from openerp.osv import fields, osv

class Teacher(osv.osv):

	_name = "teacher"
	_description="teacher details"
	_columns = {
	'name' : fields.char('name', size=20, required=True),
	'age' : fields.char('age', size=20, required=True),
	'address' : fields.char('address', size=20, required=True),

	'teacher_id' : fields.many2one('school.school', 'teacher_id'),

	'teach_id' : fields.many2many('student','teacher_id','branch',string='student details'),
	}

