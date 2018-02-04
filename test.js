const captionbot = require('captionbot');

captionbot('http://imgur.com/B7a15F5.jpg')
    .then(caption => {
        console.log(caption);
    })