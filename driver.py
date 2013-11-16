from __future__ import print_function
import sys
import commands
import subprocess
import os

def make_aligned_in_dir(dir_name):
  for directory in os.listdir(dir_name):
    if os.path.isdir(os.path.join(dir_name, directory)): 
      new_path = os.path.join(dir_name, directory)
      new_path = os.path.join(new_path, "model")
      in_file = os.path.join(new_path, "true.reduced.fasta")
      out_file = os.path.join(new_path, "unaligned.fasta")
      cmd = " ".join(["python unalign.py", in_file, out_file])
      #print ("running command "+ cmd + "\n")
      status, output = commands.getstatusoutput(cmd)
      if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(1)
      print (output)  ## Otherwise do something with the command's output 

def run_algo(dir_name, algo="baliphy"):
  for directory in os.listdir(dir_name):
    if os.path.isdir(os.path.join(dir_name, directory)): 
      new_path = os.path.join(dir_name, directory)
      new_path = os.path.join(new_path, "model")
      in_file = os.path.join(new_path, "unaligned.fasta")
      if algo == "baliphy":
        cmd = " ".join(["bali-phy", in_file, "&"])
      else:
        #mafft
        out_file = os.path.join(new_path, "out.mafft")
        cmd = " ".join(["mafft --localpair --maxiterate 1000 --quiet", in_file, ">", out_file, "&"])
      print ("running command "+ cmd + "\n")
      subprocess.Popen(cmd, shell=True)
      
      

def main():
  if len(sys.argv) != 3:
    print("Usage: driver.py <directory> (-unalign|-baliphy|-mafft|-clean)\n")
    sys.exit(1)
  if sys.argv[2] == "-unalign":
    make_aligned_in_dir(sys.argv[1])
    sys.exit(0)
  if sys.argv[2] == "-baliphy":
    run_algo(sys.argv[1], "baliphy")
    sys.exit(0)		
  if sys.argv[2] == "-mafft":
    run_algo(sys.argv[1], "mafft")
    sys.exit(0)
  if sys.argv[2] == "-clean":
    raise NotImplementedError
    sys.exit(0)


if __name__ == "__main__":
  main()			 		
