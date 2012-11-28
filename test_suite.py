from url import URL

def main():
  url1 = URL("example.com")
  url2 = URL(" ")
  url3 = URL("http://example.com/")
  url4 = URL("http://www.example.com")
  url5 = URL("http://z.com/")
  url6 = URL("http://example.com alsdfkj")
  url7 = URL("http://example.com ()")
  url8 = URL("google.com")
  
  
  #testing validity
  if not url1.isValid():
    print "Pass first test"
  else:
    print "Failed first test"

  if not url2.isValid():
    print "Pass second test"
  else:
    print "Failed second test"

  if url3.isValid():
    print "Pass third test"
  else:
    print "Failed third test"

  if not url4.isValid():
    print "Pass fourth test"
  else:
    print "Failed fourth test"

  if url5.isValid():
    print "Pass fifth test"
  else:
    print "Failed fifth test"

  if not url6.isValid():
    print "Pass sixth test"
  else:
    print "Failed sixth test"

  if not url7.isValid():
    print "Pass seventh test"
  else:
    print "Failed seventh test"


  if url3 == url3:
    print "Pass eighth test"
  else:
    print "Failed eighth test"

  if url3 < url5:
    print "Pass ninth test"
  else:
    print "Failed ninth test"

  if url1 != url3:
    print "Pass tenth test"
  else:
    print "Pass tenth test"


if __name__ == "__main__":
  main()

