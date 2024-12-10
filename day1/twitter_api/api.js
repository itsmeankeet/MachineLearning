async function getData() {
    const clubName = document.getElementById('clubInput').value; // Get the club name from the input field
    if (!clubName) {
        alert("Please enter a club name.");
        return;
    }

    const URL = `https://v3.football.api-sports.io/teams?name=${clubName}`;
    const API_KEY = "08493462347796e30de7e31ac847a9f6";
    
    try {
        const response = await fetch(URL, {
            method: "GET",
            headers: {
                'x-apisports-key': API_KEY,
                'Accept': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data);

        if (data.response.length === 0) {
            alert("No club found with that name.");
            return;
        }

        // Get the first team result
        const team = data.response[0].team;
        const venue = data.response[0].venue;

        // Set the club logo
        const imageElement = document.getElementById('clubLogo');
        imageElement.src = team.logo;
        imageElement.style.display = 'block'; // Make the logo visible

        // Set the club details
        document.getElementById('name').textContent = team.name ? team.name : 'N/A'	;
        document.getElementById('homeGround').textContent = venue.name ? venue.name : 'N/A';
        document.getElementById('captain').textContent = team.country ? team.country : 'N/A';
        document.getElementById('coach').textContent = venue.city ? venue.city : 'N/A';

        // Display the club details section
        document.getElementById('clubDetails').style.display = 'block';

    } catch (error) {
        console.error('Fetch error: ', error);
        alert('Error fetching club data.');
    }
}
