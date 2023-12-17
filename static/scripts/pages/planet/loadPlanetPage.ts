function getCookie (name: string): string | null {
    const cookies = document.cookie.split('; ');

    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) { return cookieValue; }
    }
    return null;
};

function getResourceColor(value: number, max_value: number): string {
    if (value >= max_value * 0.99) {
        return "var(--error-color)"
    }
    else if (value >= max_value * 0.9) {
        return "var(--warn-color)"
    }
    return "var(--text-color)"
}

function generateBuildingInformationBox(jsonResponse: any, id: string, imgSrc: string, name: string, description: string): string {
    const buildingMapping: Record<string, [number[], number]> = {
        ['bld-metal-mine']: [[0, 1, 1], 480],
        ['bld-crystal-mine']: [[1, 0, 1], 480],
        ['bld-gas-mine']: [[1, 1, 0], 480],
        ['bld-factory']: [[0, 1, 1], 240],
        ['bld-shipyard']: [[1, 0, 1], 240],
        ['bld-metal-storage']: [[1, 1, 0], 240],
        ['bld-crystal-storage']: [[1, 1, 0.5], 720],
        ['bld-gas-storage']: [[1, 0.5, 1], 480],
        ['bld-laboratory']: [[0.5, 1, 1], 480],
        ['bld-terraformer']: [[1, 1, 1], 720],
    };
    const buildingInfo = buildingMapping[id]

    let metalCost = 0
    let crystalCost = 0
    let gasCost = 0
    if (buildingInfo) {
        const [buildingResources, buildingCostMult] = buildingInfo
        const buildingCost = Math.round(buildingCostMult * Math.pow(1.4142135, jsonResponse[`${id.replace(/-/g, '_')}`]) / (jsonResponse.bld_factory + 1))
        metalCost = buildingCost * buildingResources[0]
        crystalCost = buildingCost * buildingResources[1]
        gasCost = buildingCost * buildingResources[2]
    }

    // To Do: Make this display if one can afford it or not
    return `<div id="${id}-information-box" class="planet-information-box">
    <div style="display: flex;">
            <div style="margin: 10px;">
                <img src="${imgSrc}">
                <p style="font-weight: bold;">${name}</p>
            </div>
            <div>
                <p>${description}</p>
                <hr />
                <div style="display: flex;">
                    <div>
                        <p style="font-size: 12px;">${metalCost.toLocaleString()} Metal</p>
                        <p style="font-size: 12px;">${crystalCost.toLocaleString()} Gas</p>
                        <p style="font-size: 12px;">${gasCost.toLocaleString()} Crystals</p>
                        <div style="display: block;">
                            <i class="material-icons" style="font-size:12px; color: var(--text-color); cursor: pointer; margin-top: 10px; position: absolute;">info</i>
                            <p style="font-size: 12px; position:absolute; left: 164px; bottom: -8px;">Technical Details</p>
                        </div>
                    </div>
                    <div class="upgrade-btn-container">
                        <a class="planet-button" id="${id}-upgrade-button" onclick="sendPlanetBuildingRequest('${id}')">Upgrade</a>
                    </div>                 
                </div>
            </div>
        </div>
    </div>`
}
function generateDefenseInformationBox(jsonResponse: any, id: string, imgSrc: string, name: string, description: string): string {
    const defenseMapping: Record<string, [number[], number]> = {
        ['def-aa']: [[1, 0, 0], 6000],
        ['def-railgun']: [[1, 0.1, 0], 30000],
        ['def-rocket']: [[1, 0.5, 0.5], 30000],
        ['def-laser']: [[0.5, 1, 0.5], 750000],
        ['def-ion']: [[0.4, 1, 0.5], 1200000],
        ['def-plasma']: [[0.3, 1, 0.5], 1650000],
        ['def-disruptor']:[[0.2, 1, 0.5], 2100000],
        ['def-s-shield']: [[0.2, 1, 0.5], 180000],
        ['def-m-shield']: [[0.2, 1, 0.5], 3800000],
        ['def-l-shield']:[[0.2, 1, 0.5], 15000000],
    };
    const defenseInfo = defenseMapping[id]

    let metalCost = 0
    let crystalCost = 0
    let gasCost = 0
    let amount = 1
    if (defenseInfo) {
        const [buildingResources, buildingCostMult] = defenseInfo
        const buildingCost = Math.round(buildingCostMult * amount / (jsonResponse.bld_factory + 1))
        metalCost = buildingCost * buildingResources[0]
        crystalCost = buildingCost * buildingResources[1]
        gasCost = buildingCost * buildingResources[2]
    }

    // To Do: Make this display the total cost, not the one per unit
    // To Do: Make this display if one can afford it or not
    return `<div id="${id}-information-box" class="planet-information-box">
    <div style="display: flex;">
            <div style="margin: 10px;">
                <img src="${imgSrc}">
                <p style="font-weight: bold;">${name}</p>
            </div>
            <div>
                <p>${description}</p>
                <hr />
                <div style="display: flex;">
                    <div>
                        <p style="font-size: 12px;">${metalCost.toLocaleString()} Metal per Unit</p>
                        <p style="font-size: 12px;">${crystalCost.toLocaleString()} Gas per Unit</p>
                        <p style="font-size: 12px;">${gasCost.toLocaleString()} Crystals per Unit</p>
                        <div style="display: block;">
                            <i class="material-icons" style="font-size:12px; color: var(--text-color); cursor: pointer; margin-top: 10px; position: absolute;">info</i>
                            <p style="font-size: 12px; position:absolute; left: 164px; bottom: -8px;">Technical Details</p>
                        </div>
                    </div>
                    <div class="upgrade-btn-container">
                        <div class="upgrade-input-container">
                            <input id="${id}-input-amount" type="number" value="0">
                            <span class="upgrade-input-desc">Amount</span>
                        </div>
                        <br>
                        <a class="planet-button" id="${id}-upgrade-button" onclick="sendPlanetDefenseRequest('${id}')">Upgrade</a>
                    </div>                 
                </div>
            </div>
        </div>
    </div>`
}

