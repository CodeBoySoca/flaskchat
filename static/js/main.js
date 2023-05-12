document.getElementById('show').addEventListener('click', () => {
    anime({
        targets: '.message-container',
        translateY: -350,
        easing: 'easeInOutExpo'
    })
})

document.getElementById('hide').addEventListener('click', () => {
    anime({
        targets: '.message-container',
        translateY: 0,
        easing: 'easeInOutExpo'
    })
})
