/* abre e fecha menu lateral em modo mobile */

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");
    body.classList.toggle("menu-nav-active");
});

/* Fecha o menu quando clicar em algum item e muda icone para list */
const NavItem = document.querySelectorAll('.nav-item')

/* console.log(Navitem)*/

NavItem.forEach(item => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")){
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x", "bi-list");
        }
    })
})

// Animar todos os itens na tela que tiveram um atributo data-anime

//https://davidwalsh.name/javascript-debounce-function
// Returns a function, that, as long as it continues to be invoked, will not
// be triggered. The function will be called after it stops being called for
// N milliseconds. If `immediate` is passed, trigger the function on the
// leading edge, instead of the trailing.
function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};


const target = document.querySelectorAll('[data-anime]');
const animationClass = 'animate';

function animeScroll() {
    //console.log('teste animação');
    //window.pageYOffset == window.scrollY; // always true
    const windowTop = window.scrollY + (window.innerHeight * 3) / 4;
    target.forEach(function(element) {
        if((windowTop) > element.offsetTop) {
            element.classList.add(animationClass);
        } else {
            element.classList.remove(animationClass);
        }
    })
}

animeScroll();

if (target.length) {
    window.addEventListener('scroll', debounce(function() {
        animeScroll();
        console.log('testando');
}, 200))}


/*const item = document.querySelectorAll("data-anime");
const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;
    item.forEach(element => {
        if(windowTop) > element.offsetTop){
            element.classList.add('animate');
        } else {
            element.classList.remove('animate');
        }
    });
};
animeScroll();

window.addEventListener("scroll", () => {
    animeScroll();
})*/
