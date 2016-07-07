
import sys
from pyspatialite import dbapi2 as db

def _buildUpdateWhereClauseSpatialite(table, update_field,
                                      lookup_field, valueList):
    valueList = ["'%s'" % value for value in valueList]
    whereClause = (
        "update %s set %s = datetime('now', 'localtime') where %s IN(%s)" % (
            table, update_field, lookup_field, ', '.join(map(str, valueList))))
    return whereClause

database = sys.argv[1]
ids = eval(sys.argv[2])
query = _buildUpdateWhereClauseSpatialite('SuspiciousRecheck', 'pp_timestamp', 'tree_uid', ids)
# print 'the database is {}'.format(database)
# print 'the ids are {}'.format(ids)
# print 'the query is {}'.format(query)

# print 'connecting'
conn = db.connect(database)
# print 'connected'
c = conn.cursor()
# print 'executing'
c.execute(query)
# print 'committing'
conn.commit()
# print 'commited'
conn.close()