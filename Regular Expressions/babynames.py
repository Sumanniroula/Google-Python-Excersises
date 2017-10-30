#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  file = open(filename, 'r')
  text = file.read()
  match = re.search(r'Popularity\sin\s\d\d\d\d', text) #matching text: 'popularity in [year]'
  print match.group()
  matched_item = match.group() #assigning variable for later use
  n = re.findall(r'(<td>\d+</td>)(<td>\w+</td>)(<td>\w+</td>)', text)#regular expression to find rank,boy's name and girl's name
  dict_boy = {} #empty dictionary assigned
  dict_girl = {}
  for i in n:
      dict_boy[i[1][4:][:-5]] = i[0][4:][:-5] #stored boy's name and it's respective rank in dict_boy. E.g: dict_boy = {'abdul':243,'sam':453}
      dict_girl[i[2][4:][:-5]] = i[0][4:][:-5] #similar for girl
  result = merge_dicts(dict_boy,dict_girl) #merging two dictionaries
  sorted_list = sorted(result.items()) #sorting the merged dictionary with key
  listt = [matched_item[-4:]] #last 4 values of matched_item is assigned as first item of list i.e. ['2006',...]
  for i in sorted_list:
      listt.append(i[0] + ' ' + i[1]) #['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  return listt
  


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # LAB(begin solution)
  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print text
  # LAB(end solution)

if __name__ == '__main__':
  main()
