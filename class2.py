# class user():
#     def __init__(self):
#
#
# user1=user()
# user1.id=001
# user1.name="biju"
#
# print(user1.name)




#
# class user():
#     def __init__(self,id,username,followers,following):
#         self.id=id
#         self.username=username
#         self.followers=followers
#         self.following=following
#
# user1=user("001","biju",600,300)
# print(f'{user1.id}\n{user1.username}\n{user1.followers}\n{user1.following}')

class insta():
    def __init__(self,id,username):
        self.id=id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=insta("001","biju")
# print(f'{user1.id}\n{user1.username}\n{user1.followers}\n{user1.following}')
user2=insta("002","ravi")
# user1.follow()
# print(f'{user1.id}\n{user1.username}\n{user1.followers}\n{user1.following}')

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)



user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)










































