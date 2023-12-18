import argparse
import sys
from django.conf import settings
from django.test.utils import get_runner

def run_tests(test_labels, verbosity=1):
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=verbosity)
    failures = test_runner.run_tests(test_labels)
    sys.exit(bool(failures))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Django tests.')
    parser.add_argument('-t', '--test', help='Run specific test or test module.')
    parser.add_argument('-a', '--all', action='store_true', help='Run all tests.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    parser.add_argument('-l', '--list', action='store_true', help='List available tests.')

    args = parser.parse_args()

    if args.list:
        # Implement functionality to list all tests
        pass
    elif args.test:
        run_tests([args.test], verbosity=2 if args.verbose else 1)
    elif args.all:
        run_tests(['core'], verbosity=2 if args.verbose else 1)
    else:
        parser.print_help()
