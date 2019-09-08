# Ask use list of 3 friends
# for each friend tell if they are nearby
# save them in near by friends file

friends = input('Enter 3 friends name, seperated by commas : ').split(',')
print(friends)

people = open('people.txt', 'r')

people_list = [line.strip() for line in people.readlines()]
print(people)
print(people_list)

people.close()

friends_set = set(friend.strip() for friend in friends)
people_set = set(people_list)

print(friends_set)
print(people_set)

friends_nearby_set = friends_set.intersection(people_set)

print(friends_nearby_set)

friends_nearby_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby ')
    friends_nearby_file.write(f'{friend}\n')

friends_nearby_file.close()

