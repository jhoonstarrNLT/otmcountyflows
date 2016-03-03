from . import logger

def otm_createtable(finalized_data):

    if not finalized_data:
        logger.error("No data passed for table creation")
        sys.exit(1)

    try:
        logger.debug("Creating final table")
        counties = sorted(finalized_data.keys())

        output = []

        columnlabels = ['']
        for county in counties: 
            columnlabels.append(county)

        output.append(columnlabels)

        for county in counties:
            data_dict = finalized_data[county]
            row = [county]
            for county in counties:
                if county in data_dict.keys():
                    row.append(data_dict[county])
                else:
                    row.append('NaN')

            output.append(row)

        return output

    except Exception, e:
            logger.error("Error creating output")
            logger.error("Failed: {0}".format(str(e)))



