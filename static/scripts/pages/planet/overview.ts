function getCookie_2 (name: string): string | null {
    const cookies = document.cookie.split('; ')

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=')
        if (cookieName === name) { return cookieValue }
    }
    return null
}
async function sendPlanetRenameRequest() : Promise<void> {
    const urlParams = new URLSearchParams(window.location.search)
    const planetID = urlParams.get('planet')
    const token = getCookie_2("Authorization")
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token ?? "",
    }

    try {
        const response = await fetch(
            `../api/planet/rename`,
            {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    'planetID': Number(planetID),
                    'name': (<HTMLInputElement>document.getElementById(`new-planet-name-input`)).value ?? 'Colony',
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

function openRenamePlanetMenu() : void {
    const elementToChange =  document.getElementById('screen-overlay')

    if (!elementToChange) { return }
    if (elementToChange.className == '') {
        elementToChange.setAttribute('class', 'screen-overlay')
        elementToChange.innerHTML = `
            <div class="detailed-information-box" style="height: 100px; min-height: 100px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2>Rename Planet</h2>
                    <button onclick="openRenamePlanetMenu()">x</button>
                </div>
                <div>
                    <div style="float:left;width:100%;">
                    <input type="text" id="new-planet-name-input" placeholder="New planet name">
                    <a onclick="sendPlanetRenameRequest()" class="planet-button" style="float: right;">Rename</a>
                </div>
            </div>
        `
    }
    else {
        elementToChange.setAttribute('class', '')
        elementToChange.innerHTML = ''
    }
}