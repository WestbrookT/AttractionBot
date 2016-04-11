import requests, json, template, sys
import urllib, os
from blogengine import pageLocation

path = os.path.join(pageLocation, '..')



def tind():

    auth = {'facebook_token':token,'facebook_id':str(fb_id)}
    print(auth)

    s = requests.session()

    r = s.post('https://api.gotinder.com/auth', data=auth)
    print(r.text)
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
        print(results)
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

        images = []
        for image in person['photos']:
            data['content'].append({'tag':'img','class':'image','id':'','content':image['processedFiles'][0]['url']})
            images.append(image['processedFiles'][0]['url'])
        print(images)

        hotness = 0.0
        number = 0

        for i in images:
            print(i)
            img = urllib.request.urlopen(i)
            f = open(os.path.join(path, 'test.jpg'), 'wb')
            f.write(img.read())
            f.close()

            headers = {'browseFile': ('test.jpg', open(os.path.join(path, 'test.jpg'), 'rb'))}
            response = requests.post('http://www.howhot.io/main.php', files=headers)
            message = response.json()
            try:
                print(message['message']['hotness'])
                hotness += float(message['message']['hotness'])
                number += 1
                print(hotness)
            except:
                pass


        if number == 0 or hotness/number >= 5:
            try:
                print('overall value: ')
                print(hotness/number)
            except:
                pass
            r = s.get('https://api.gotinder.com/like/{}'.format(person['_id']))
            template.createPage(data)
        print('success')

if __name__ == '__main__':
    tind()


