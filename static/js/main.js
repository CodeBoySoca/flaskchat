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
    let menu = document.createElement('div')
    let inviteMenuItem = document.createElement('div')
    let logoutMenuItem = document.createElement('div')
    let closeButton = document.createElement('div')
    let inviteLink = document.createElement('a')
    let logoutLink = document.createElement('a')
    let closeLink = document.createElement('a')

    inviteLink.innerHTML = 'INVITE A FRIEND'
    logoutLink.innerHTML = 'LOGOUT'
    closeLink.innerHTML = '[X]CLOSE'

    inviteMenuItem.appendChild(inviteLink)
    logoutMenuItem.appendChild(logoutLink)
    closeButton.appendChild(closeLink)



    inviteLink.setAttribute('href', '/invite')
    logoutLink.setAttribute('href', '/logout')
    closeLink.setAttribute('id', 'close')
    overlay.setAttribute('class', 'overlay')
    

    menu.setAttribute('class', 'menu')
    menu.setAttribute('id', 'menu')
    closeButton.setAttribute('class', 'close')

    document.body.appendChild(overlay)
    document.body.appendChild(closeButton)
    overlay.appendChild(menu)
    menu.appendChild(inviteMenuItem)
    menu.appendChild(logoutMenuItem)
    anime({
        targets: '.menu',
        translateX: 400,
        easing: 'easeInOutExpo'
    })

    //TODO: make this work whenever its clicked, not just the first time
    document.getElementById('close').addEventListener('click', () => {
        anime({
            targets:  ['.overlay', '.close'],
            translateX: 1900,
            easing: 'easeInOutExpo'
        })
   })

   
})



