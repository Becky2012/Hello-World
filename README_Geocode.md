.# Hello-World
Programs: Geocode_impute.py
This code is to impute the missing values by using closest match with the same variable in reference file.
Given two tables with two variables (one is used to perform match, the other is with missing values need to impute. Please see the sample data source in data folder.

Both tables will have non-missing values for ZIP. A record in input file can have either a 5-character ZIP or a 9-character ZIP, but records in reference will always have the complete 9-character ZIP and it will never have missing values for GEOCODE
To fill in the missing values, my designed steps are as follow:
1) Identify the observations with missing values
2) The closest match will be the record that matches on the most digits of ZIP: a full 9-character match on ZIP is best
3) If the 9-character ZIP does not exist in the reference, then I impute based on an 8-character match (the first 8 characters), then 7 characters, etc. down to a 5-character match. 

                                           Example of Code Output
                                                ZIP	  GEOCODE	
                                       111111111	420562314985676	
                                       111111112	420562314987845  	#<Imputed with 9 char ZIP>
                                       234561111	764329172845372  	#<Imputed with 9 char ZIP>
                                       33333	    673827498716253  	#<Imputed with 9 char ZIP>
                                       3333322	  673827498716253  	#<Imputed with 9 char ZIP>
                                          ...          ...
                                          ...          ...
                                       444444444	673827498717894	#<Imputed with 9 char ZIP>
 Note: The data used for this work sample is test data only and not real. I ran the data for testing purposes. 

