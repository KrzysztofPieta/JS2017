import sys
print(sys.argv)
from decimal import Decimal

if(sys.argv[2]=='-'):
	print(Decimal(sys.argv[1])-Decimal(sys.argv[3]))
if (sys.argv[2]=='+'):\
	print(Decimal(sys.argv[1])+Decimal(sys.argv[3]))
if (sys.argv[2]=='*'):\
	print(Decimal(sys.argv[1])*Decimal(sys.argv[3]))
