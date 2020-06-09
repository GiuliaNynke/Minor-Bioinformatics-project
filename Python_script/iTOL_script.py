import os
import sys
from itolapi import Itol, ItolExport

current_dir = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.join(current_dir, '..')
sys.path.append(root_path)
boom = Itol()

# Set the tree file
tree = os.path.join(current_dir, 'MERS_CoV.tree.txt')
boom.add_file(tree)

# Add parameters
boom.params['treeName']='MERS_CoV'
boom.params['display_mode']='2'
boom.params['ignore_branch_length']='1'
boom.params['current_font_size']='28'

# Check parameters
boom.print_variables()

# Submit the tree
print('')
print((
    'Uploading the tree.  This may take some time depending on how large the '
    'tree is and how much load there is on the itol server'
))
good_upload = boom.upload()
if not good_upload:
    print('There was an error:' + boom.comm.upload_output)
    sys.exit(1)

# Read the tree ID
print('Tree ID: ' + str(boom.comm.tree_id))

# Read the iTOL API return statement
print('iTOL output: ' + str(boom.comm.upload_output))

# Website to be redirected to iTOL tree
print('Tree Web Page URL: ' + boom.get_webpage())

# Warnings associated with the upload
print('Warnings: ' + str(boom.comm.warnings))

# Export the tree to pdf
print('Exporting to pdf')
itol_exporter = boom.get_itol_export()
export_location = os.path.join(current_dir, 'MERS_CoV.pdf')
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
itol_exporter.export(export_location)
print('exported tree to ', export_location)
