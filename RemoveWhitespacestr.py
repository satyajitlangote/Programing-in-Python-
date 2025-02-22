# Removing All Whitespaces in a String
import re
string ="C O D E"
spaces=re.compiler(r'\s+')
result=re.sub(spaces," ",string)
print(result)


-----------------------------------------------------------------------------------------------------------------

