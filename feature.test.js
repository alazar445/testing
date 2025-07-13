const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('Feature Branch HTML Test', () => {
  let dom;
  let document;

  beforeAll(() => {
    const html = fs.readFileSync(path.resolve(__dirname, 'testing.html'), 'utf8');
    dom = new JSDOM(html);
    document = dom.window.document;
  });

  test('renders h1 with correct text', () => {
    const h1 = document.querySelector('h1');
    expect(h1).not.toBeNull();
    expect(h1.textContent).toBe('Hello from the Feature Branch!');
  });

  test('renders paragraph with correct text', () => {
    const p = document.querySelector('p');
    expect(p).not.toBeNull();
    expect(p.textContent).toBe('This is a simple HTML file for testing.');
  });

  test('has a valid doctype', () => {
    expect(dom.serialize().startsWith('<!DOCTYPE html>')).toBe(true);
  });
});
