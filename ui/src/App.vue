<template>
  <div style='height:100%'>
    <router-view />
  </div>
</template>


<script>
export default {
}
</script>

<style>

.html{
  height:100%;
}

body {
  font-family: "Public Sans";
  background-color:#f08921;
}

.button-white {
  cursor: pointer;
  float: right;
  padding: 14px 24px;
  background: #ffffff;
  color: #0d1821;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #0d1821;
  box-sizing: border-box;
  border-radius: 40px;
}

.button-white:hover{
  box-shadow: 0px 0px 20px black;
  transition: box-shadow 0.2s ease-in-out;  
}

.button-black:hover{
  box-shadow: 0px 0px 20px black;
  transition: box-shadow 0.2s ease-in-out;  
}

.button-see-more {
  float: none;
  display: inline-block;
  font-weight: bold;
  font-size: 16px;
}

.button-white > .text {
  display: inline-block;
  font-size: 16px;
  vertical-align: middle;
  margin-right: 8px;
}

.button-white > .material-icons {
  display: inline-block;
  font-size: 20px;
  vertical-align: middle;
}

@media only screen and (max-width: 700px) {
  .button-white > .text {
    display: none;
  }
  .button-white {
    padding: 14px 14px;
  }
  .button-black {
    display: none;
  }
}

.button-black {
  cursor: pointer;
  float: right;
  margin-left: 24px;
  /*width: 161px;*/
  /*height: 48px;*/
  padding: 16px 24px;
  background: #0d1821;
  color: #ffffff;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #0d1821;
  box-sizing: border-box;
  border-radius: 40px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}

.button-black > .text {
  display: inline-block;
  font-size: 16px;
  vertical-align: middle;
}

.icon {
  vertical-align: middle;
  float: left;
  /*margin-right: 10%;*/
}

.navbar {
  /*padding-left: 48px;
      padding-right: 48px;
      padding-top: 47px;*/
  display: block;
  position: static;
  /* background: red; */
}

.search-bar {
  background: #656569;
}

/*Eski CSS:*/

a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

a:active {
  text-decoration: none;
}

body {
  padding: 0px;
  margin: 0px;
  font-family: Tahoma, sans-serif;
}

.top-frame {
  padding: 16px;
  background: #f08921;
  padding-bottom: 20px;
  border-bottom: 1px solid black;
}

.home-frame {
  padding: 16px;
  background: #f08921;
  text-align: center;
  
}

.middle-frame {
  padding: 16px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  padding-bottom: 20px;
  padding-left: 18%;
  padding-right: 18%;
}

.answer-frame {
  padding:16px;
  max-width: 664px;
  min-height: 400px;
  margin-left: auto;
  margin-right: auto;
}

.bottom-frame {
  padding:16px;
  background: #656569;
  padding-bottom: 20px;
  padding-left: 5%;
  padding-top: 5.5%;
}

.navbar {
  padding: 47px;
}

.logo {
}

.button {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 14px 24px;
  position: static;
  width: 191px;
  height: 48px;
  left: 0px;
  top: 0px;
  /* Special / White */
  background: #ffffff;
  /* Grey / 500 - #0D1821 */
  border: 2px solid #0d1821;
  box-sizing: border-box;
  border-radius: 40px;
  /* Inside Auto Layout */
  font-family: Tahoma, sans-serif;
  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 24px;
}

.elipse {
  /* position: absolute; */
  width: 64px;
  height: 64px;
  border: 2px solid #dced31;
  /* box-sizing: border-box; */
  border-radius: 50%;
  align-items: center;
  display: flex;
}

.bottom-link {
  color: #dced31;
  font-weight: 600;
  font-size: 19px;
  line-height: 140%;
}

.form {
  /* This bit sets up the horizontal layout */
  display: flex;
  flex-direction: row;
  /* This bit draws the box around it */
  background: #ffffff;
  /* Shadow / 1 */
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
  border-radius: 8px;
  max-width: 664px;
  width: 100%;
  height: 56px;
  /* I've used padding so you can see the edges of the elements. */
  padding: 2px;
  /* padding-left: 16px;
  padding-right: 16px; */
  margin:8px;

}

.form:hover{
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

.form:focus-within{
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

input{
  padding-left:16px;
  padding-left:16px;
}

input,
input:placeholder-shown {
  /* Special / White */
  /* Tell the input to use all the available space */
  flex-grow: 2;
  /* And hide the input's outline, so the form looks like the outline */
  border: none;
  font-size: 16px;
  line-height: 140%;
  /* or 22px */
  letter-spacing: -0.2px;
}

input:focus {
  outline: none !important;

}

button {
  /* Just a little styling to make it pretty */
  /* border:1px solid blue; */
  background: #ffffff;
  /* color:white; */
  border: none;
  cursor: pointer;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
  text-align: center;
  align-items: center;
  margin-top: 50px;
}

div.loading {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(16, 16, 16, 0.5);
}

@-webkit-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-webkit-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-ms-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-webkit-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-o-keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes uil-ring-anim {
  0% {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
.uil-ring-css {
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 200px;
  height: 200px;
}
.uil-ring-css > div {
  position: absolute;
  display: block;
  width: 160px;
  height: 160px;
  top: 20px;
  left: 20px;
  border-radius: 80px;
  box-shadow: 0 6px 0 0 #ffffff;
  -ms-animation: uil-ring-anim 1s linear infinite;
  -moz-animation: uil-ring-anim 1s linear infinite;
  -webkit-animation: uil-ring-anim 1s linear infinite;
  -o-animation: uil-ring-anim 1s linear infinite;
  animation: uil-ring-anim 1s linear infinite;
}

.container-row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
