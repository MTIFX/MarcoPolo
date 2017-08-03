<H1> Documentation </H1>

<H3> Basics </H3> 

<li> Create the Heroku App: Heroku app runs in the cloud, providing the REST API, and the PostgreSQL database, stored on Amazon EC2. </li>
<li> Click on deploy Heroku app link from Falcon API folder </li>

<li> To use live, Heroku config needs to be specified to live, and the config.ini file needs the PostgreSQL database specified. </li> 

<li> After the Heroku app is deployed to the cloud </li>

<H3> Link Heroku app </H3>
<li> Replace with Heroku app url: ENTRY_POINT = 'eve-demo.herokuapp.com' </li>

<H3> Perform request </H3>
<li> curl -XGET https://marco-polo1.herokuapp.com/v1/users/self/login -H "Content-Type: application/json" -d '{ "email": "test1@gmail.com", "password": "test1234" }' </li>
