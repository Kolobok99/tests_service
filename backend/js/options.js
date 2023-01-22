
const trueButton = document.getElementById('get_true')

trueButton.addEventListener('click', async () => {
    const questionId = document.getElementById('title').innerHTML
    url = `http://127.0.0.1:8000/api/v1/question/${questionId}/`
    let response = await fetch(url)
    const trues = await response.json()
    for (let id of trues) {
        const option = document.getElementById(`option_${id}`)
        option.checked = true
    }
})