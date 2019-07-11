/*
 * hello-world.js
 * Copyright (C) 2019 damian <damian@damian-laptop>
 *
 * Distributed under terms of the MIT license.
 */

import { Selector } from 'testcafe';

fixture `Getting Started`
    .page `http://devexpress.github.io/testcafe/example`;

test('My first test', async t => {
    await t
        .typeText('#developer-name', 'John Smith')
        .click('#submit-button')
        .expect(Selector('#article-header').innerText).eql('Thank you, John Smith!');
});

