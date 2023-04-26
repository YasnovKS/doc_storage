const versions = document.querySelectorAll('div.version');
versions.forEach((version) => {
    version.addEventListener('click', function(version){
        let next_p = version.target.nextElementSibling.nextElementSibling
        if (next_p.classList.contains('hidden')) {
            next_p.classList.remove('hidden')
        }
        else {
            next_p.classList.add('hidden')
        }
    })
}
)
