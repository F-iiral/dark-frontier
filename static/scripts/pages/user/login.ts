export const setCookie = (name: string, value: string, duration: number=30, priority: number=1): void => {
    const currentDate = new Date();
    const expirationDate = new Date(currentDate.getTime() + duration * 24 * 60 * 60 * 1000);

    document.cookie = `${name}=${value}; expires=${expirationDate.toUTCString()}; priority=${priority}`;
};

async function sendUserLoginRequest(username: string, password: string) {
    try {
        const url = "../api/user/login";
        const data = {
            "username": username,
            "password": password
        };
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
              "Content-Type": "application/json",
              "Accept": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error("HTTP error! Status: ${response.status}");
        }

        const jsonResponse = await response.json();
        setCookie("Authorization", jsonResponse)
    } 
    catch (error) {
      console.error("Error:", error);
    }
}