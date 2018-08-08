function toggleVoteContainer(){
  //find the vote container on web page
  var voteContainer = document.getElementById("vote-container");
  console.log(voteContainer.style);
  if(voteContainer.style.display === ""){
    voteContainer.style.display = "block";
  }
}

function increaseLikes(element) {
  var likes = element.innerText;
  likes = parseInt(likes);
  likes += 1;
  element.innerText = likes;
  var scores = document.getElementsByClassName("score");
  var score = scores[0];
}

var catImages = ["https://www.petwave.com/-/media/Images/Center/Care-and-Nutrition/Cat/Kittensv2/Kitten-3.ashx?w=450&hash=C2EB74BB478F980E6504B014958FAC4BCE13D136",
"https://i.guim.co.uk/img/media/43352be36da0eb156e8551d775a57fadba8ae6d7/0_0_1440_864/master/1440.jpg?w=300&q=55&auto=format&usm=12&fit=max&s=ed148ff29b9b874a299f8b38e2fb04f3",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtLBdp2WJGSttGi5quikngaFpFhZNcQ3EO0SmXXT0GrRSo2j4JEw"];

var dogImages = ["http://cdn3-www.dogtime.com/assets/uploads/2011/03/puppy-development-460x306.jpg",
"https://static.boredpanda.com/blog/wp-content/uploads/2018/04/Dog-with-heart-mark-on-nose-enchants-where-it-passes-5acf0cf17a554__880.jpg",
"http://dirtypawzpetgrooming.com/wp-content/uploads/2015/01/Uber-Puppies.jpg"];

function changeImage(element){
  var animals = [];
  if (element.id === "cats-carousel"){
    animals = catImages;
  }
  else {
    animals = dogImages;
  }

  var carousel =document.getElementById(element.id);
  var image = carousel.getElementsByTagName('img')[0];
  var imageUrl = image.getAttribute('src');
  var imageIndex = animals.indexOf(imageUrl);
  if (imageIndex === animals.length -1){
    imageIndex = 0;
  }
  else {
    imageIndex += 1;
  }
  imageUrl = animals[imageIndex];
  image.src = imageUrl;

}
