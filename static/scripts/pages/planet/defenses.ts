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