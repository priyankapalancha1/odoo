from openerp.osv import fields, osv

class Student(osv.osv):

	_name = "student"
	_description="studentsdetails"
	_columns = {
	'name' : fields.char('name', size=20, required=True),
	'age' : fields.char('age', size=20, required=True),
	'address' : fields.char('address', size=20, required=True),
	'branch' : fields.char('branch', size=20, required=True),

	'student_id' : fields.one2many('teacher','teacher_id','teacher_details'),

	'date_start' : fields.datetime('datestart', required=True),
	'date_stop' : fields.datetime('datestop', required=True),
	}