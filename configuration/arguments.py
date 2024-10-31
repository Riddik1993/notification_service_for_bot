import argparse
from argparse import Namespace


def get_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument("future_hours_min", type=int)
    parser.add_argument("future_hours_max", type=int)
    return parser.parse_args()
