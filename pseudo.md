-under construction-

PSEUDO CODE:


PART 1) Retrieve Asset information from selected scan

-> Authentication Start API
->Get all scans
-> get all assets from a particular or selected scan
-> iterate asset list to retrieve details for a particular asset

Output Nested dictionary:
 {name of scan: [asset_list [asset name: [details]]]}


	- Benefits of a nested dictionary:

	Can be interpreted as JSON, useful for apis and report formatting. Beneficial for next stage


PART 2) send email/reports to accounts associated with assets from scan

->Read input file (citrix export of accounts associated with desktops)
-> compare input file with asset export from part 1)
	Binary search or linear search (will probably go for a binary search as it can be faster)
->associate asset with account
->issue api call to send reports to email.
