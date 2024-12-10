async function getdata(){
    const playerName = document.getElementById("clubInput").value;
    let URL = `https://apiv3.apifootball.com/?action=get_players&player_name=${playerName}&APIkey=abe2bcbf372fbf7af5b60c85482f9a9cf9fa7b5aef51acab3109aca033884570`
    try {
        const response = await fetch(URL);
        const data = await response.json();
        console.log(data);
        const [{player_image, player_name}] = data;
        document.getElementById("playerName").textContent = player_name;
        const imageElement = document.getElementById("playerImage");
        if(player_image){
            imageElement.src = player_image;
            imageElement.style.display = "block";
        }
        else{
            console.log("Image not found for player.");
        }
    }
    catch(error){
        console.log(error);
    }
}

getdata();
