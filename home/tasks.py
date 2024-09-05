# app/tasks.py
from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Posts  # Import your Post model

@shared_task
def create_post_task(posted_data, user_id, uploaded_image_urls):
    User = get_user_model()
    user = User.objects.get(id=user_id)

    # Create the post with uploaded images
    post = Posts.objects.create(
        title=posted_data['title'],
        description=posted_data['desc'],
        privacy=posted_data['privacy'],
        created_by=user
    )

    # Add tags to the post
    for tag in posted_data['tags']:
        post.tags.add(tag)

    # Add images to the post
    for image_url in uploaded_image_urls:
        post.images.create(url=image_url)

    post.save()
