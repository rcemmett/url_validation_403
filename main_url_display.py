from url import URL
import sys, random

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

def main():
  filename = None
  if len(sys.argv) is not 2:
    print 'Usage: python main.py input-file'
    exit(1)

  inputfile = open(sys.argv[1])

  strings = get_strings(inputfile)
  urls = [URL(x) for x in strings]
  normalized = {}
  original = {}
  for url in urls:
    if url.getURL() in original:
      original[url.getURL()] = original[url.getURL()] + 1
    else:
      original[url.getURL()] = 1

    if url.getNormalized() in normalized:
      normalized[url.getNormalized()] = normalized[url.getNormalized()] + 1
    else:
      normalized[url.getNormalized()] = 1

  for url in urls:
    print "Source: " + url.getURL()
    if url.isValid():
      print "Valid: True"
    else:
      print "Valid: False"
    print "Canonical: " + url.getNormalized()
    if original[url.getURL()] == 1:
      print "Source unique: True"
    else:
      print "Source unique: False"
    if normalized[url.getNormalized()] == 1:
      print "Canonicalized unique: True"
    else:
      print "Canonicalized unique: False"
    

if __name__ == "__main__":
  main()