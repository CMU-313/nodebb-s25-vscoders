# UserGuide.md

Our implementation use a custom Harmony Theme, to access full feature, you need to:
```bash
/some/dir$ cd NodeBB
/some/dir/NodeBB$ npm install ./nodebb-theme-harmony
/some/dir/NodeBB$ npm install ./nodebb-plugin-composer-default
```
# Feature documentation

## Endorse tag

We implemented this endorsement tag feature so that when an instructor (admin user) upvotes a post, a visible tag will be displayed under the post.

![Alt text](https://drive.google.com/uc?id=1voISPy8BOMs5vZEtcXF3931LYYeBue11)
## Private Post

- After an user create a topic, it can access the private post functionality by accessing the Topic Tools, as picture shown below:

![Alt text](https://drive.google.com/uc?id=1P9TU32CCjrC_EWaxGHomP0rz84Cafdwo)

- After clicking the Make Private button, the post will be transformed into a private post such that only the creator and admin user are able to view and access the post. To be specific, normal users aren’t able to view/access it in categories, recent Replies, recent Topics, and direct link.
  -Furthermore, a tag named “privatepost” will be added to the topic.
- To undo the private transformation, users only need to click the Make Public button that automatically shows up after clicking the Make Private button. 
- To be specifically noticed, admin users are able to make the topic private or public whether or not they are the creator of the topic.

## Anonymous feature

- The Post Anonymously button will be displayed as an option to students who want their usernames to be anonymous. If the student checks the button, their username will be anonymous to all users. If the checkbox is not selected, their username will be displayed to all students.
  
![Alt text](https://drive.google.com/uc?id=1oI7YR5JE26N0nFP6K7a1AKY35SL3y7EF)

- If the user chooses to hide their real username, the anonymous username will be randomly generated consisting of random characters and numbers
  
![Alt text](https://drive.google.com/uc?id=1AxVkQiSK8Z1FxcxJVTcS6qgjMVbtWidT)

- (INCOMPLETE) Once the user fills out the topic title, content, and checks the post anonymously button, then the randomly generated username will be displayed in real-time. 
