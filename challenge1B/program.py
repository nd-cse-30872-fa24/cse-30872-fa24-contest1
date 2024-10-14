#!/usr/bin/env python3
import sys

def isomorphic(s, t):
    # Length check
    if len(s) != len(t):
        return False
    mapping = {}
    # Avoid to map same character
    used_t_chars = set()
    # Use zip to match letter
    for c1, c2 in zip(s, t):
        if c1 in mapping:
            # Not matching
            if mapping[c1] != c2:
                return False
        else:
            # No same letter
            if c2 in used_t_chars:
                return False
            mapping[c1] = c2
            used_t_chars.add(c2)
    return True

def main():
    lines = sys.stdin.read().strip().splitlines()
    for line in lines:
        words = line.strip().split()
        s, t = words
        if isomorphic(s, t):
            print("Isomorphic")
        else:
            print("Not Isomorphic")

if __name__ == '__main__':
    main()
