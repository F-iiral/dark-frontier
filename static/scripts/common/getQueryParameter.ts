function getQueryParam(param: string): any {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}