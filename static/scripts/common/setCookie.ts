export const setCookie = (name: string, value: string, duration: number=30, priority: number=1): void => {
    const currentDate = new Date();
    const expirationDate = new Date(currentDate.getTime() + duration * 24 * 60 * 60 * 1000);

    document.cookie = `${name}=${value}; expires=${expirationDate.toUTCString()}; priority=${priority}`;
};