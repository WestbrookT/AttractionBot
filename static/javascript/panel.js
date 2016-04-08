function loadPage(page) {

  $.get('/api/pages/' + page + '/meta', function (data) {
    var response = JSON.parse(data);
    pageItems.$data = response;

    metaItems.meta = response.meta;
  });

}

function showModal(id) {
  $('#' + id).addClass('active');
}



$(document).ready(function () {
  $("#nav").click(function () {
    if (!$("#nav").hasClass("active")) {
      $(this).toggleClass("active");
    }
  });


  $(document).click(function (event) {

    if ($("#nav").hasClass("active")) {
      console.log(event.target);
      if (event.target.id == "body") {
        $("#nav").toggleClass("active");
      }
    }
  });

  $("#main").click(function () {
    if ($("#nav").hasClass("active")) {
      $("#nav").toggleClass("active");
    }
  });

  $(".navdrop").click(function () {
    $(this).siblings("ul").toggleClass("active");
  });

  $(".page-link").click(function () {

    loadPage($(this).html());
  });


  $('.modal').click(function(event) {
  if (event.target.id == 'delete-modal') {

    $(this).removeClass('active');
    $.get("/admin/delete/" + pageItems.pageName);
    window.location = '/admin';
  }
  else if (event.target.id == 'cancel') {
    $(this).removeClass('active');
  }
});
});


var pageItems = new Vue({

  el: '#elements',

  data: {
    pageName: '',
    content: [],
    meta: [],
  },

  created: function() {
    this.addItem();
  },

  methods: {
    addItem: function() {
      this.content.push({
        open: false,
        tag: 'p',
        class: '',
        id: '',
        content: ''
      });
    },
    removeItem: function(index) {
      this.content.splice(index, 1);
    },
    addMeta: function() {
      this.meta.push({
        open: false,
        title: '',
        value: ''
      });
    },
    removeMeta: function(index) {
      this.meta.splice(index, 1);
    },
    dropdown: function(index) {
      this.content[index].open = !this.content[index].open;
      if (this.content[index].open) {
        autosize($('textarea'));
      }
    },
    dropdownMeta: function(index) {
      this.meta[index].open = !this.meta[index].open;
      if (this.meta[index].open) {
        autosize($('textarea'));
      }
    },
    auto: function (index) {
      autosize($('textarea'));
    },
    submit: function() {
      console.log('test');
      if (this.pageName != '') {
        this.meta = metaItems.meta;
        $.post('/admin/create', JSON.stringify(this.$data));
        loadPage(pageItems.pageName);
        window.location = '/admin';
      }
    }
  }

});

var metaItems = new Vue({

  el: '#meta',

  data: {
    meta: []
  },

  created: function() {
    this.addMeta();
  },

  methods: {
    addMeta: function() {
      this.meta.push({
        open: false,
        title: '',
        value: ''
      });
    },
    removeMeta: function(index) {
      this.meta.splice(index, 1);
    },
    auto: function (index) {
      autosize($('textarea'));
    },
    dropdownMeta: function(index) {
      this.meta[index].open = !this.meta[index].open;
      if (this.meta[index].open) {
        autosize($('textarea'));
      }
    }
  }

});
