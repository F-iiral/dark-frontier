function getCookie_2 (name: string): string | null {
    const cookies = document.cookie.split('; ')

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=')
        if (cookieName === name) { return cookieValue }
    }
    return null
}

function sendPlanetShipyardRequest() : never {
    throw new Error("not implemented")
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