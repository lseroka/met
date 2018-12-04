import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in both UNSD M49 country and area .csv file
	(tab delimited) as well as the UNESCO heritage site .csv file (tab delimited).
	Extract regions, sub-regions, intermediate regions, country and areas, and
	other column data.  Filter out duplicate values and NaN values and sort the
	series in alphabetical order. Write out each series to a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read {0}',
		'MET Department written to file {0}',
		'MET Classification written to file {0}',
		'MET Acquisition written to file {0}',
		'MET City written to file {0}',
		'MET Country written to file {0}',
		'MET Region written to file {0}',
		'MET Object Title written to file {0}'
		# 'UNESCO heritage site regions written to file {0}',
		# 'UNESCO heritage site transboundary values written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


	
	# Read in MET data set (comma separator)
	met_csv = './scripts/input/csv/met_artwork_trimmed.csv'
	met_data_frame = read_csv(met_csv, '\t')
	# met_data_frame_trimmed = trim_columns(met_data_frame)
	# met_trimmed_csv = './scripts/output/master_spreadsheet_trimmed.csv'
	# write_series_to_csv(met_data_frame_trimmed, met_trimmed_csv, '\t', False)
	logging.info(msg[0].format(os.path.abspath(met_csv)))



	#write deprtatment to a csv file
	met_dept = extract_filtered_series(met_data_frame, 'department')
	met_dept_tsv = './scripts/output/met_dept.tsv'
	write_series_to_csv(met_dept, met_dept_tsv, '\t', False)
	logging.info(msg[1].format(os.path.abspath(met_dept_tsv)))

	# write classification to a csv file
	met_classification = extract_filtered_series(met_data_frame, 'classification')
	met_classification_tsv = './scripts/output/met_classification.tsv'
	write_series_to_csv(met_classification, met_classification_tsv, '\t', False)
	logging.info(msg[2].format(os.path.abspath(met_classification_tsv)))

	# #write acquisition to a csv file 
	# met_acquisition = extract_filtered_series(met_data_frame_trimmed, 'acquisition')
	# met_acquisition_tsv = './scripts/output/met_acquisition.tsv'
	# write_series_to_csv(met_acquisition, met_acquisition_tsv, '\t', False)
	# logging.info(msg[3].format(os.path.abspath(met_acquisition_tsv)))

	#write city to a csv file
	met_city = extract_filtered_series(met_data_frame, 'city')
	met_city_tsv = './scripts/output/met_city.tsv'
	write_series_to_csv(met_city, met_city_tsv, '\t', False)
	logging.info(msg[4].format(os.path.abspath(met_city_tsv)))

	#write country to a csv file
	met_country = extract_filtered_series(met_data_frame, 'country')
	met_country_tsv = './scripts/output/met_country.tsv'
	write_series_to_csv(met_country, met_country_tsv, '\t', False)
	logging.info(msg[5].format(os.path.abspath(met_country_tsv)))

	#write region to a csv file
	met_region = extract_filtered_series(met_data_frame, 'region')
	met_region_tsv = './scripts/output/met_region.tsv'
	write_series_to_csv(met_region, met_region_tsv, '\t', False)
	logging.info(msg[6].format(os.path.abspath(met_region_tsv)))

	#write object title to a csv file
	met_title = extract_filtered_series(met_data_frame, 'object_title')
	met_title_tsv = './scripts/output/met_title.tsv'
	write_series_to_csv(met_title, met_title_tsv, '\t', False)
	logging.info(msg[7].format(os.path.abspath(met_title_tsv)))
 



	#Write mediums to a csv file

	#Write artists to a csv file

	#write role to a csv file

	#write nationality to a csv file

	



	# # Read in United Nations Statistical Division (UNSD) M49 Standard data set (tabbed separator)
	# unsd_csv = './input/csv/un_area_country_codes-m49.csv'
	# unsd_data_frame = read_csv(unsd_csv, '\t')
	# logging.info(msg[0].format(os.path.abspath(unsd_csv)))


	# # Write regions to a .csv file.
	# unsd_region = extract_filtered_series(unsd_data_frame, 'region_name')
	# unsd_region_csv = './output/unsd_region.csv'
	# write_series_to_csv(unsd_region, unsd_region_csv, '\t', False)
	# logging.info(msg[1].format(os.path.abspath(unsd_region_csv)))

	# # Write sub-regions to a .csv file.
	# unsd_sub_region = extract_filtered_series(unsd_data_frame, 'sub_region_name')
	# unsd_sub_region_csv = './output/unsd_sub_region.csv'
	# write_series_to_csv(unsd_sub_region, unsd_sub_region_csv, '\t', False)
	# logging.info(msg[2].format(os.path.abspath(unsd_sub_region_csv)))

	# # Write intermediate_regions to a .csv file.
	# unsd_intermed_region = extract_filtered_series(unsd_data_frame, 'intermediate_region_name')
	# unsd_intermed_region_csv = './output/unsd_intermed_region.csv'
	# write_series_to_csv(unsd_intermed_region, unsd_intermed_region_csv, '\t', False)
	# logging.info(msg[3].format(os.path.abspath(unsd_intermed_region_csv)))

	# # Write countries or areas to a .csv file.
	# unsd_country_area = extract_filtered_series(unsd_data_frame, 'country_area_name')
	# unsd_country_area_csv = './output/unsd_country_area.csv'
	# write_series_to_csv(unsd_country_area, unsd_country_area_csv, '\t', False)
	# logging.info(msg[4].format(os.path.abspath(unsd_country_area_csv)))

	# # Write development status to a .csv file.
	# unsd_dev_status = extract_filtered_series(unsd_data_frame, 'country_area_development_status')
	# unsd_dev_status_csv = './output/unsd_dev_status.csv'
	# write_series_to_csv(unsd_dev_status, unsd_dev_status_csv, '\t', False)
	# logging.info(msg[5].format(os.path.abspath(unsd_dev_status_csv)))

	


	# # Read UNESCO heritage sites data (tabbed separator)
	# unesco_csv = './input/csv/unesco_heritage_sites.csv'
	# unesco_data_frame = read_csv(unesco_csv, '\t')
	# logging.info(msg[0].format(os.path.abspath(unesco_csv)))

	# # Write UNESCO heritage site countries and areas to a .csv file
	# unesco_country_area = extract_filtered_series(unesco_data_frame, 'country_area')
	# unesco_country_area_csv = './output/unesco_heritage_site_country_area.csv'
	# write_series_to_csv(unesco_country_area, unesco_country_area_csv, '\t', False)
	# logging.info(msg[6].format(os.path.abspath(unesco_country_area_csv)))

	# # Write UNESCO heritage site categories to a .csv file
	# unesco_site_category = extract_filtered_series(unesco_data_frame, 'category')
	# unesco_site_category_csv = './output/unesco_heritage_site_category.csv'
	# write_series_to_csv(unesco_site_category, unesco_site_category_csv, '\t', False)
	# logging.info(msg[7].format(os.path.abspath(unesco_site_category_csv)))

	# # Write UNESCO heritage site regions to a .csv file
	# unesco_region = extract_filtered_series(unesco_data_frame, 'region')
	# unesco_region_csv = './output/unesco_heritage_site_region.csv'
	# write_series_to_csv(unesco_region, unesco_region_csv, '\t', False)
	# logging.info(msg[8].format(os.path.abspath(unesco_region_csv)))

	# # Write UNESCO heritage site transboundary values to a .csv file
	# unesco_transboundary = extract_filtered_series(unesco_data_frame, 'transboundary')
	# unesco_transboundary_csv = './output/unesco_heritage_site_transboundary.csv'
	# write_series_to_csv(unesco_transboundary, unesco_transboundary_csv, '\t', False)
	# logging.info(msg[9].format(os.path.abspath(unesco_transboundary_csv)))


