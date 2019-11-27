#!/usr/bin/env python3
import sys
import os

if not sys.stdin.isatty():
    print("Las dos primeras lineas de tu stdin son:")
    lines = ["{} -> {}".format(n, line.strip()) for n,line in enumerate(sys.stdin)]
    lines = lines[:2]
    print("\n".join(lines))

sys.stdout.write('Stdout\n')
sys.stderr.write('Stderr\n')

print(sys.argv)
print("VAR: {}".format(os.environ.get("VAR")))


print("name: {}".format(__name__))
    
sys.exit(8)
