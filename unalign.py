from __future__ import print_function
import re
import os
import sys

def make_unaligned(in_file, out_file):
  gap_pattern = re.compile("-+")
  with open(in_file, "rb") as f:
    raw_str = f.read()
  out_str = gap_pattern.sub("",raw_str)
  with open(out_file, "w") as f:
    f.write(out_str)
  
 
def main():
  if len(sys.argv) != 3:
    print("Usage: unalign.py <in_file> <out_file>\n")
    exit(1)
  in_file = sys.argv[1]
  out_file = sys.argv[2]
  make_unaligned(in_file, out_file)

if __name__ == "__main__":
  main()
