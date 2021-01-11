


let checks = document.querySelectorAll(".fa-check")

for (let check of checks) {
    check.addEventListener('click', e => {
        check.classList.toggle('fas')
        check.classList.toggle('far')
        let answerPk = check.parentElement.dataset.answerPk
        let url = `core/${answerPk}/correct`
        fetch(url, {
            heaers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => {
            return response.json()
        })
        .then(data => {
            //Perform actions with the response data from the view
            
        })
        
    })
}