function generateBuildingHTML(id: string, tooltip: string, imgSrc: string): string {
    return `
    <div class="image-container-128px">
        <div>
            <div class="image-overlay-128px tooltip" onclick="showBuildingInformation('${id}')">
                <div class="tooltiptext">${tooltip}</div>
            </div>
            <img src="${imgSrc}" />
            <div style="float: left; width: 0px;">
                <span id="${id}-count" class="image-text-inside-128px">0</span>
            </div>
        </div>
    </div>
    `
}
function generateDefenseHTML(id: string, tooltip: string, imgSrc: string): string {
    return `
    <div class="image-container-128px">
        <div>
            <div class="image-overlay-128px tooltip" onclick="showDefenseInformation('${id}')">
                <div class="tooltiptext">${tooltip}</div>
            </div>
            <img src="${imgSrc}" />
            <div style="float: left; width: 0px;">
                <span id="${id}-count" class="image-text-inside-128px">0</span>
            </div>
        </div>
    </div>
    `
}
function generateShipHTML(id: string, tooltip: string, imgSrc: string, countID: string): string {
    return `
      <div class="image-container-80px">
        <div>
          <div class="image-overlay-80px tooltip">
            <div class="tooltiptext">${tooltip}</div>
          </div>
          <img src="${imgSrc}" />
          <div style="float: left; width: 0px;">
            <span id="${countID}" class="image-text-inside-80px">0</span>
          </div>
        </div>
      </div>
    `
}
function generateTechnologyHTML(id: string, tooltip: string, imgSrc: string, countID: string): string {
    return `
      <div class="image-container-80px">
        <div>
          <div class="image-overlay-80px tooltip">
            <div class="tooltiptext">${tooltip}</div>
          </div>
          <img src="${imgSrc}" />
          <div style="float: left; width: 0px;">
            <span id="${countID}" class="image-text-inside-80px">0</span>
          </div>
        </div>
      </div>
    `
}
  
