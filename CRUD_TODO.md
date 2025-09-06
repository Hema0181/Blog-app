# Blog App CRUD Operations Implementation

## Current Status
- ✅ Create Post: Implemented (create_post view)
- ✅ Read Posts: Implemented (home, post_detail, profile views)
- ✅ Update Profile: Implemented (edit_profile view)
- ❌ Update Post: Missing
- ❌ Delete Post: Missing

## Implementation Plan

### 1. Update Post (Edit Post)
- [ ] Add edit_post view in views.py
- [ ] Add edit_post URL pattern
- [ ] Create edit_post.html template
- [ ] Add edit button to post_detail.html
- [ ] Add edit button to profile.html for user's posts

### 2. Delete Post
- [ ] Add delete_post view in views.py
- [ ] Add delete_post URL pattern
- [ ] Add delete confirmation template
- [ ] Add delete button to post_detail.html (for post author only)
- [ ] Add delete button to profile.html for user's posts

### 3. Authorization & Security
- [ ] Ensure only post author can edit/delete their posts
- [ ] Add proper error handling for unauthorized access

### 4. Navigation Enhancements
- [ ] Add back buttons to edit/delete forms
- [ ] Update navigation links in templates
