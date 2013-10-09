'''
author : jack_lcz
'''

import gflags
import MySQLdb
import sqlalchemy
FLAGS = gflags.FLAGS
gflags.DEFINE_boolean('echosql',False,"is echo sql?")
gflags.DEFINE_string('dbuser','test','mysql user')
gflags.DEFINE_string('dbpasswd','test','mysql password')
gflags.DEFINE_string('db','test','database')
gflags.DEFINE_string('dbhost','127.0.0.1','mysql host')
gflags.DEFINE_string('dbport','3306','mysql port')



def get_db_engine(**kwargs):
    echosql = kwargs.get('echosql') if kwargs.has_key('echosql') else FLAGS.echosql
	connstr = kwargs.get('connstr')
	if connstr:
        return create_engine(connstr, echo=echosql)
    dbuser = kwargs.get('dbuser') if kwargs.has_key('dbuser') else FLAGS.dbuser
    dbpasswd = kwargs.get('dbpasswd') if kwargs.has_key('dbpasswd') else FLAGS.dbpasswd
    dbhost = kwargs.get('dbhost') if kwargs.has_key('dbhost') else FLAGS.dbhost
	dbport = kwargs.get('dbport') if kwargs.has_key('dbport') else FLAGS.dbport
	dbtimeout = kwargs.get('dbtimeout') if kwargs.has_key('dbtimeout') else FLAGS.dbtimeout
	db = kwargs.get('db') if kwargs.has_key('db') else FLAGS.db
    return create_engine('mysql://%s:%s@%s:%s/%s?charset=utf8' % (dbuser, dbpasswd, dbhost, dbport, db), echo=echosql, pool_recycle=dbtimeout)



