d = document.getElementById('flexCheckIndeterminate')

d.addEventLister('click',function () {
  var xhr = new XMLHttpRequest();

  xhr.onload = () => {
    // process response
    if (xhr.status == 200) {
        // parse JSON data

    } else {

    };

  xhr.open('GET', 'website_url/add?id={{ t }}');

  xhr.send();
};
})