def extract_filtered_series(data_frame, column_name):
	"""
	Returns a filtered Panda Series one-dimensional ndarray from a targeted column.
	Duplicate values and NaN or blank values are dropped from the result set which is
	returned sorted (ascending).
	:param data_frame: Pandas DataFrame
	:param column_name: column name string
	:return: Panda Series one-dimensional ndarray
	"""
	return data_frame[column_name].drop_duplicates().dropna().sort_values()


def read_csv(path, delimiter=','):
	"""
	Utilize Pandas to read in *.csv file.
	:param path: file path
	:param delimiter: field delimiter
	:return: Pandas DataFrame
	"""
	return pd.read_csv(path, sep=delimiter, encoding= "ISO-8859-1", engine='python')


def trim_columns(data_frame):
	"""
	:param data_frame:
	:return: trimmed data frame
	"""
	trim = lambda x: x.strip() if type(x) is str else x
	return data_frame.applymap(trim)

def write_series_to_csv(series, path, delimiter=',', row_name=True):
	"""
	Write Pandas DataFrame to a *.csv file.
	:param series: Pandas one dimensional ndarray
	:param path: file path
	:param delimiter: field delimiter
	:param row_name: include row name boolean
	"""
	series.to_csv(path, sep=delimiter, index=row_name)


if __name__ == '__main__':
	sys.exit(main())