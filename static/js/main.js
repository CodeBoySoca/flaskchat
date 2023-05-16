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


document.getElementById('menu-button').addEventListener('click', (e) => {
    e.stopPropagation();
    let overlay = document.createElement('div')
    let modal = document.getElementById('invite-modal')
    overlay.setAttribute('class', 'overlay')
    document.body.appendChild(overlay)
    document.getElementById('menu').style.display='block'
    document.getElementById('close').style.display='block'
    overlay.appendChild(modal)
    //document.getElementById('invite-modal').style.display='block'
    
    anime({
        targets: ['.menu'],
        translateX: 400,
        easing: 'easeInOutExpo'
    })

    anime({
        targets: ['.close'],
        translateX: 0,
        easing: 'easeInOutExpo'
    })


    // anime({
    //     targets: ['#invite-modal'],
    //     translateY: 0,
    //     easing: 'easeInOutExpo'
    // })


    document.getElementById('close').addEventListener('click', () => {
        anime({
            targets:  ['.overlay', '.close', '.menu'],
            translateX: 2900,
            easing: 'easeInOutExpo'
        })
        anime({
            targets: '#invite-modal',
            translateY: 0,
            easing: 'easeInOutExpo'
        })
    })
   
})


document.getElementById('invite').addEventListener('click', () => {

    let modal = document.getElementById('invite-modal').style.display='block'
 

    anime({
        targets : '.menu',
        translateX : -2900,
        easing: 'easeInOutExpo'
    })

    anime({
        targets: '#invite-modal',
        translateY: 775,
        easing: 'easeInOutExpo'
    })

})



