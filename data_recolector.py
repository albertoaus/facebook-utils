# -*- coding: utf-8 -*-
__author__ = 'aus'

import facebook
import json
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Argument 1:', sys.argv[0]
print 'Argument 2:', sys.argv[1]

group_id = sys.argv[1]

access_token = "EAACEdEose0cBAI5cJuSU8BCGiliHYa1J8kNJN0608AEZCHkTjVt0MvPoagSpC9ZAkbt1vkjdroQYDMcyondYepYS5ZA78WvmODWZAoyZAOfuu7GeXTPSWiZBuomYxNMrO8RrIr9rKxghqSHYlMheepqGfCLZAUhomYEljZCgYANJYAZDZD"
version = "2.4"

graph = facebook.GraphAPI(access_token, version)
graph.timeout = 100

# Get all the comments from a post
connection_name = 'feed'
feed = graph.get_connections(group_id, connection_name)
feed_data = feed['data']

# Feed lenght
feed_len = len(feed_data)
print "Feed lenght is " + str(feed_len)


#Extract the valid data of each post(message, creation time and id)
valid_info_list = []

for i in range(0, (feed_len)):

    post = {}

    post['message'] = feed_data[i]['message']
    post['creation'] = feed_data[i]['created_time']
    post['id'] = feed_data[i]['id']
    valid_info_list.append(post)

# post = {}
#
# post['message'] = feed_data[0]['message']
# post['creation'] = feed_data[0]['created_time']
# post['id'] = feed_data[0]['id']
#
#
# #I need to delete de 'u, \n,\u20ac ,... from the dictionary
#
#
# valid_info_list.append(post)
#
# print post

#Save the Json into a file
with open('test.json', 'w') as outfile:
    json.dump(valid_info_list, outfile)
