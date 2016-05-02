# -*- coding: utf-8 -*-
import facebook
import json
import requests
import thread

#Crear Archivos
#postsFile = open('Data/posts.txt', 'w')
#likesFile = open('Data/likes.txt', 'w')
#commentsFile = open('Data/comments.txt', 'w')

#Acceso a Facebook
token = ''
graph = facebook.GraphAPI(access_token=token, version='2.2')

def pruebaUsuario():
    #10151981468682251 Marco Lozano Sierra
    #10204409256658491
    #picture = graph.get_object("10151981468682251/picture")
    #print picture["url"]

    picture = graph.get_object("10151407860159534/picture")
    print picture

pruebaUsuario()

#profile = graph.get_object("chocolatesjet")
#profile = graph.get_object("hamburguesaselcorral")

"""
#posts = graph.get_object(profile['id']+"/posts",since='2010-01-01', until='2015-01-01',limit=50)
posts = graph.get_object(profile['id']+"/posts")


def getLikes(likes):
    try:
        while(True):
            likesFile = open('Data/likes.txt', 'a')
            JDictLikes= json.loads(json.dumps(likes))
            for like in JDictLikes['data']:
                likeProfile = graph.get_object(like['id'])
                likesFile.write(json.dumps(likeProfile)+"\n")

            likes=requests.get(likes['paging']['next']).json()
    except KeyError:
        print "Error in Likes"
        likesFile.close()

def getComments(comments):
    try:
        while(True):
            commentsFile = open('Data/comments.txt', 'a')
            JDictComments= json.loads(json.dumps(comments))

            for comment in JDictComments['data']:

                commentsFile.write(json.dumps(comment)+"\n")

            #if "next" in comments['paging']:
            comments=requests.get(comments['paging']['next']).json()
    except Exception as e:
        print "Errorrrr " + e.message
        commentsFile.close()



try:
    while(True):
        postsFile = open('Data/posts.txt', 'a')
        JDictPosts= json.loads(json.dumps(posts))
        for post in JDictPosts['data']:
            if "message" in post:
#               [Opción 1]
                #postsFile.write(json.dumps(po['created_time'].encode('utf-8'))+" "+json.dumps(po['message'].encode('utf-8'))+ "\n")

#               [Opción 2]
                #json.dump(po['message'] , postsFile, ensure_ascii=True, encoding="utf-8")

#               [Opcion 3]
#                string = unicode(json.dumps(po['message'] , 'utf8'))+ "\n"
#                string_for_output = string.encode('utf8', 'replace')
#                postsFile.write( string_for_output )

#               [Opción 4]
                #string = unicode(json.dumps(po['message']),encoding='utf-8', errors='replace')#+ "\n"
#               string.replace("é","e")
                #postsFile.write(string)
                postsFile.write(json.dumps(post)+"\n")

                #Extracción de LIKES
                if "likes" in post:
                    likes = post['likes']
#                    thread.start_new_thread( getLikes, (likes,) );
                    getLikes(likes)
                #Fin Extracción de LIKES

                #Extracción de COMMENTS
                if "comments" in post:
                    comments = post['comments']
#                    thread.start_new_thread( getComments, (comments,) );
                    getComments(comments)
                #Fin Extracción de COMMENTS

        posts=requests.get(posts['paging']['next']).json()

except Exception as e:
    print "Errorrrr in post: " + e.message
    postsFile.close()
print "Info guardada!"
"""
