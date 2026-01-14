//we use the setTimeout method and pipes

async function sleep(millis: number): Promise<void> {
    return new Promise(timenow => setTimeout(timenow, millis));

}
