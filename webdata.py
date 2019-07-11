import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
totalSum = 0

address = input('Indica una URL:')
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Info:', data)