function generateBuildingGrid(jsonResponse: any): string {
    const buildings = [
        { id: 'bld-metal-mine', tooltip: 'Metal Refinery', imgSrc: '../static/assets/planet-building-metal-mine.png', description: 'This mine produces useable metals from various ores, with production increasing with each level.' },
        { id: 'bld-crystal-mine', tooltip: 'Crystal Mine', imgSrc: '../static/assets/planet-building-crystal-mine.png', description: 'This mine mines useable crystals from the ground, with production increasing with each level.' },
        { id: 'bld-gas-mine', tooltip: 'Gas Extractor', imgSrc: '../static/assets/planet-building-gas-mine.png', description: 'This mine extracts useable gases from the ocean, with production increasing with each level.' },
        { id: 'bld-factory', tooltip: 'Factory', imgSrc: '../static/assets/planet-building-factory.png', description: 'The factory drastically reduces the resources required to upgrade all other buildings.' },
        { id: 'bld-shipyard', tooltip: 'Shipyard', imgSrc: '../static/assets/planet-building-shipyard.png', description: 'A shipyard allows you to produce ships, with each upgrade increasing the size of ships and speed of construction.' },
        { id: 'bld-metal-storage', tooltip: 'Metal Depot', imgSrc: '../static/assets/planet-building-metal-storage.png', description: 'This depot stores metals produced by the metal refinery. Upgrades increase storage capacity.' },
        { id: 'bld-crystal-storage', tooltip: 'Crystal Depot', imgSrc: '../static/assets/planet-building-crystal-storage.png', description: 'This depot stores crystals produced by the crystal mine. Upgrades increase storage capacity.' },
        { id: 'bld-gas-storage', tooltip: 'Gas Storage', imgSrc: '../static/assets/planet-building-gas-storage.png', description: 'This depot stores gases produced by the gas extractor. Upgrades incerases storage capacity.' },
        { id: 'bld-laboratory', tooltip: 'Laboratory', imgSrc: '../static/assets/planet-building-laboratory.png', description: 'The laboratory enables you to conduct research on emerging technologies or enhance existing ones.' },
        { id: 'bld-terraformer', tooltip: 'Terraformer', imgSrc: '../static/assets/planet-building-terraformer.png', description: 'The terraformer allows you to construct additional buildings after the entire planet has been covered.' },
    ];
  
    const buildingHTML = buildings.map(building => generateBuildingHTML(building.id, building.tooltip, building.imgSrc)).join('')
    const buildingInfoHTML = buildings.map(building => generateBuildingInformationBox(jsonResponse, building.id, building.imgSrc, building.tooltip, building.description)).join('')
    return `
    <div id="information-box-container" style="justify-content: center; display: flex;">
        ${buildingInfoHTML}
    </div>
    <div style="display: grid; grid-template-columns: repeat(5, 150px); grid-gap: 20px; justify-content: left; background: var(--background-color); z-index: 1; position: sticky;">
        ${buildingHTML}
    </div>`
}
function generateDefenseGrid(jsonResponse: any): string {
    const defenses = [
        { id: 'def-aa', tooltip: 'AA Guns', imgSrc: '../static/assets/planet-defense-aa.png', description: 'AA Guns are small and not very strong, but they are very cheap and can be constructed en masse.' },
        { id: 'def-railgun', tooltip: 'Railgun Turrets', imgSrc: '../static/assets/planet-defense-railgun.png', description: 'Railgun turrets use electromagnets to launch hypersonic slugs at the enemy.' },
        { id: 'def-rocket', tooltip: 'Rocket Launchers', imgSrc: '../static/assets/planet-defense-rocket.png', description: 'Rocket Launchers are able to launch surface-to-orbit missiles tipped with nukes at enemy capital ships.' },
        { id: 'def-laser', tooltip: 'Laser Turrets', imgSrc: '../static/assets/planet-defense-laser.png', description: 'Laser turrets are ideal to use against small- or midsized ships due to their comparatively low cost and high output.' },
        { id: 'def-ion', tooltip: 'Ion Turrets', imgSrc: '../static/assets/planet-defense-ion.png', description: 'Ion turrets have the same raw power as lasers, but sacrifice armor for shield strength.' },
        { id: 'def-plasma', tooltip: 'Plasma Turrets', imgSrc: '../static/assets/planet-defense-plasma.png', description: 'Plasma turrets launch large plasma bolts against medium and large ships to melt their armor away.' },
        { id: 'def-disruptor', tooltip: 'Disruptor Turrets', imgSrc: '../static/assets/planet-defense-disruptor.png', description: 'Disruptor turrets can be used to rapidly disassemble even large capital ships in orbit.' },
        { id: 'def-s-shield', tooltip: 'Small Shield', imgSrc: '../static/assets/planet-defense-s-shield.png', description: 'A small shield generator that can protect the area surrounding it from the enemy. Only one can be built.' },
        { id: 'def-m-shield', tooltip: 'Large Shield', imgSrc: '../static/assets/planet-defense-m-shield.png', description: 'A large shield generator that can protect large regions from the enemy. Only one can be built.' },
        { id: 'def-l-shield', tooltip: 'Planetary Shield', imgSrc: '../static/assets/planet-defense-l-shield.png', description: 'A gigantic shield generator that can protect the entire planet from the enemy. Only one can be built.' },
    ];
    
    const defenseHTML = defenses.map(defense => generateDefenseHTML(defense.id, defense.tooltip, defense.imgSrc)).join('')
    const defenseInfoHTML = defenses.map(defense => generateDefenseInformationBox(jsonResponse, defense.id, defense.imgSrc, defense.tooltip, defense.description)).join('')
    return `
    <div id="information-box-container" style="justify-content: center; display: flex;">
        ${defenseInfoHTML}
    </div>
    <div style="display: grid; grid-template-columns: repeat(5, 150px); grid-gap: 20px; justify-content: left; background: var(--background-color); z-index: 1">
        ${defenseHTML}
    </div>`
}
function generateShipGrid(): string {
    const militaryShips = [
        { id: 'ship-fighter', tooltip: 'Fighter', imgSrc: '../static/assets/planet-shipyard-fighter-icon.png', countID: 'ship-fighter-count' },
        { id: 'ship-interceptor', tooltip: 'Interceptor', imgSrc: '../static/assets/planet-shipyard-interceptor-icon.png', countID: 'ship-interceptor-count' },
        { id: 'ship-tac-bomber', tooltip: 'Bomber', imgSrc: '../static/assets/planet-shipyard-tac-bomber-icon.png', countID: 'ship-tac-bomber-count' },
        { id: 'ship-str-bomber', tooltip: 'Strategic Bomber', imgSrc: '../static/assets/planet-shipyard-str-bomber-icon.png', countID: 'ship-str-bomber-count' },
        { id: 'ship-frigate', tooltip: 'Frigate', imgSrc: '../static/assets/planet-shipyard-frigate-icon.png', countID: 'ship-frigate-count' },
        { id: 'ship-destroyer', tooltip: 'Destroyer', imgSrc: '../static/assets/planet-shipyard-destroyer-icon.png', countID: 'ship-destroyer-count' },
        { id: 'ship-cruiser', tooltip: 'Cruiser', imgSrc: '../static/assets/planet-shipyard-cruiser-icon.png', countID: 'ship-cruiser-count' },
        { id: 'ship-escort-carrier', tooltip: 'Escort Carrier', imgSrc: '../static/assets/planet-shipyard-escort-carrier-icon.png', countID: 'ship-escort-carrier-count' },
        { id: 'ship-battlecruiser', tooltip: 'Battlecruiser', imgSrc: '../static/assets/planet-shipyard-battlecruiser-icon.png', countID: 'ship-battlecruiser-count' },
        { id: 'ship-battleship', tooltip: 'Battleship', imgSrc: '../static/assets/planet-shipyard-battleship-icon.png', countID: 'ship-battleship-count' },
        { id: 'ship-fleet-carrier', tooltip: 'Fleet Carrier', imgSrc: '../static/assets/planet-shipyard-fleet-carrier-icon.png', countID: 'ship-fleet-carrier-count' },
        { id: 'ship-titan', tooltip: 'Titan', imgSrc: '../static/assets/planet-shipyard-titan-icon.png', countID: 'ship-titan-count' },
    ]
    const civilianShips = [
        { id: 'ship-small-cargo', tooltip: 'Small Cargoship', imgSrc: '../static/assets/planet-shipyard-small-cargo-icon.png', countID: 'ship-small-cargo-count' },
        { id: 'ship-large-cargo', tooltip: 'Large Cargoship', imgSrc: '../static/assets/planet-shipyard-large-cargo-icon.png', countID: 'ship-large-cargo-count' },
        { id: 'ship-sattelites', tooltip: 'Sattelites', imgSrc: '../static/assets/planet-shipyard-sattelites-icon.png', countID: 'ship-sattelites-count' },
        { id: 'ship-colony-ship', tooltip: 'Colony Ship', imgSrc: '../static/assets/planet-shipyard-colony-ship-icon.png', countID: 'ship-colony-ship-count' },
        { id: 'ship-science-ship', tooltip: 'Science Ship', imgSrc: '../static/assets/planet-shipyard-science-ship-icon.png', countID: 'ship-science-ship-count' },
        { id: 'ship-construction-ship', tooltip: 'Construction Ship', imgSrc: '../static/assets/planet-shipyard-construction-ship-icon.png', countID: 'ship-construction-ship-count' },
    ];
  
    const militaryShipsHTML = militaryShips.map(ship => generateShipHTML(ship.id, ship.tooltip, ship.imgSrc, ship.countID)).join('')
    const civilianShipsHTML = civilianShips.map(ship => generateShipHTML(ship.id, ship.tooltip, ship.imgSrc, ship.countID)).join('')
    return `
     <div style="display: flex;">
         <div style="display: grid; grid-template-columns: repeat(4, 104px); grid-gap: 20px; justify-content: left; background: var(--background-color); z-index: 1">
            ${militaryShipsHTML}
         </div>
         <div style="margin-left: 70px; display: grid; grid-template-columns: repeat(2, 104px); grid-gap: 20px; justify-content: left; background: var(--background-color); z-index: 1">
            ${civilianShipsHTML}
         </div>
     </div>
    `
}
function generateTechnologyGrid(): string {
    const technologies = [
        { id: 'tec-energy', tooltip: 'Energy', imgSrc: '../static/assets/planet-tech-energy-icon.png', countID: 'tec-energy-count' },
        { id: 'tec-computing', tooltip: 'Computing', imgSrc: '../static/assets/planet-tech-computing-icon.png', countID: 'tec-computing-count' },
        { id: 'tec-hyperspace', tooltip: 'Hyperspace', imgSrc: '../static/assets/planet-tech-hyperspace-icon.png', countID: 'tec-hyperspace-count' },
        { id: 'tec-production', tooltip: 'Production', imgSrc: '../static/assets/planet-tech-production-icon.png', countID: 'tec-production-count' },
        { id: 'tec-colonization', tooltip: 'Colonization', imgSrc: '../static/assets/planet-tech-colonization-icon.png', countID: 'tec-colonization-count' },
        { id: 'tec-shield', tooltip: 'Shields', imgSrc: '../static/assets/planet-tech-shield-icon.png', countID: 'tec-shield-count' },
        { id: 'tec-armor', tooltip: 'Armor', imgSrc: '../static/assets/80px-refrence.png', countID: 'tec-armor-count' },
        { id: 'tec-engine', tooltip: 'Engine', imgSrc: '../static/assets/planet-tech-engine-icon.png', countID: 'tec-engine-count' },
        { id: 'tec-storage', tooltip: 'Storage', imgSrc: '../static/assets/planet-tech-storage-icon.png', countID: 'tec-storage-count' },
        { id: 'tec-hangar', tooltip: 'Hangar', imgSrc: '../static/assets/planet-tech-hangar-icon.png', countID: 'tec-hangar-count' },
        { id: 'tec-conv-weapon', tooltip: 'Conventional Weapons', imgSrc: '../static/assets/planet-tech-conv-weapons-icon.png', countID: 'tec-conv-weapon-count' },
        { id: 'tec-laser', tooltip: 'Laser Weapons', imgSrc: '../static/assets/planet-tech-laser-icon.png', countID: 'tec-laser-count' },
        { id: 'tec-ion', tooltip: 'Ion Weapons', imgSrc: '../static/assets/planet-tech-ion-icon.png', countID: 'tec-ion-count' },
        { id: 'tec-plasma', tooltip: 'Plasma Weapons', imgSrc: '../static/assets/planet-tech-plasma-icon.png', countID: 'tec-plasma-count' },
        { id: 'tec-disruptor', tooltip: 'Disruptor Weapons', imgSrc: '../static/assets/planet-tech-disruptor-icon.png', countID: 'tec-disruptor-count' },
    ];
  
    const defenseHTML = technologies.map(technologies => generateTechnologyHTML(technologies.id, technologies.tooltip, technologies.imgSrc, technologies.countID)).join('')
    return `<div style="display: grid; grid-template-columns: repeat(5, 104px); grid-gap: 20px; justify-content: center; background: var(--background-color); z-index: 1">
        ${defenseHTML}
    </div>`
}

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
            console.log(response)
            document.getElementById("planet-news-dislay")!.innerHTML = `${response.status} - ${response.statusText}`
        }

        const jsonResponse = await response.json();
        document.getElementById("metal-amount")!.innerHTML = `${Math.round(jsonResponse.metal_amount.toLocaleString())}`
        document.getElementById("crystal-amount")!.innerHTML = `${Math.round(jsonResponse.crystal_amount.toLocaleString())}`
        document.getElementById("gas-amount")!.innerHTML = `${Math.round(jsonResponse.gas_amount.toLocaleString())}`
        document.getElementById("overview-button")!.setAttribute('href', `overview?planet=${planetID}`)
        document.getElementById("buildings-button")!.setAttribute('href', `buildings?planet=${planetID}`)
        document.getElementById("defense-button")!.setAttribute('href', `defense?planet=${planetID}`)
        document.getElementById("shipyard-button")!.setAttribute('href', `shipyard?planet=${planetID}`)
        document.getElementById("fleet-button")!.setAttribute('href', `fleet?planet=${planetID}`)
        document.getElementById("technology-button")!.setAttribute('href', `technology?planet=${planetID}`)

        if (page_name === "overview") {
            document.getElementById("planet-name")!.innerHTML   = jsonResponse.name
            document.getElementById("planet-coords")!.innerHTML = `[${jsonResponse.position[0]} : ${jsonResponse.position[1]} : ${jsonResponse.position[2]}]`
            document.getElementById("planet-radius")!.innerHTML = `${jsonResponse.radius.toLocaleString()} km`
            document.getElementById("planet-temperature")!.innerHTML = `${jsonResponse.temperature} C°`
        }
        else if (page_name == "buildings") {
            document.getElementById("main-content")!.innerHTML += generateBuildingGrid(jsonResponse)

            document.getElementById("bld-metal-mine-count")!.innerHTML = jsonResponse.bld_metal_mine.toLocaleString()
            document.getElementById("bld-crystal-mine-count")!.innerHTML = jsonResponse.bld_crystal_mine.toLocaleString()
            document.getElementById("bld-gas-mine-count")!.innerHTML = jsonResponse.bld_gas_mine.toLocaleString()
            document.getElementById("bld-factory-count")!.innerHTML = jsonResponse.bld_factory.toLocaleString()
            document.getElementById("bld-shipyard-count")!.innerHTML = jsonResponse.bld_shipyard.toLocaleString()
            document.getElementById("bld-metal-storage-count")!.innerHTML = jsonResponse.bld_metal_storage.toLocaleString()
            document.getElementById("bld-crystal-storage-count")!.innerHTML = jsonResponse.bld_crystal_storage.toLocaleString()
            document.getElementById("bld-gas-storage-count")!.innerHTML = jsonResponse.bld_gas_storage.toLocaleString()
            document.getElementById("bld-laboratory-count")!.innerHTML = jsonResponse.bld_laboratory.toLocaleString()
            document.getElementById("bld-terraformer-count")!.innerHTML = jsonResponse.bld_terraformer.toLocaleString()
        }
        else if (page_name == "defense") {
            document.getElementById("main-content")!.innerHTML += generateDefenseGrid(jsonResponse)

            document.getElementById("def-aa-count")!.innerHTML = `${jsonResponse.def_aa}`
            document.getElementById("def-railgun-count")!.innerHTML = `${jsonResponse.def_railgun}`
            document.getElementById("def-rocket-count")!.innerHTML = `${jsonResponse.def_rocket}`
            document.getElementById("def-laser-count")!.innerHTML = `${jsonResponse.def_laser}`
            document.getElementById("def-ion-count")!.innerHTML = `${jsonResponse.def_ion}`
            document.getElementById("def-plasma-count")!.innerHTML = `${jsonResponse.def_plasma}`
            document.getElementById("def-disruptor-count")!.innerHTML = `${jsonResponse.def_disruptor}`
            document.getElementById("def-s-shield-count")!.innerHTML = `${jsonResponse.def_s_shield}`
            document.getElementById("def-m-shield-count")!.innerHTML = `${jsonResponse.def_m_shield}`
            document.getElementById("def-l-shield-count")!.innerHTML = `${jsonResponse.def_l_shield}`
        }
        else if (page_name == "shipyard") {
            document.getElementById("main-content")!.innerHTML += generateShipGrid()

            if (jsonResponse.stationed_fleet !== null) {
                document.getElementById("ship-fighter-count")!.innerHTML = `${jsonResponse.stationed_fleet.fighters}`
                document.getElementById("ship-interceptor-count")!.innerHTML = `${jsonResponse.stationed_fleet.interceptors}`
                document.getElementById("ship-tac-bomber-count")!.innerHTML = `${jsonResponse.stationed_fleet.tac_bombers}`
                document.getElementById("ship-str-bomber-count")!.innerHTML = `${jsonResponse.stationed_fleet.str_bombers}`
                document.getElementById("ship-frigate-count")!.innerHTML = `${jsonResponse.stationed_fleet.frigates}`
                document.getElementById("ship-destroyer-count")!.innerHTML = `${jsonResponse.stationed_fleet.destroyers}`
                document.getElementById("ship-cruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.cruisers}`
                document.getElementById("ship-battlecruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.battlecruisers}`
                document.getElementById("ship-battleship-count")!.innerHTML = `${jsonResponse.stationed_fleet.battleships}`
                document.getElementById("ship-escort-carrier-count")!.innerHTML = `${jsonResponse.stationed_fleet.escort_carriers}`
                document.getElementById("ship-fleet-carrier-count")!.innerHTML = `${jsonResponse.stationed_fleet.fleet_carriers}`
                document.getElementById("ship-titan-count")!.innerHTML = `${jsonResponse.stationed_fleet.titans}`
                document.getElementById("ship-sattelites-count")!.innerHTML = `${jsonResponse.stationed_fleet.sattelites}`
                document.getElementById("ship-small-cargo-count")!.innerHTML = `${jsonResponse.stationed_fleet.small_cargo_ships}`
                document.getElementById("ship-large-cargo-count")!.innerHTML = `${jsonResponse.stationed_fleet.small_cargo_ships}`
                document.getElementById("ship-colony-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.colony_ships}`
                document.getElementById("ship-science-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.science_ships}`
                document.getElementById("ship-construction-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.construction_ships}`
            }
        }
        else if (page_name == "technology") {
            document.getElementById("main-content")!.innerHTML += generateTechnologyGrid()
        }

        let loopCalls = 0
        const maxMetalAmount = 2 ** (0.5 * jsonResponse.bld_metal_storage) * 500000
        const maxCrystalAmount = 2 ** (0.5 * jsonResponse.bld_crystal_storage) * 500000
        const maxGasAmount = 2 ** (0.5 * jsonResponse.bld_gas_storage) * 500000
        let metalAmount = jsonResponse.metal_amount
        let crystalAmount = jsonResponse.crystal_amount
        let gasAmount = jsonResponse.gas_amount
        let bonusMetal = 1
        let bonusGas = 1
        let bonusCrystals = 1
        if (jsonResponse.temperature >= 423) { bonusMetal = 1.3 }
        else if (jsonResponse.temperature >= 210) { bonusMetal = 1.2 }
        else if (jsonResponse.temperature >= 82) { bonusMetal = 1.1 }
        if (jsonResponse.temperature <= -184) { bonusGas = 1.3 }
        else if (jsonResponse.temperature <= -170) { bonusGas = 1.2 }
        else if (jsonResponse.temperature <= -152) { bonusGas = 1.1 }
        if (bonusMetal == 1 && bonusGas == 1) { bonusCrystals = 1.15 }

        while (true) {
            if (metalAmount < maxMetalAmount) { 
                metalAmount = Math.round(jsonResponse.metal_amount + 8 * (jsonResponse.bld_metal_mine ** 1.1) * jsonResponse.owner.galaxy.resource_speed * bonusMetal * loopCalls)
            }
            if (crystalAmount < maxCrystalAmount) {
                crystalAmount = Math.round(jsonResponse.crystal_amount + 8 * (jsonResponse.bld_crystal_mine ** 1.1) * jsonResponse.owner.galaxy.resource_speed * bonusCrystals * loopCalls)
            }
            if (gasAmount < maxGasAmount) {
                gasAmount = Math.round(jsonResponse.gas_amount + 8 * (jsonResponse.bld_gas_mine ** 1.1) * jsonResponse.owner.galaxy.resource_speed * bonusGas * loopCalls)
            }

            document.getElementById("metal-amount")!.innerHTML = `${metalAmount}`;
            document.getElementById("crystal-amount")!.innerHTML = `${crystalAmount}`;
            document.getElementById("gas-amount")!.innerHTML = `${gasAmount}`; 
            document.getElementById("metal-amount")!.style.setProperty("color", getResourceColor(metalAmount, maxMetalAmount))
            document.getElementById("crystal-amount")!.style.setProperty("color", getResourceColor(crystalAmount, maxCrystalAmount))
            document.getElementById("gas-amount")!.style.setProperty("color", getResourceColor(gasAmount, maxGasAmount))
            loopCalls++;
    
            await new Promise(resolve => setTimeout(resolve, 1000))
        }
    } 
    catch (error) {
        console.error("Error:", error);
    }
}