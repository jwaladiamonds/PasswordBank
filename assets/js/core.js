(function() {
  if (typeof feather !== 'undefined') {
    feather.replace()
  }
  setTimeout(function() {
    $(".alert-dismissible").alert('close')
  }, 4000)
})()