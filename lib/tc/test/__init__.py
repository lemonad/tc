# encoding: utf-8
import unittest, sys, os

def suite():
  suites = []
  import tc.test.hdb, tc.test.bdb, tc.test.tdb
  suites.append(tc.test.hdb.suite())
  suites.append(tc.test.bdb.suite())
  suites.append(tc.test.tdb.suite())
  return unittest.TestSuite(suites)

def test(*va, **kw):
  runner = unittest.TextTestRunner(*va, **kw)
  return runner.run(suite())

if __name__ == "__main__":
  test()
