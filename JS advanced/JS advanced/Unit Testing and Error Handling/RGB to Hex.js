const {expect} = require('chai');

function rgbToHexColor(red, green, blue) {
    if (!Number.isInteger(red) || (red < 0) || (red > 255)){
        return undefined; // Red value is invalid
    }
    if (!Number.isInteger(green) || (green < 0) || (green > 255)){
        return undefined; // Green value is invalid
    }
    if (!Number.isInteger(blue) || (blue < 0) || (blue > 255)){
        return undefined; // Blue value is invalid
    }
    return "#" +
        ("0" + red.toString(16).toUpperCase()).slice(-2) +
        ("0" + green.toString(16).toUpperCase()).slice(-2) +
        ("0" + blue.toString(16).toUpperCase()).slice(-2);
}

describe('rgbToHexColor', () => {
    it('first param', () => {
        expect(rgbToHexColor('asd', 1, 1)).to.be.undefined;
        expect(rgbToHexColor(-1, 1, 1)).to.be.undefined;
        expect(rgbToHexColor(256, 1, 1)).to.be.undefined;
        expect(rgbToHexColor('1', 2, 3)).to.be.undefined;
        expect(rgbToHexColor('1', '2', '3')).to.be.undefined;
    });
    it('second param', () => {
        expect(rgbToHexColor(1, 'das', 1)).to.be.undefined;
        expect(rgbToHexColor(1, -1, 1)).to.be.undefined;
        expect(rgbToHexColor(1, 256, 1)).to.be.undefined;
        expect(rgbToHexColor(1, '2', 3)).to.be.undefined;
    });
    it('third param', () => {
        expect(rgbToHexColor(1, 1, 'das')).to.be.undefined;
        expect(rgbToHexColor(1, 1, -1)).to.be.undefined;
        expect(rgbToHexColor(1, 1, 256)).to.be.undefined;
        expect(rgbToHexColor(1, 2, '3')).to.be.undefined;
    });
    it('valid input', () => {
        expect(rgbToHexColor(1, 1, 1)).to.be.equal('#010101');
        expect(rgbToHexColor(10, 20, 30)).to.be.equal('#0A141E');
        expect(rgbToHexColor(100, 200, 250)).to.be.equal('#64C8FA');
        expect(rgbToHexColor(1, 150, 255)).to.be.equal('#0196FF');
        expect(rgbToHexColor(0, 150, 255)).to.be.equal('#0096FF');
    })
})