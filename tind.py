import requests, json, template, sys



def tind(token='''EAAGm0PX4ZCpsBAJZAyNmXsqXBWcFIlPajSZCcJ2pKKJMSZBtmrmRZCkLIS4ZAOZBn0LXLiwJV9OpZCpofxEEb4BzkqqknG9SxbtVDoQ6O5U8jTzZAOEyW0D7VwWVhyHi9jC1FZBNP9IcqHBZBqdmx8E6CCeYjD1Oa36IJZCXFdgGSBxH9AZDZD'''
, fb_id = str(100009796425951)):

    auth = {'facebook_token':token,'facebook_id':str(fb_id)}
    print(auth)

    s = requests.session()

    r = s.post('https://api.gotinder.com/auth', data=auth)

    auth_response = r.json()

    print(auth_response)

    s.headers.update({'X-Auth-Token': auth_response['token']
                         , 'Content-type': 'application/json'
                         , 'User-agent': 'Tinder/3.0.4 (iPhone; iOS 7.1; Scale/2.00)'
                      })

    r = s.get('https://api.gotinder.com/user/recs')

    results = r.json()

    try:
        people = results['results']
    except:
        return
    print(people[0])
    for person in people:
        data = {'pageName': person['name'], 'content' : [], 'meta' : {}}

        data['content'].append({'tag': 'h4', 'class': 'name', 'id': '', 'content': person['name']})

        if person['gender']:
            data['content'].append({'tag': 'p', 'class': 'gender', 'id': '', 'content': 'Girl'})
        else:
            data['content'].append({'tag': 'p', 'class': 'gender', 'id': '', 'content': 'Guy'})
        data['content'].append({'tag': 'p', 'class': 'bio', 'id': '', 'content': person['bio']})


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
            data['meta']['age'] = person['age']
        except:
            pass
        try:
            data['meta']['profilepic'] = person['profile_picture']
        except:
            data['meta']['profilepic'] = person['photos'][0]['processedFiles'][0]['url']


        for image in person['photos']:
            data['content'].append({'tag':'img','class':'image','id':'','content':image['processedFiles'][0]['url']})

        template.createPage(data)
        print('success')

if __name__ == '__main__':
    tind()


