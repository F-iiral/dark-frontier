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

        if (page_name === "overview") {
            document.getElementById("planet-name")!.innerHTML   = jsonResponse.name
            document.getElementById("planet-coords")!.innerHTML = `[${jsonResponse.position[0]} : ${jsonResponse.position[1]} : ${jsonResponse.position[2]}]`
            document.getElementById("planet-radius")!.innerHTML = `${jsonResponse.radius.toLocaleString()} km`
            document.getElementById("planet-temperature")!.innerHTML = `${jsonResponse.temperature} C°`
        }
        else if (page_name == "buildings") {
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
            if (jsonResponse.stationed_fleet !== null) {
                document.getElementById("ship-fighter-count")!.innerHTML = `${jsonResponse.stationed_fleet.fighter}`
                document.getElementById("ship-interceptor-count")!.innerHTML = `${jsonResponse.stationed_fleet.interceptor}`
                document.getElementById("ship-tac-bomber-count")!.innerHTML = `${jsonResponse.stationed_fleet.tac_bomber}`
                document.getElementById("ship-str-bomber-count")!.innerHTML = `${jsonResponse.stationed_fleet.str_bomber}`
                document.getElementById("ship-frigate-count")!.innerHTML = `${jsonResponse.stationed_fleet.frigate}`
                document.getElementById("ship-destroyer-count")!.innerHTML = `${jsonResponse.stationed_fleet.destroyer}`
                document.getElementById("ship-cruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.cruiser}`
                document.getElementById("ship-battlecruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.battlecruiser}`
                document.getElementById("ship-battleship-count")!.innerHTML = `${jsonResponse.stationed_fleet.battleship}`
                document.getElementById("ship-escort-carrier-count")!.innerHTML = `${jsonResponse.stationed_fleet.escort_carrier}`
                document.getElementById("ship-fleet-carrier-count")!.innerHTML = `${jsonResponse.stationed_fleet.fleet_carrier}`
                document.getElementById("ship-titan-count")!.innerHTML = `${jsonResponse.stationed_fleet.titan}`
                document.getElementById("ship-cruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.cruiser}`
                document.getElementById("ship-battlecruiser-count")!.innerHTML = `${jsonResponse.stationed_fleet.battlecruiser}`
                document.getElementById("ship-battleship-count")!.innerHTML = `${jsonResponse.stationed_fleet.battleship}`
                document.getElementById("ship-colony-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.colony_ship}`
                document.getElementById("ship-science-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.science_ship}`
                document.getElementById("ship-construction-ship-count")!.innerHTML = `${jsonResponse.stationed_fleet.construction_ship}`
            }
        }

        let loop_calls = 0
        const maxMetalAmount = 2 ** (0.5 * jsonResponse.bld_metal_storage) * 500000
        const maxCrystalAmount = 2 ** (0.5 * jsonResponse.bld_crystal_storage) * 500000
        const maxGasAmount = 2 ** (0.5 * jsonResponse.bld_gas_storage) * 500000

        while (true) {
            let metalAmount = Math.round(jsonResponse.metal_amount + jsonResponse.bld_metal_mine * jsonResponse.owner.galaxy.resource_speed * 8 * loop_calls)
            let crystalAmount = Math.round(jsonResponse.crystal_amount + jsonResponse.bld_crystal_mine * jsonResponse.owner.galaxy.resource_speed * 8 * loop_calls)
            let gasAmount = Math.round(jsonResponse.gas_amount + jsonResponse.bld_gas_mine * jsonResponse.owner.galaxy.resource_speed * 8 * loop_calls)

            if (metalAmount < maxMetalAmount) { document.getElementById("metal-amount")!.innerHTML = `${metalAmount.toLocaleString()}`; }
            if (crystalAmount < maxCrystalAmount) { document.getElementById("crystal-amount")!.innerHTML = `${crystalAmount.toLocaleString()}`; }
            if (gasAmount < maxGasAmount) { document.getElementById("gas-amount")!.innerHTML = `${gasAmount.toLocaleString()}`; }
            document.getElementById("metal-amount")!.style.setProperty("color", getResourceColor(metalAmount, maxMetalAmount))
            document.getElementById("crystal-amount")!.style.setProperty("color", getResourceColor(crystalAmount, maxCrystalAmount))
            document.getElementById("gas-amount")!.style.setProperty("color", getResourceColor(gasAmount, maxGasAmount))
            loop_calls++;
    
            await new Promise(resolve => setTimeout(resolve, 1000))
        }
    } 
    catch (error) {
        console.error("Error:", error);
    }
}