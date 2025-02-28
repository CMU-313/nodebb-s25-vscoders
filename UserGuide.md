UserGuide.md

Our implementation use a custom Harmony Theme, to access full feature, you need to:
/some/dir$ cd NodeBB
/some/dir/NodeBB$ npm install ./nodebb-theme-harmony
/some/dir/NodeBB$ npm install ./nodebb-plugin-composer-default
Feature documentation
Endorse tag
We implemented this endorsement tag feature so that when an instructor (admin user) upvotes a post, all students would know that the post has accurate information.

Private Post
After an user create a topic, it can access the private post functionality by accessing the Topic Tools, as picture shown below:

After clicking the Make Private button, the post will be transformed into a private post such that only the creator and admin user are able to view and access the post. To be specific, normal users aren’t able to view/access it in categories, recent Replies, recent Topics, and direct link.
Furthermore, a tag named “privatepost” will be added to the topic.
To undo the private transformation, users only need to click the Make Public button that automatically shows up after clicking the Make Private button. 
To be specifically noticed, admin users are able to make the topic private or public whether or not they are the creator of the topic.

Anonymous feature
The Post Anonymously button will be displayed as an option to students who want their usernames to be anonymous. If the student checks the button, their username will be anonymous to all users. If the checkbox is not selected, their username will be displayed to all students. 

If the user chooses to hide their real username, the anonymous username will be randomly generated consisting of random characters and numbers

(INCOMPLETE) Once the user fills out the topic title, content, and checks the post anonymously button, then the randomly generated username will be displayed in real-time. 

To access guide with picture, here is the link: https://docs.google.com/document/d/1_iC1MWRpt3Nclsy9cZAPID4-sk3d_MjEwMk6y60HUaA/edit?usp=sharing