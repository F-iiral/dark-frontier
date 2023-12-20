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
enum ShipWeapons {
    CONVENTIONAL    = 1,
    LASER           = 2,
    ION             = 4,
    PLASMA          = 8,
    DISRUPTOR       = 16
}
enum ShipRanges {
    INTERPLANETARY      = 1,
    INTERSTELLAR        = 2,
    INTERSTELLAR_PLUS   = 3,
    GALACTIC            = 4
}
type ShipStatisticsFull = {
    name: string;
    description: string;
    armor: number;
    shields: number;
    weapons: number;
    weaponType: number;
    speed: number;
    range: number;
    fuelUsage: number;
    cargoSpace: number;
    hangarSpace: number;
    hangarUsage: number;
};
const ShipStatisticsRecord: Record<string, ShipStatisticsFull> = {
    ["ship-fighter"]:
    {
        name: "Fighter",
        description: "TO DO",
        armor: 8,
        shields: 0,
        weapons: 1,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 10000,
        range: ShipRanges.INTERPLANETARY,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-interceptor"]:
    {
        name: "Interceptor",
        description: "TO DO",
        armor: 8,
        shields: 0,
        weapons: 1,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 12000,
        range: ShipRanges.INTERPLANETARY,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-tac-bomber"]:
    {
        name: "Bomber",
        description: "TO DO",
        armor: 8,
        shields: 0,
        weapons: 2,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 8000,
        range: ShipRanges.INTERPLANETARY,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-str-bomber"]:
    {
        name: "Strategic Bomber",
        description: "TO DO",
        armor: 40,
        shields: 0,
        weapons: 10,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 8000,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-frigate"]:
    {
        name: "Frigate",
        description: "TO DO",
        armor: 240,
        shields: 0,
        weapons: 30,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 4000,
        range: ShipRanges.INTERSTELLAR,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-destroyer"]:
    {
        name: "Destroyer",
        description: "TO DO",
        armor: 950,
        shields: 20,
        weapons: 120,
        weaponType: ShipWeapons.LASER,
        speed: 4000,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-cruiser"]:
    {
        name: "Cruiser",
        description: "TO DO",
        armor: 3000,
        shields: 300,
        weapons: 420,
        weaponType: ShipWeapons.LASER,
        speed: 3500,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-battlecruiser"]:
    {
        name: "Battlecruiser",
        description: "TO DO",
        armor: 4800,
        shields: 300,
        weapons: 620,
        weaponType: ShipWeapons.LASER & ShipWeapons.PLASMA,
        speed: 3500,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-battleship"]:
    {
        name: "Battleship",
        description: "TO DO",
        armor: 18000,
        shields: 2000,
        weapons: 2500,
        weaponType: ShipWeapons.PLASMA,
        speed: 2500,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-escort-carrier"]:
    {
        name: "Escort Carrier",
        description: "TO DO",
        armor: 300,
        shields: 300,
        weapons: 20,
        weaponType: ShipWeapons.ION,
        speed: 2200,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 400,
        hangarUsage: 0,
    },
    ["ship-fleet-carrier"]:
    {
        name: "Fleet Carrier",
        description: "TO DO",
        armor: 1800,
        shields: 2000,
        weapons: 160,
        weaponType: ShipWeapons.ION,
        speed: 3500,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 2300,
        hangarUsage: 0,
    },
    ["ship-titan"]:
    {
        name: "Titan",
        description: "TO DO",
        armor: 220000,
        shields: 20000,
        weapons: 30000,
        weaponType: ShipWeapons.PLASMA & ShipWeapons.DISRUPTOR,
        speed: 500,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-sattelites"]:
    {
        name: "Sattelites",
        description: "TO DO",
        armor: 1,
        shields: 0,
        weapons: 0,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 100000,
        range: ShipRanges.INTERPLANETARY,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-small-cargo"]:
    {
        name: "Small Cargoship",
        description: "TO DO",
        armor: 120,
        shields: 20,
        weapons: 0,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 2500,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 30000,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-large-cargo"]:
    {
        name: "Large Cargoship",
        description: "TO DO",
        armor: 400,
        shields: 0,
        weapons: 20,
        weaponType: ShipWeapons.ION,
        speed: 2200,
        range: ShipRanges.GALACTIC,
        fuelUsage: 0,
        cargoSpace: 750000,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-colony-ship"]:
    {
        name: "Colony Ship",
        description: "TO DO",
        armor: 120,
        shields: 0,
        weapons: 0,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 500,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 750000,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-science-ship"]:
    {
        name: "Science Ship",
        description: "TO DO",
        armor: 120,
        shields: 0,
        weapons: 0,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 0,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
    ["ship-construction-ship"]:
    {
        name: "Construction Ship",
        description: "TO DO",
        armor: 120,
        shields: 0,
        weapons: 0,
        weaponType: ShipWeapons.CONVENTIONAL,
        speed: 0,
        range: ShipRanges.INTERSTELLAR_PLUS,
        fuelUsage: 0,
        cargoSpace: 0,
        hangarSpace: 0,
        hangarUsage: 0,
    },
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
function getShipStatistics(id: string): string {
    const ShipDetails = ShipStatisticsRecord[id]
    return `
    <div style="margin-top:10px;padding-left:20px;">
        <li>Armor: ${ShipDetails['armor']}</li>
        <li>Shields: ${ShipDetails['shields']}</li>
        <li>Firepower: ${ShipDetails['weapons']}</li>
        <li>Speed speed: ${ShipDetails['speed']}</li>
        <li>Fuel Usage: ${ShipDetails['fuelUsage']}</li>
        <li>Cargo Space: ${ShipDetails['cargoSpace']}</li>
        <li>Hangar Info: ${ShipDetails['hangarSpace']} | ${ShipDetails['hangarUsage']}</li>
    </div>
    `
}
function showShipDetailedInformation(id: string): void {
    const elementToChange =  document.getElementById('screen-overlay')

    if (!elementToChange) {
        return
    }

    if (elementToChange.className == '') {
        elementToChange.setAttribute('class', 'screen-overlay')
        elementToChange.innerHTML = `
            <div class="detailed-information-box">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2>${ShipStatisticsRecord[id]['name']} - Technical Details</h2>
                    <button onclick="showShipDetailedInformation('${id}')">x</button>
                </div>
                <div id="ship-info-modal">
                    <div>
                        <!--image is todo-->
                    </div>
                    <div class="right-col">
                        <div class="info">
                            <p>${ShipStatisticsRecord[id]['description']}</p>
                        </div>
                        ${getShipStatistics(id)}
                    </div>
                </div>
            </div>
        `
    }
    else {
        elementToChange.setAttribute('class', '')
        elementToChange.innerHTML = ''
    }
}