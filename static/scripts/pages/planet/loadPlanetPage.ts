function getCookie (name: string): string | null {
    const cookies = document.cookie.split('; ');

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) { return cookieValue; }
    }
    return null;
};

async function loadPlanetPage (planetID: number, page_name: string): Promise<void> {
    const token = getCookie("Authorization");
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token ?? "",
    };

    try {
        const response = await fetch(
            `../api/planet?planet=${planetID}`,
            {
                method: 'GET',
                headers: headers,
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const jsonResponse = await response.json();
        document.getElementById("metal-amount")!.innerHTML = jsonResponse["metal_amount"];
        document.getElementById("crystal-amount")!.innerHTML = jsonResponse["crystal_amount"];
        document.getElementById("gas-amount")!.innerHTML = jsonResponse["gas_amount"];
        document.getElementById("overview-button")!.setAttribute('href', `overview?planet=${planetID}`)
        document.getElementById("buildings-button")!.setAttribute('href', `buildings?planet=${planetID}`)
        document.getElementById("defense-button")!.setAttribute('href', `defense?planet=${planetID}`)
        document.getElementById("shipyard-button")!.setAttribute('href', `shipyard?planet=${planetID}`)
        document.getElementById("fleet-button")!.setAttribute('href', `fleet?planet=${planetID}`)

        if (page_name === "overview") {
            document.getElementById("planet-name")!.innerHTML   = jsonResponse["name"]
            document.getElementById("planet-coords")!.innerHTML = `[${jsonResponse['position']}]`
            document.getElementById("planet-radius")!.innerHTML = `${jsonResponse['radius']} km`
            document.getElementById("planet-temperature")!.innerHTML = `${jsonResponse['temperature']} C°`
        }
    } 
    catch (error) {
        console.error("Error:", error);
    }
}