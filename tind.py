import requests, json, template, sys



#fb_id = sys.argv[1]
#token = sys.argv[2]



token = '''CAAGm0PX4ZCpsBAPCTHOySDDNZA2YA1SV83no7ZAlIeSQabyhZCV9MAJXtCoHbBMAhVXZARtgjg61cbKuQy39PkB6Jt0ZBLkvRt8e2Yr826IiZBrILgjerp8LRPEllc9lZBprZAU7TMZBSWv8ZAHcVZBOg4dldfH6oRmLZAMYnuFEn3UJ5UXfI8eZCcqApOb9CC4yv3dVcA1SvvZAtEySAZDZD'''



fb_id = str(100011654715820)

auth = {'facebook_token':token,'facebook_id':fb_id}

s = requests.session()




r = s.post('https://api.gotinder.com/auth', data=auth)

auth_response = r.json()




s.headers.update({'X-Auth-Token': auth_response['token']
                     , 'Content-type': 'application/json'
                     , 'User-agent': 'Tinder/3.0.4 (iPhone; iOS 7.1; Scale/2.00)'
                  })





print(r.text)

r = s.get('https://api.gotinder.com/user/recs')

results = r.json()
print(results)

people = results['results']

print(people[0])
for person in people:
    data = {'pageName': person['name'], 'content' : [], 'meta' : {}}

    data['content'].append({'tag':'p', 'class':'bio', 'id':'', 'content':person['bio']})

    r = s.get('https://api.gotinder.com/like/{}'.format(person['_id']))


    try:
        data['meta']['bio'] = person['bio']
    except:
        pass
    try:
        data['meta']['name'] = person['name']
    except:
        pass
    try:
        data['meta']['distance'] = person['distance_mi']
    except:
        pass
    try:
        data['meta']['gender'] = person['gender']
    except:
        pass
    try:
        data['meta']['username'] = person['username']
    except:
        pass
    try:
        data['meta']['profilepic'] = person['profile_picture']
    except:
        data['meta']['profilepic'] = person['photos'][0]['processedFiles'][0]['url']


    for image in person['photos']:
        data['content'].append({'tag':'img','class':'image','id':'','content':image['processedFiles'][0]['url']})

    template.createPage(data)




