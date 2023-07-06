import axios from "axios";

//Backend (Django) - Frontend (React) api connection using axios;

export const FormApi = ({ url, method, values, actions }) => {
  axios({
    method: method,
    url: url,
    data: values
  })
  .then(function (res) {
    console.log(res)
    alert(`Successfully ${actions}!`);  
  })
  .catch(function (res) {
    console.log(res)
  });
}

//Separate functions for api connection;
/* export const SignUpApi = ({ values }) => {
    axios({
      method: 'POST',
      url: 'http://localhost:8000/api/register',
      data: values
    })
    .then(function (res) {
      console.log(res)
      alert('Successfully signed up!');  
    })
    .catch(function (res) {
      console.log(res)
    });
}

export const LogInApi = ({ values }) => {
    axios({
      method: 'POST',
      url: 'http://localhost:8000/api/login',
      data: values
    })
    .then(function (res) {
      console.log(res)
      alert('Successfully logged in!');  
    })
    .catch(function (res) {
      console.log(res)
    });
} */