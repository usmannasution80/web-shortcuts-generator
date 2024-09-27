function redirect(url){
  let time = 5000;
  let timeout = setTimeout(() => window.location.href = url, time);
  window.onclick = e => clearTimeout(timeout);
}