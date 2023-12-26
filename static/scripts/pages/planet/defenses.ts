enum Defenses {
    AA_GUN          = 1,
    ROCKET          = 2,
    RAILGUN         = 3,
    LASER           = 4,
    ION             = 5,
    PLASMA          = 6,
    DISRUPTOR       = 7,
    SHIELD_S        = 8,
    SHIELD_M        = 9,
    SHIELD_L        = 10
}
enum DefenseWeapons {
    CONVENTIONAL    = 1,
    LASER           = 2,
    ION             = 4,
    PLASMA          = 8,
    DISRUPTOR       = 16
}
type DefenseStatisticsFull = {
    name: string
    description: string
    descriptionLong: string
    damageMults: number[]
    armor: number
    shields: number
    weapons: number
    weaponType: number
}
const DefenseStatisticsRecord: Record<string, DefenseStatisticsFull> = {
    ["def-aa"]:
    {
        name: "AA Guns",
        description: "AA Guns are small and not very strong, but they are very cheap and can be constructed en masse.",
        descriptionLong: "AA Guns are small and not very strong, but they are very cheap and can be constructed en masse.",
        damageMults: [5, 5, 5, -20, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 8,
        shields: 0,
        weapons: 1,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
    ["def-railgun"]:
    {
        name: "Railgun Turrets",
        description: "Railgun turrets use electromagnets to launch hypersonic slugs at the enemy.",
        descriptionLong: "Railgun turrets use electromagnets to launch hypersonic slugs at the enemy.",
        damageMults: [0, 0, 0, -10, 3, 2, 2, 2, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 40,
        shields: 0,
        weapons: 10,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
    ["def-rocket"]:
    {
        name: "Rocket Launchers",
        description: "Rocket Launchers are able to launch surface-to-orbit missiles tipped with nukes at enemy capital ships.",
        descriptionLong: "Rocket Launchers are able to launch surface-to-orbit missiles tipped with nukes at enemy capital ships.",
        damageMults: [0, 0, 0, -10, 0, 0, 0, 0, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 40,
        shields: 0,
        weapons: 10,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
    ["def-laser"]:
    {
        name: "Laser Turrets",
        description: "Laser turrets are ideal to use against small- or midsized ships due to their comparatively low cost and high output.",
        descriptionLong: "Laser turrets are ideal to use against small- or midsized ships due to their comparatively low cost and high output.",
        damageMults: [5, 5, 5, -5, 20, 20, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 950,
        shields: 0,
        weapons: 120,
        weaponType: DefenseWeapons.LASER,
    },
    ["def-ion"]:
    {
        name: "Ion Turrets",
        description: "Ion turrets have the same raw power as lasers, but sacrifice armor for shield strength.",
        descriptionLong: "Ion turrets have the same raw power as lasers, but sacrifice armor for shield strength.",
        damageMults: [5, 5, 5, -5, 20, 20, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 950,
        shields: 1520,
        weapons: 120,
        weaponType: DefenseWeapons.ION,
    },
    ["def-plasma"]:
    {
        name: "Plasma Turrets",
        description: "Plasma turrets launch large plasma bolts against medium and large ships to melt their armor away.",
        descriptionLong: "Plasma turrets launch large plasma bolts against medium and large ships to melt their armor away.",
        damageMults: [0, 0, 0, -3, 15, 15, 20, 20, 25, 20, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 2000,
        shields: 100,
        weapons: 220,
        weaponType: DefenseWeapons.PLASMA,
    },
    ["def-disruptor"]:
    {
        name: "Disruptor Turrets",
        description: "Disruptor turrets can be used to rapidly disassemble even large capital ships in orbit.",
        descriptionLong: "Disruptor turrets can be used to rapidly disassemble even large capital ships in orbit.",
        damageMults: [0, 0, 0, -3, 5, 5, 15, 15, 20, 30, 30, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 2500,
        shields: 150,
        weapons: 280,
        weaponType: DefenseWeapons.DISRUPTOR,
    },
    ["def-s-shield"]:
    {
        name: "Small Shield",
        description: "A small shield generator that can protect the area surrounding it from the enemy. Only one can be built.",
        descriptionLong: "A small shield generator that can protect the area surrounding it from the enemy. Only one can be built.",
        damageMults: [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 150,
        shields: 1500,
        weapons: 0,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
    ["def-m-shield"]:
    {
        name: "Large Shield",
        description: "A large shield generator that can protect large regions from the enemy. Only one can be built.",
        descriptionLong: "A large shield generator that can protect large regions from the enemy. Only one can be built.",
        damageMults: [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 3150,
        shields: 31500,
        weapons: 0,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
    ["def-l-shield"]:
    {
        name: "Planetary Shield",
        description: "A gigantic shield generator that can protect the entire planet from the enemy. Only one can be built.",
        descriptionLong: "A gigantic shield generator that can protect the entire planet from the enemy. Only one can be built.",
        damageMults: [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor: 12500,
        shields: 125000,
        weapons: 0,
        weaponType: DefenseWeapons.CONVENTIONAL,
    },
}
const DefenseUnitMultNames = [
    "Fighter", "Interceptor", "Bomber", "Strategic Bomber", 
    "Frigate", "Destroyer", "Cruiser", "Escort Carrier",
    "Battlecruiser", "Battleship", "Fleet Carrier", "Titan",
    "Sattelites", "Small Cargoship", "Large Cargoship", "Colony Ship", "Science Ship", "Construction Ship",
    "AA Guns", "Railgun Turrets", "Rocket Launchers", "Laser Turrets", "Ion Turrets",
    "Plasma Turrets", "Disruptor Turrets", "Small Shield", "Medium Shield", "Planetary Shield"
]

function getCookie_1 (name: string): string | null {
    const cookies = document.cookie.split('; ')

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=')
        if (cookieName === name) { return cookieValue }
    }
    return null
}
async function sendPlanetDefenseRequest(id: string): Promise<void> {
    const urlParams = new URLSearchParams(window.location.search)
    const planetID = urlParams.get('planet')
    const token = getCookie_1("Authorization")
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token ?? "",
    }

    let defenseType = 0 
    if (id == 'def-aa') { defenseType = Defenses.AA_GUN }
    else if (id == 'def-railgun') { defenseType = Defenses.RAILGUN }
    else if (id == 'def-rocket') { defenseType = Defenses.ROCKET }
    else if (id == 'def-laser') { defenseType = Defenses.LASER }
    else if (id == 'def-ion') { defenseType = Defenses.ION }
    else if (id == 'def-plasma') { defenseType = Defenses.PLASMA }
    else if (id == 'def-disruptor') { defenseType = Defenses.DISRUPTOR }
    else if (id == 'def-s-shield') { defenseType = Defenses.SHIELD_S }
    else if (id == 'def-m-shield') { defenseType = Defenses.SHIELD_M }
    else if (id == 'def-l-shield') { defenseType = Defenses.SHIELD_L }

    try {
        const response = await fetch(
            `../api/planet/defenses`,
            {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    'planetID': Number(planetID),
                    'defense': defenseType,
                    'amount': Number((<HTMLInputElement>document.getElementById(`${id}-input-amount`)).value) ?? 0,
                }),
            }
        )

        if (!response.ok) {
            console.log(response)
            document.getElementById("planet-news-dislay")!.innerHTML = `${response.status} - ${response.statusText}`
        }
        location.reload()
    }
    catch (error) {
        console.error("Error:", error)
    }
}

function showDefenseInformation(id: string): void {
    const defenses = [ 'aa', 'railgun', 'rocket', 'laser', 'ion', 'plasma', 'disruptor', 's-shield', 'm-shield', 'l-shield']
    const elementToChange = document.getElementById(`${id}-information-box`)
    const hideAllBuildings = () => {
        defenses.forEach(defense => {
            const defenseElement = document.getElementById(`def-${defense}-information-box`)
            if (defenseElement) {
                defenseElement.style.top = '400px'
            }
        })
    }

    if (elementToChange && elementToChange.style.top === '141px') {
        hideAllBuildings()
    } else {
        hideAllBuildings()
        setTimeout(() => {
            if (elementToChange) {
                elementToChange.style.top = '141px'
            }
        }, 150)
    }
}
function getDefenseStatistics(id: string): string {
    const DefenseDetails = DefenseStatisticsRecord[id]

    function shipDamageMultPositive(DefenseDetails: DefenseStatisticsFull): string {
        let positiveDamageMultString = ``
        let j = 0

        for (let i of DefenseDetails.damageMults) {
            if (i > 1) {
                positiveDamageMultString += `<li>Damage against <span style="color:var(--ok-color);">${DefenseUnitMultNames[j]}</span>: ${i}x</li>`
            }
            j++
        }
        return positiveDamageMultString
    }
    function shipDamageMultNegative(DefenseDetails: DefenseStatisticsFull): string {
        let negativeDamageMultString = ``
        let j = 0

        for (let i of DefenseDetails.damageMults) {
            if (i < -1) {
                negativeDamageMultString += `<li>Damage from  <span style="color:var(--error-color);">${DefenseUnitMultNames[j]}</span>: ${-i}x</li>`
            }
            j++
        }
        return negativeDamageMultString
    }
    function getWeaponName(DefenseDetails: DefenseStatisticsFull): string {
        let weaponName = ''
        if ((DefenseDetails.weaponType & DefenseWeapons.CONVENTIONAL) == DefenseWeapons.CONVENTIONAL) { weaponName += 'Conventional\n' }
        if ((DefenseDetails.weaponType & DefenseWeapons.LASER) == DefenseWeapons.LASER) { weaponName += 'Laser\n' }
        if ((DefenseDetails.weaponType & DefenseWeapons.ION) == DefenseWeapons.ION) { weaponName += 'Ion\n' }
        if ((DefenseDetails.weaponType & DefenseWeapons.PLASMA) == DefenseWeapons.PLASMA) { weaponName += 'Plasma\n' }
        if ((DefenseDetails.weaponType & DefenseWeapons.DISRUPTOR) == DefenseWeapons.DISRUPTOR) { weaponName += 'Disruptor\n' }
        return weaponName.trim()
    }

    return `
    <div style="margin-top:10px;padding-left:20px;">
        ${shipDamageMultPositive(DefenseDetails)}
    </div>
    <div style="margin-top:10px;padding-left:20px;">
        ${shipDamageMultNegative(DefenseDetails)}
    </div>
    <div style="margin-top:10px;padding-left:20px;">
        <li>Armor: ${DefenseDetails.armor}</li>
        <li>Shields: ${DefenseDetails.shields}</li>
        <li>
            <span style="border-bottom: 1px dotted var(--text-color);">
                Firepower: ${DefenseDetails.weapons}
                <div class="tooltip" style="position: absolute; height: 20px; width: 92px; left: 40px;">
                    <div class="tooltiptext" style="position: absolute; white-space: pre-line;">Weapons: ${getWeaponName(DefenseDetails)}</div>
                </div>
            </span>
        </li>
    </div>
    `
}
function showDefenseDetailedInformation(id: string): void {
    const elementToChange =  document.getElementById('screen-overlay')

    if (!elementToChange) { return }
    if (elementToChange.className == '' && id != '') {
        elementToChange.setAttribute('class', 'screen-overlay')
        elementToChange.innerHTML = `
            <div class="detailed-information-box">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2>${DefenseStatisticsRecord[id].name} - Technical Details</h2>
                    <button onclick="showShipDetailedInformation('${id}')">x</button>
                </div>
                <div>
                    <div>
                        <!--image is todo-->
                    </div>
                    <div>
                        <div>
                            <p>${DefenseStatisticsRecord[id].descriptionLong}</p>
                        </div>
                        ${getDefenseStatistics(id)}
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