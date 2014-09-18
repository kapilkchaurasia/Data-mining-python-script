# GIVE YOU THE ID OF ALL CONNECTIONS OF YOURS AND USING ID FEILD TO DATA MINE "EDUCATIONS AND JOB FREQUENCY " OF YOUR CONNECTION
# BY LOOKING  "https://developer.linkedin.com/documents/profile-fields#fullprofile" YOU CAN EASILY MANIPULATE BELOW SRC CODE AND DATA MINE ACCORDING TO YOUR NEED 


from linkedin import linkedin 
import json
import re

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = 'xxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxx'
USER_TOKEN = 'XXXXXXXXXXXX'
USER_SECRET = 'XXXXX'

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

connections=app.get_connections()


connections_data = '/home/kapil.ch/linkedin DM/linkedindata'

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()



# DATA MINING EDUCATION FEILD
for k,v in connections.items():

	if(k=='values' ):
		for x in v:
			for k1,v1 in x.items():
				#print k1
				if(k1=="id"):
					#print v1
					xyz= app.get_profile(member_id=v1,selectors= ['person:(educations)'])
					print xyz

# DATA MINING JOBS OF YOUR CONNECTION IN SORTED ORDER
titles = []
for contact in contacts:
    titles.extend([t.strip() for t in contact['Job Title'].split('/')
                  if contact['Job Title'].strip() != ''])

# Replace common/known abbreviations

for i, _ in enumerate(titles):
    for transform in transforms:
        titles[i] = titles[i].replace(*transform)

# Print out a table of titles sorted by frequency

pt = PrettyTable(field_names=['Title', 'Freq'])
pt.align = 'l'
c = Counter(titles)
[pt.add_row([title, freq]) 
 for (title, freq) in sorted(c.items(), key=itemgetter(1), reverse=True) 
     if freq > 1]
print pt

# Print out a table of tokens sorted by frequency

tokens = []
for title in titles:
    tokens.extend([t.strip(',') for t in title.split()])
pt = PrettyTable(field_names=['Token', 'Freq'])
pt.align = 'l'
c = Counter(tokens)
[pt.add_row([token, freq]) 
 for (token, freq) in sorted(c.items(), key=itemgetter(1), reverse=True) 
     if freq > 1 and len(token) > 2]
print pt					

					
