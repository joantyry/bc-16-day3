def words(mylst):
	'''
	This function outputs the number of occurence of each word in a given list.
	'''
  mylst2 = {}
  for word in list(mylst.split()):
    
    try:
      word_count = int(word)
    except ValueError:

      mylst2[word] = mylst.split().count(word)

    else:

      mylst2[int(word)] = mylst.split().count(word)

  return mylst2
    
    

print words("joan ate joan")    