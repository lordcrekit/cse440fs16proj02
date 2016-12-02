import argparse;

parser = argparse.ArgumentParser(description="Todo: write description.");
parser.add_argument("-t", "--tokens", action="store_true", help="Print tokens instead of answer.");
parser.add_argument("-s", "--syntax", action="store_true", help="Print syntax tree instead of answer.");
parser.add_argument("-d", "--debug", action="store_true", help="Debug mode. Print information about run.");

args = parser.parse_args();
