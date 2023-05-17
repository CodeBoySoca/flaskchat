
/**  Chat = Web socket code */

const socket = io({autoConnect: false})

/**  Menu and chat window animations  */
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

/** AJAX call  */
document.getElementById('send_number').addEventListener('click', () => {
    var mobile = document.getElementById('mobile').value
    send_invite(mobile)
    anime({
        targets: ['#invite-modal', '.overlay', '.close'],
        translateY: -1275,
        easing: 'easeInOutExpo'
    })
    document.getElementById('mobile').value=''

})

function send_invite(mobile){
    let chatname = getChatname()
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

function getChatname(){
  return location.pathname.split('/').pop()
}

/** Chat  */

document.getElementById('chatbox').addEventListener('keypress', (evt) => { 
    if(evt.key == 'Enter'){
        let chatMessage = document.getElementById('chatbox').value
        let chatroom = getChatname()
        socket.connect()
        socket.emit('user_join', {chatroom: chatroom, message: chatMessage})
        document.getElementById('chatbox').value=''
    }
 

})