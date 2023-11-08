if (localStorage.getItem("theme") == 1) {
    document.querySelector('#css').href = 'light.css';
}
else {
    document.querySelector('#css').href = 'dark.css';
}

document.querySelector('#theme-btn').addEventListener('click', () => {
    if (localStorage.getItem("theme") == 1) {
        localStorage.setItem("theme", 0);
    }
    else {
        localStorage.setItem("theme", 1);
    }
    if (localStorage.getItem("theme") == 1) {
        document.querySelector('#css').href = 'light.css';
    }
    else {
        document.querySelector('#css').href = 'dark.css';
    }
});