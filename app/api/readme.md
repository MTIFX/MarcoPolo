<H1> Usage </H1>


<H3> Create Heroku App </H3>
<li> Click on deploy Heroku app link from Falcon API folder </li>

<H3> Linking Heroku App into code </H3>
<li> Replace with Heroku app url: ENTRY_POINT = 'eve-demo.herokuapp.com' </li>

<H3> Perform request </H3>

<li> curl -XGET https://marco-polo1.herokuapp.com/v1/users/self/login -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'

</li>

