#!/usr/bin/python

# IMPORTS:
import cgitb
cgitb.enable()
import cgi

import base, settings, test
from connect import connect
# :IMPORTS

# FUNCTIONS:
def revoke_test(db, test_id, revoke=True, comment="default"):
	con = connect(True, db)
	cur = con.cursor()
	
	# The following method escapes characters correctly:
	cmd = "INSERT INTO TestRevoke (test_id, comment) VALUES (%s, %s)"
	values = (test_id, comment)
	cur.execute(cmd, values)
	con.commit()

def main():
	# Arguments:
	form = cgi.FieldStorage()
	test_id = base.cleanCGInumber(form.getvalue('test_id'))
	comment = form.getvalue('comment')
	db = settings.get_db()
	card_id = test.fetch_cardid_from_testid(db, test_id)
	testtype_id = test.fetch_testtypeid_from_testid(db, test_id)
	
	# Revoke:
	revoke_test(db, test_id, revoke=True, comment=comment)
	
	# Basic:
	base.begin()
#	base.header(title='{0}: revoke'.format(db))
	base.header_redirect("module.py?db={0}&card_id={1}#test-{2}".format(db, card_id, testtype_id))
	base.top(db)

	base.bottom()
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN
