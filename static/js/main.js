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
    document.getElementById('invite-modal').style.display='block'
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

document.getElementById('send_number').addEventListener('click', () => {
    var mobile = document.getElementById('mobile').value
    console.log(mobile)
    send_invite(mobile)
    anime({
        targets: ['#invite-modal', '.overlay', '.close'],
        translateY: -775,
        easing: 'easeInOutExpo'
    })

})

function send_invite(mobile){
    let chatname = location.pathname.split('/').pop()
    var url = `http://localhost:5000/invite/${chatname}`
    data = {
        mobile_number: mobile
    }
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url)
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.send(JSON.stringify(data)) 
}