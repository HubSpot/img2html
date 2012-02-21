"""
Copyright 2011 HubSpot, Inc.

  Licensed under the Apache License, Version 2.0 (the 
"License"); you may not use this file except in compliance 
with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an 
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
either express or implied.  See the License for the specific 
language governing permissions and limitations under the 
License.
"""

import sys
from PIL import Image

# Check args
if not len(sys.argv) > 1:
    sys.exit("Please specify an input file!")

# Get RGB image data
image = Image.open(sys.argv[1])
image = image.convert('RGB')
pixels = image.load()
width, height = image.size

# Start table
print '<html><body>'
print '<table width="%spx" height="%spx" cellpadding="0" cellspacing="0">' % (width, height)

# Loop through rows
run_length = 1
for row in xrange(height):
    print '<tr>'
    
    # Loop through columns
    for col in xrange(width):

        # If this is not first row (to make sure we get all columns), the last column, and this is part of a run, increase colspan
        if row != 0 and col < width - 1 and pixels[col, row] == pixels[col + 1, row]:
            run_length = run_length + 1
        
        # If there is no run, or this is the end of a run, output this pixel (with no newline)
        else:
            color = '#%x%x%x' % pixels[col, row]
            colspan = 'colspan="%s"' % run_length if run_length > 1 else ''
            print '<td bgcolor="%s" width="%spx" height="1px" %s></td>' % (color, run_length, colspan),
            run_length = 1

    print '</tr>'

# Finish up
print '</table>'
print '</body></html>'
