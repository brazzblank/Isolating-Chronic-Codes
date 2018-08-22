# Isolating-Chronic-Medical-Codes.py

This was made for a project of isolating each instance of a chronic ICD9, ICD10, or SNOMED code from millions of rows of data, which would then be used for further analysis. 

This was made using python 2.7

In the database the medical codes appear as SNOMED!1234 so the initial hurdle was separating the string 'SNOMED!' from the number because the reference code csv's sometimes had the string and sometimes didnt. Depended on who sent the files.
