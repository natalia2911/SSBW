
const darkSwitch = document.getElementById('darkSwitch');
window.addEventListener('load', () => {
  if (darkSwitch) {
    initTheme();
    darkSwitch.addEventListener('change', () => {
      resetTheme();
    });
  }
});

  function initTheme() {
    const darkThemeSelected =
      localStorage.getItem('darkSwitch') !== null &&
      localStorage.getItem('darkSwitch') === 'dark';
    darkSwitch.checked = darkThemeSelected;
    darkThemeSelected ? document.body.setAttribute('data-theme', 'dark') :
      document.body.removeAttribute('data-theme');
  
  }

  function resetTheme() {
    if (darkSwitch.checked) {
      document.body.setAttribute('data-theme', 'dark');
      localStorage.setItem('darkSwitch', 'dark');
      $("body > div").css("background-color", "blue");
      $("li").css("background-color", "black");
      $("header > nav").css("background-color", ' black');
 $("span").css("color", 'white ');
      $("container-fluid").css("background-color", "black");
      $("a").css("color", "white");
    } else {
      document.body.removeAttribute('data-theme');
      localStorage.removeItem('darkSwitch');
      $("body > div").css("background-color", 'grey  ');
      $("li").css("background-color", ' transparent');
      $("header > nav").css("background-color", ' #E9EDF4');
      $("a").css("color", 'white ');
$("span").css("color", 'black ');
      $("footer > div").css( "background-color"," blue ");
    }
  }