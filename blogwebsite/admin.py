from django.contrib import admin
from blogwebsite.models import User,Post,Liked_post,Comment_post

class UserAdmin(admin.ModelAdmin):
    list_display=['address','first_name','last_name','email','password','phone_no','gender','profile_pic']
admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=['blog_heading','datetime','likes_count','comment','id']
admin.site.register(Post,PostAdmin)
class Liked_postAdmin(admin.ModelAdmin):
    list_display=['post_id','liker_email','is_liked']
admin.site.register(Liked_post,Liked_postAdmin)

class Comment_postAdmin(admin.ModelAdmin):
    list_display=['post_id','commenter_email','comment','datetime','post_id']
admin.site.register(Comment_post,Comment_postAdmin)

# Register your models here.
 