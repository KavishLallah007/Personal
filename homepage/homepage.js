document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
    let name = document.querySelector('#name').value;
    let clan = document.querySelector('#clan').value;

    if(clan =='Hyuga' || clan =='Uchiha' || clan =='Senju')
    {
        alert('Welcome, ' + name + '. You are now a member of the ' + clan + ' clan!');
        event.preventDefault();
    }
    else
    {
        alert('You are not registered, incorrect clan!');
        event.preventDefault();
    }
    });
});