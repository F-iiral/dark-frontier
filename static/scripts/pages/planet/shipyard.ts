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
    descriptionLong: string;
    damageMults: number[];
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
        description: "Fighters are small but cheap craft that can be produced easily to escort larger fleet groups.",
        descriptionLong: "The nimble Fighters, designed as cost-effective assets, are the backbone of any formidable fleet. They serve as the vanguard, swiftly neutralizing threats. However, caution is advised when facing Frigates, as their limited armor makes them susceptible to concentrated fire.",
        damageMults: [0, 1.5, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Interceptors are an evolution of fighters that focuses on speed, making them much faster and more agile.",
        descriptionLong: "The Interceptor, a refined iteration of its predecessor, the Fighter, is meticulously engineered for unparalleled speed and agility on the battlefield. With double the damage output against Bombers, they can easily protect capital ships against their weapons.",
        damageMults: [-1.5, 0, 2, 2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Bombers are designed to carry nukes and other big weapons to destroy capital ships with raw firepower.",
        descriptionLong: "Bombers have the raw firepower necessary to annihilate capital ships with unparalleled efficiency. Armed with the capacity to carry nukes and heavy weapons, it becomes the vengeful force against any large craft that dares to enter the battlefield unprotected.",
        damageMults: [0, -2, 0, 0, -3, 0, 2, 2, 4, 5, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Strategic bombers were designed to carry out long distance bombing runs on other planets.",
        descriptionLong: "Strategic Bombers are designed to execute precision bombing runs across distant planets. With an arsenal tailored for planetary assault, they unleash cataclysmic damage, devastating any static planetary defenses. Unfortunately, they are helpless in space-to-space combat.",
        damageMults: [0, -2, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 10, 5, 5, 3, 2, 5, 5, 5],
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
        description: "Frigates are ideal for interstellar patrol duties and planetary defense forces.",
        descriptionLong: "Frigates are designed to protect planets in smaller planetary defense force fleets but can also be used in larger fleetgroups to destroy any smaller craft like fighters or bombers. This is possible thanks to the extensive point defense and anti-air grid on their hulls.",
        damageMults: [3, 3, 3, 3, 0, -2, -3, 0, 0, 0, 0, 0, 9, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Destroyers form the backbone of any interstellar strike force, as they are fast and can operate as escorts.",
        descriptionLong: "Destroyers, the backbone of interstellar strike forces, combine speed and versatility to operate effectively as escorts. With double damage against Frigates and Battleships, thanks to torpedos, they are able to screen against smaller vessels or use numbers to attack larger craft.",
        damageMults: [0, 0, 0, 0, 2, 0, -2, 0, 0, 2, 0, 0, 12, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Cruisers are large enough to operate independently and cross galactic distances without refueling at all.",
        descriptionLong: "Cruisers were designed for two goals: They needed to be large enough to cross galactic distances and they needed to protect even heavier ships against the rise of destroyers. Their shields were reinforced as well, making them able to withstand fire for extended periods of time.",
        damageMults: [0, 0, -2, 0, 3, 2, 0, 0, -2, -3, 0, -2, 25, 8, 8, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Battlecruisers were designed to outgun everything they cant run from and outrun anything they do not outgun.",
        descriptionLong: "Battlecruisers were an offshoot of the cruiser that was designed to carry bigger guns and still be comperatively fast. They have a combined arsenal of lasers and plasma weapons to achieve the first goal and are also still the same speed as Cruiser though they did have to sacrifice both armor and shield strength.",
        damageMults: [0, 0, -4, 0, 0, 0, 2, 0, 0, 0, 0, -4, 30, 10, 10, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Battleships carry heavy guns, are well armored and have strong shields, making them the flagship of an interstellar strike force.",
        descriptionLong: "Battleships are large capital ships with plasma weapons, heavy armor and strong shields. As such, they are often the flagship of any given fleet. While powerful in their own right, they require an escort fleet as they would rapidly fall to Bombers or larger Destroyer groups without them.",
        damageMults: [0, 0, -5, 0, 0, -2, 3, 0, 0, 0, 0, -3, 30, 10, 10, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Escort Carriers were designed to transport small Fighters that cannot cross interstellar distances themselves.",
        descriptionLong: "Escort Carriers, designed for transporting small Fighters incapable of interstellar travel, excel in low-priority strategic deployment. Unfortunetly, they are not fast enough to keep pace with combat ships, but they are able to keep pace with Large Cargoships, which is how they go their name.",
        damageMults: [0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, -3, 8, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Fleet Carriers are a larger version of the Escort Carries and are fast enough to keep pace with Cruisers.",
        descriptionLong: "Fleet Carriers, an enlarged iteration of Escort Carriers, match the speed of Cruisers while also having enhanced offensive capabilities. While this does not mean that they are designed to engage in the frontline, they are much less likely to fall to a stray bomber that somehow got through its extensive fighter screen.",
        damageMults: [0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, -3, 15, 5, 5, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Titans are gigantic and ludicrously expensive flagships only few can afford. They are a navy's pride.",
        descriptionLong: "Titans, colossal and exorbitantly priced flagships, stand as the epitome of a navy's prestige, reserved for the empire few who can afford them. With awe-inspiring damage against any smaller ships, Titans reign supreme on the galactic battlefield and are naval supremacy made manifest.",
        damageMults: [0, 0, -10, 0, 0, 0, 2, 3, 4, 3, 3, 0, 100, 25, 25, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Satellites can be used for many purposes, ranging from power generation to spying on others.",
        descriptionLong: "Satellites can be used for many purposes, ranging from power generation to spying on others. However, they are EXTREMELY, fragile and will die to just about anything.",
        damageMults: [-2, 0, 0, 0, -9, -12, -25, -8, -30, -30, -15, -100, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Small Cargoships allow trade between different planets and stars in your empire.",
        descriptionLong: "Small Cargoships allow trade between different planets and stars in your empire. They are not capable of crossing between different spiral arms without upgrades and have nearly no armor, resulting in them requiring escorts to keep alive.",
        damageMults: [0, 0, 0, 0, -3, -5, -8, -4, -10, -10, -5, -25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 120,
        shields: 0,
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
        description: "A larger cargo vessel was needed, and so the Large Cargoship was created. It can cross galactic distances.",
        descriptionLong: "A larger cargo vessel was needed, and so the Large Cargoship was created. It has been upgraded to be able to cross between different spiral arms, increased cargo capacity and has also been equipped with some self-defense weapons to reduce the risk of them being destroyed in pirate attacks.",
        damageMults: [0, 0, 0, 0, -3, -5, -8, -4, -10, -10, -5, -25, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 400,
        shields: 20,
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
        description: "Colony ships carry colonists to distant planets to expand your empire across the entire Galaxy.",
        descriptionLong: "Colony ships carry colonists to distant planets to expand your empire across the entire Galaxy.",
        damageMults: [0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Science ships can be used to explore deep space and return valuable resources from it.",
        descriptionLong: "Science ships can be used to explore deep space and return valuable resources from it.",
        damageMults: [0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        description: "Construction ships can aid in resource production and can be used to create megastructures for your alliance.",
        descriptionLong: "Construction ships can aid in resource production and can be used to create megastructures for your alliance.",
        damageMults: [0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
const UnitMultNames = [
    "Fighter", "Interceptor", "Bomber", "Strategic Bomber", 
    "Frigate", "Destroyer", "Cruiser", "Escort Carrier",
    "Battlecruiser", "Battleship", "Fleet Carrier", "Titan",
    "Sattelites", "Small Cargoship", "Large Cargoship", "Colony Ship", "Science Ship", "Construction Ship",
    "AA Guns", "Railgun Turrets", "Rocket Launchers", "Laser Turrets", "Ion Turrets",
    "Plasma Turrets", "Disruptor Turrets", "Small Shield", "Medium Shield", "Planetary Shield"
]

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

    function shipDamageMultPositive(ShipDetails: ShipStatisticsFull): string {
        let positiveDamageMultString = ``
        let j = 0

        for (let i of ShipDetails['damageMults']) {
            if (i > 1) {
                positiveDamageMultString += `<li>Damage against <span style="color:var(--ok-color);">${UnitMultNames[j]}</span>: ${i}x</li>`
            }
            j++
        }
        return positiveDamageMultString
    }
    function shipDamageMultNegative(ShipDetails: ShipStatisticsFull): string {
        let negativeDamageMultString = ``
        let j = 0

        for (let i of ShipDetails['damageMults']) {
            if (i < -1) {
                negativeDamageMultString += `<li>Damage from  <span style="color:var(--error-color);">${UnitMultNames[j]}</span>: ${-i}x</li>`
            }
            j++
        }
        return negativeDamageMultString
    }

    return `
    <div style="margin-top:10px;padding-left:20px;">
        ${shipDamageMultPositive(ShipDetails)}
    </div>
    <div style="margin-top:10px;padding-left:20px;">
        ${shipDamageMultNegative(ShipDetails)}
    </div>
    <div style="margin-top:10px;padding-left:20px;">
        <li>Armor: ${ShipDetails['armor']}</li>
        <li>Shields: ${ShipDetails['shields']}</li>
        <li>Firepower: ${ShipDetails['weapons']}</li>
        <li>Speed: ${ShipDetails['speed']}</li>
        <li>Fuel Usage: ${ShipDetails['fuelUsage']}</li>
        <li>Cargo Space: ${ShipDetails['cargoSpace']}</li>
        <li>Hangar Info: ${ShipDetails['hangarSpace']} | ${ShipDetails['hangarUsage']}</li>
    </div>
    `
}
function showShipDetailedInformation(id: string): void {
    const elementToChange =  document.getElementById('screen-overlay')

    if (!elementToChange) { return }
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
                            <p>${ShipStatisticsRecord[id]['descriptionLong']}</p>
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