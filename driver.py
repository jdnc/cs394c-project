from __future__ import print_function
import sys
import commands
import os

def make_aligned_in_dir(dir_name):
  for directory in os.listdir(dir_name):
    if os.path.isdir(os.path.join(dir_name, directory)): 
      new_path = os.path.join(dir_name, directory)
      new_path = os.path.join(new_path, "model")
      in_file = os.path.join(new_path, "true.reduced.fasta")
      out_file = os.path.join(new_path, "unaligned.fasta")
      cmd = " ".join(["python unalign.py", in_file, out_file])
      print ("running command "+ cmd)
      status, output = commands.getstatusoutput(cmd)
      if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(1)
      print (output)  ## Otherwise do something with the command's output 


def main():
  if len(sys.argv) != 2:
    print("Usage: driver.py <directory>\n")
    sys.exit(1)
  make_aligned_in_dir(sys.argv[1])


if __name__ == "__main__":
  main()			 		
