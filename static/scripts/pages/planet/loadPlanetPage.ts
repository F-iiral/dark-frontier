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

function generateBuildingHTML(id: string, tooltip: string, imgSrc: string, countID: string): string {
    return `
    <div class="image-container-128px">
        <div>
            <div class="image-overlay-128px tooltip">
                <div class="tooltiptext">${tooltip}</div>
            </div>
            <img src="${imgSrc}" />
            <div style="float: left; width: 0px;">
                <span id="${countID}" class="image-text-inside-128px">0</span>
            </div>
        </div>
    </div>
    `
}
function generateDefenseHTML(id: string, tooltip: string, imgSrc: string, countID: string): string {
    return `
    <div class="image-container-128px">
        <div>
            <div class="image-overlay-128px tooltip">
                <div class="tooltiptext">${tooltip}</div>
            </div>
            <img src="${imgSrc}" />
            <div style="float: left; width: 0px;">
                <span id="${countID}" class="image-text-inside-128px">0</span>
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
  
function generateBuildingGrid(): string {
    const buildings = [
        { id: 'bld-metal-mine', tooltip: 'Metal Mine', imgSrc: '../static/assets/planet-building-metal-mine.png', countID: 'bld-metal-mine-count' },
        { id: 'bld-crystal-mine', tooltip: 'Crystal Mine', imgSrc: '../static/assets/planet-building-crystal-mine.png', countID: 'bld-crystal-mine-count' },
        { id: 'bld-gas-mine', tooltip: 'Gas Extractor', imgSrc: '../static/assets/planet-building-gas-mine.png', countID: 'bld-gas-mine-count' },
        { id: 'bld-factory', tooltip: 'Factory', imgSrc: '../static/assets/planet-building-factory.png', countID: 'bld-factory-count' },
        { id: 'bld-shipyard', tooltip: 'Shipyard', imgSrc: '../static/assets/planet-building-shipyard.png', countID: 'bld-shipyard-count' },
        { id: 'bld-metal-storage', tooltip: 'Metal Storage', imgSrc: '../static/assets/planet-building-metal-storage.png', countID: 'bld-metal-storage-count' },
        { id: 'bld-crystal-storage', tooltip: 'Crystal Storage', imgSrc: '../static/assets/planet-building-crystal-storage.png', countID: 'bld-crystal-storage-count' },
        { id: 'bld-gas-storage', tooltip: 'Gas Storage', imgSrc: '../static/assets/planet-building-gas-storage.png', countID: 'bld-gas-storage-count' },
        { id: 'bld-laboratory', tooltip: 'Laboratory', imgSrc: '../static/assets/planet-building-laboratory.png', countID: 'bld-laboratory-count' },
        { id: 'bld-terraformer', tooltip: 'Terraformer', imgSrc: '../static/assets/planet-building-terraformer.png', countID: 'bld-terraformer-count' },
    ];
  
    const buildingHTML = buildings.map(building => generateBuildingHTML(building.id, building.tooltip, building.imgSrc, building.countID)).join('')
    return `<div style="display: grid; grid-template-columns: repeat(5, 150px); grid-gap: 20px; justify-content: left;">${buildingHTML}</div>`
}
function generateDefenseGrid(): string {
    const defenses = [
        { id: 'def-aa', tooltip: 'AA Guns', imgSrc: '../static/assets/planet-defense-aa.png', countID: 'def-aa-count' },
        { id: 'def-railgun', tooltip: 'Railgun Turrets', imgSrc: '../static/assets/planet-defense-railgun.png', countID: 'def-railgun-count' },
        { id: 'def-rocket', tooltip: 'Rocket Launchers', imgSrc: '../static/assets/planet-defense-rocket.png', countID: 'def-rocket-count' },
        { id: 'def-laser', tooltip: 'Laser Turrets', imgSrc: '../static/assets/planet-defense-laser.png', countID: 'def-laser-count' },
        { id: 'def-ion', tooltip: 'Ion Turrets', imgSrc: '../static/assets/planet-defense-ion.png', countID: 'def-ion-count' },
        { id: 'def-plasma', tooltip: 'Plasma Turrets', imgSrc: '../static/assets/planet-defense-plasma.png', countID: 'def-plasma-count' },
        { id: 'def-disruptor', tooltip: 'Disruptor Turrets', imgSrc: '../static/assets/planet-defense-disruptor.png', countID: 'def-disruptor-count' },
        { id: 'def-s-shield', tooltip: 'Small Shield Generator', imgSrc: '../static/assets/planet-defense-s-shield.png', countID: 'def-s-shield-count' },
        { id: 'def-m-shield', tooltip: 'Large Shield Generator', imgSrc: '../static/assets/planet-defense-m-shield.png', countID: 'def-m-shield-count' },
        { id: 'def-l-shield', tooltip: 'Planetary Shield Generator', imgSrc: '../static/assets/planet-defense-l-shield.png', countID: 'def-l-shield-count' },
    ];
  
    const defenseHTML = defenses.map(defense => generateDefenseHTML(defense.id, defense.tooltip, defense.imgSrc, defense.countID)).join('')
    return `<div style="display: grid; grid-template-columns: repeat(5, 150px); grid-gap: 20px; justify-content: left;">${defenseHTML}</div>`
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
         <div style="display: grid; grid-template-columns: repeat(4, 104px); grid-gap: 20px; justify-content: left;">
            ${militaryShipsHTML}
         </div>
         <div style="margin-left: 70px; display: grid; grid-template-columns: repeat(2, 104px); grid-gap: 20px; justify-content: left;">
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
    return `<div style="display: grid; grid-template-columns: repeat(5, 104px); grid-gap: 20px; justify-content: center;">${defenseHTML}</div>`
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
            document.getElementById("main-content")!.innerHTML += generateBuildingGrid()

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
            document.getElementById("main-content")!.innerHTML += generateDefenseGrid()

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