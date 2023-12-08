import { setCookie } from "../../common/setCookie"

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
        console.log(jsonResponse);
        setCookie("authorization", jsonResponse)
    } 
    catch (error) {
      console.error("Error:", error.message);
    }
}