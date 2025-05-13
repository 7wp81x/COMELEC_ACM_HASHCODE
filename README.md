
# COMELEC ACM HASHCODE ISSUE

This repo was created in order to compare the MD5 checksums of files listed in the Comelec [Source Code Hash Manifest](https://comelec.gov.ph/?r=2025NLE%2FLocalSourceCodeReview%2FHashManifest_2025),
which is typically in PDF format for different software versions ([3.4.0](https://comelec.gov.ph/php-tpls-attachments/2025NLE/SCH/01312025_SourceHashes/phl-acm-3.4.0_md5.pdf) and [v3.5.0](https://comelec.gov.ph/php-tpls-attachments/2025NLE/SCH/phl-acm-3.5.0_20250328_md5.pdf)) used in Automated Counting Machines (ACMs).

The goal is to identify newly added or modified files between the two versions (**3.4.0** and **3.5.0**), ensuring transparency and detecting potential discrepancies in the election system software.


### Requirements:
```
pip3 install pdfplumber pandas
```

### Usages:
Tool used for converting PDF files containing MD5 checksums of files for two software versions [3.4.0](https://comelec.gov.ph/php-tpls-attachments/2025NLE/SCH/01312025_SourceHashes/phl-acm-3.4.0_md5.pdf) and [3.5.0](https://comelec.gov.ph/php-tpls-attachments/2025NLE/SCH/phl-acm-3.5.0_20250328_md5.pdf) into CSV format for easy comparison.  
Usage:
```
python3 pdf_to_csv.py <filename.pdf> <output.csv>
```

Tool for comparing two software versions. This will display what are newly added files and modified files between the two software versions.  
Usage:
```
python3 compare_md5.py <version1>.csv <version2>.csv
```

# Results
[View not modified files](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/results/results_not_modified_files.txt)  
[View modified non-build? files](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/results/results_modified_src_files.txt)
[View all modified files](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/results/results_all_modified_files.txt)
[View all new files](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/results/results_all_new_files.txt)


# Screenshots

![New files demo](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/Screenshots/Screenshot%20from%202025-05-13%2014-57-01.png)  
*Screenshot example output of newly added files.*

![Modified files](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/Screenshots/Screenshot%20from%202025-05-13%2014-55-57.png)  
*Screenshot example output of modified files.*

![Weird file naming](https://raw.githubusercontent.com/7wp81x/COMELEC_ACM_HASHCODE/refs/heads/main/Screenshots/Screenshot%20from%202025-05-13%2014-58-15.png)  
*Screenshot weird directory `worm*` has `setup` and `startup`.*

### Conclusion
There are some source code that was modified. But most **build artifacts** (e.g., compiled binaris) were included in v3.5.0, which were **not present** in v3.4.0 — which leads to the hash mismatch.
