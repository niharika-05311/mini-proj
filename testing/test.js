const { Builder, By } = require('selenium-webdriver');

(async function test() {
    let driver = await new Builder().forBrowser('chrome').build();

    await driver.get('http://localhost:5000');

    let text = await driver.findElement(By.tagName('body')).getText();

    console.log("Page content:", text);

    if (text.includes("Working") || text.includes("Registered")) {
        console.log("Test Passed");
    } else {
        console.log("Test Failed");
    }

    await driver.quit();
})();