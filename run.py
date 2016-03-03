import otmcountypy as o

jobtype = 's000' # all jobs (optional setting in arrangedata)
year = '2013' # vintage of data

print "1 - Gathering OTM zip files"
otm_zip_files = o.otm_gatherzips('county_to_county_data/')

print "2 - Extracting data to folders"
otm_zip_folders = o.otm_unzip(otm_zip_files)

print "3 - Organizing data"
finalized_data = o.otm_arrangedata(otm_zip_folders, year, jobtype)

print "4 - Creating final table"
final_table = o.otm_createtable(finalized_data)

print "5 - Writing data to file"
o.otm_writedata(final_table, 'output.csv')

print "6 - Clean up"
o.otm_cleanupfolders(otm_zip_folders)

print "Complete"
