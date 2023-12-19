enum Ships {
    FIGHTERS           = 0,
    INTERCEPTORS       = 1,
    TAC_BOMBERS        = 2,
    STR_BOMBERS        = 3,
    FRIGATES           = 4,
    DESTROYERS         = 5,
    CRUISERS           = 6,
    BATTLECRUISERS     = 7,
    BATTLESHIPS        = 8,
    ESCORT_CARRIERS    = 9,
    FLEET_CARRIERS     = 10,
    TITANS             = 11,
    SATTELITES         = 12,
    SMALL_CARGO_SHIPS  = 13,
    BIG_CARGO_SHIPS    = 14,
    COLONY_SHIPS       = 15,
    SCIENCE_SHIPS      = 16,
    CONSTRUCTION_SHIPS = 17,
}

function getCookie_2 (name: string): string | null {
    const cookies = document.cookie.split('; ')

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=')
        if (cookieName === name) { return cookieValue }
    }
    return null
}

async function sendPlanetShipyardRequest(id: string) : Promise<void> {
    const urlParams = new URLSearchParams(window.location.search)
    const planetID = urlParams.get('planet')
    const token = getCookie_2("Authorization");
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token ?? "",
    };

    let shipType = 0 
    if (id == 'ship-fighter') { shipType = Ships.FIGHTERS }
    else if (id == 'ship-interceptor') { shipType = Ships.INTERCEPTORS }
    else if (id == 'ship-tac-bomber') { shipType = Ships.TAC_BOMBERS }
    else if (id == 'ship-str-bomber') { shipType = Ships.STR_BOMBERS }
    else if (id == 'ship-frigate') { shipType = Ships.FRIGATES }
    else if (id == 'ship-destroyer') { shipType = Ships.DESTROYERS }
    else if (id == 'ship-cruiser') { shipType = Ships.CRUISERS }
    else if (id == 'ship-battlecruiser') { shipType = Ships.BATTLECRUISERS }
    else if (id == 'ship-battleship') { shipType = Ships.BATTLESHIPS }
    else if (id == 'ship-escort-carrier') { shipType = Ships.ESCORT_CARRIERS }
    else if (id == 'ship-fleet-carrier') { shipType = Ships.FLEET_CARRIERS }
    else if (id == 'ship-titan') { shipType = Ships.TITANS }
    else if (id == 'ship-sattelites') { shipType = Ships.SATTELITES }
    else if (id == 'ship-small-cargo') { shipType = Ships.SMALL_CARGO_SHIPS }
    else if (id == 'ship-large-cargo') { shipType = Ships.BIG_CARGO_SHIPS }
    else if (id == 'ship-colony-ship') { shipType = Ships.COLONY_SHIPS }
    else if (id == 'ship-science-ship') { shipType = Ships.SCIENCE_SHIPS }
    else if (id == 'ship-construction-ship') { shipType = Ships.CONSTRUCTION_SHIPS }

    try {
        const response = await fetch(
            `../api/planet/shipyard`,
            {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    'planetID': Number(planetID),
                    'ship': shipType,
                    'amount': Number((<HTMLInputElement>document.getElementById(`${id}-input-amount`)).value) ?? 0,
                }),
            }
        );

        if (!response.ok) {
            console.log(response)
            document.getElementById("planet-news-dislay")!.innerHTML = `${response.status} - ${response.statusText}`
        }
        location.reload()
    }
    catch (error) {
        console.error("Error:", error);
    }
}

function showShipInformation(id: string): void {
    const ships = [ 'fighter', 'interceptor', 'tac-bomber', 'str-bomber', 'frigate', 'destroyer', 'cruiser', 'escort-carrier', 'battlecruiser', 'battleship', 'fleet-carrier', 'titan', 'small-cargo', 'large-cargo', 'sattelites', 'colony-ship', 'science-ship', 'construction-ship']
    const elementToChange = document.getElementById(`${id}-information-box`)
    const hideAllShips = () => {
        ships.forEach(ship => {
            const buildingElement = document.getElementById(`ship-${ship}-information-box`)
            if (buildingElement) {
                buildingElement.style.top = '400px'
            }
        })
    }

    if (elementToChange && elementToChange.style.top === '141px') {
        hideAllShips()
    } else {
        hideAllShips()
        setTimeout(() => {
            if (elementToChange) {
                elementToChange.style.top = '141px'
            }
        }, 150)
    }
}