import unittest
import coverage

# Script to run both the test files

cov = coverage.Coverage()
cov.start()

loader = unittest.TestLoader()
tests = loader.discover(start_dir='.', pattern='*_test.py')
test_runner = unittest.TextTestRunner()
result = test_runner.run(tests)

cov.stop()
cov.save()
cov.report()

print(result)

if not result.wasSuccessful():
    exit(1)
