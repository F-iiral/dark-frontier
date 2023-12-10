namespace Overview {
    function getCookie (name: string): string | null {
        const cookies = document.cookie.split('; ');

        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.split('=');
            if (cookieName === name) { return cookieValue; }
        }
        return null;
    };

    async function loadPlanetOverview (planetID: number): Promise<void> {
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
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const jsonResponse = await response.json();
            document.getElementById("metal-amount")!.innerHTML = jsonResponse["metal_amount"];
            document.getElementById("crystal-amount")!.innerHTML = jsonResponse["crystal_amount"];
            document.getElementById("gas-amount")!.innerHTML = jsonResponse["gas_amount"];
            // Add more here for later use (name, owner, etc.)
        } 
        catch (error) {
            console.error("Error:", error);
        }
    }
}