enum Buildings {
    METAL_MINE      = 1,
    CRYSTAL_MINE    = 2,
    GAS_MINE        = 3,
    METAL_STORAGE   = 4,
    CRYSTAL_STORAGE = 5,
    GAS_STORAGE     = 6,
    FACTORY         = 7,
    SHIPYARD        = 8,
    LABORATORY      = 9,
    TERRAFORMER     = 10
}

function getCookie_0 (name: string): string | null {
    const cookies = document.cookie.split('; ')

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=')
        if (cookieName === name) { return cookieValue }
    }
    return null
}

async function sendPlanetBuildingRequest(id: string): Promise<void> {
    const urlParams = new URLSearchParams(window.location.search)
    const planetID = urlParams.get('planet')
    const token = getCookie_0("Authorization");
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token ?? "",
    };

    let buildingType = 0 
    if (id == 'bld-metal-mine') { buildingType = Buildings.METAL_MINE }
    else if (id == 'bld-crystal-mine') { buildingType = Buildings.CRYSTAL_MINE }
    else if (id == 'bld-gas-mine') { buildingType = Buildings.GAS_MINE }
    else if (id == 'bld-factory') { buildingType = Buildings.FACTORY }
    else if (id == 'bld-shipyard') { buildingType = Buildings.SHIPYARD }
    else if (id == 'bld-metal-storage') { buildingType = Buildings.METAL_STORAGE }
    else if (id == 'bld-crystal-storage') { buildingType = Buildings.CRYSTAL_STORAGE }
    else if (id == 'bld-gas-storage') { buildingType = Buildings.GAS_STORAGE }
    else if (id == 'bld-laboratory') { buildingType = Buildings.LABORATORY }
    else if (id == 'bld-terraformer') { buildingType = Buildings.TERRAFORMER }

    try {
        const response = await fetch(
            `../api/planet/building`,
            {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    'planetID': Number(planetID),
                    'building': buildingType,
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

function showBuildingInformation(id: string): void {
    const buildings = [ 'metal-mine', 'crystal-mine', 'gas-mine', 'factory', 'shipyard', 'metal-storage', 'crystal-storage', 'gas-storage', 'laboratory', 'terraformer']
    const elementToChange = document.getElementById(`${id}-information-box`)
    const hideAllBuildings = () => {
        buildings.forEach(building => {
            const buildingElement = document.getElementById(`bld-${building}-information-box`)
            if (buildingElement) {
                buildingElement.style.top = '400px'
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