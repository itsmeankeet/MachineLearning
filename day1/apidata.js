// fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
// .then(response => response.json())
// .then(data => console.log(data.name))
//  .catch(error =>
//     console.log(error)
// );


async function getdata(){
    try{
        const pokemanName = document.getElementById("pokemonName").value.toLowerCase();
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemanName}`);
        if(!response.ok){
            throw new Error("Network response was not ok");
        }
        const data = await response.json();
        console.log(data);

        const image = data.sprites.back_female;

        const imageElement = document.getElementById("pokemanSprite");
        imageElement.src = image;
        imageElement.style.display = "block";
    }
    catch(error){
        console.log(error);
    }
}