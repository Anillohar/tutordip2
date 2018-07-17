
/*Wow Animation*/
new WOW().init();

/*Header Fixed */

$(window).scroll(function () {
    var sticky = $('.header'),
        scroll = $(window).scrollTop();                   

    if (scroll >= 100) sticky.addClass('fixed');
    else sticky.removeClass('fixed');
});

/*Testimonial Slider*/

$('#testimonial_slider .owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    nav: true,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    autoplay:true,
    autoplayTimeout: 5000,
    dots: false,
    responsive:{
        0:{items:1},
        600:{items:1},
        1000:{items:1}
    }
});

/*Overview Slider*/

$('#overview_slider .owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    nav:true,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    autoplay:true,
    autoplayTimeout:5000,
    responsive:{
        0:{items:1},
        600:{items:1},
        1000:{items:1}
    }
    });


$(".navbar li.dropdown .arrow_menu").on("click", function (a) {
    a.stopPropagation();
    $(this).siblings(".dropdown-menu").slideToggle()
}), $(".navbar li.dropdown .arrow_menu").on("click", function (e) {
    e.stopImmediatePropagation()
});


/*Timer*/

var a = 0;
        function formatter(value, options) {
            return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
        }
        $(window).scroll(function () {

            var oTop = $('.categorie_timer').offset().top - window.innerHeight;
            if (a == 0 && $(window).scrollTop() > oTop) {
                $('.timer').each(function () {
                    var $this = $(this),
                      countTo = $this.attr('data-count');
                    $({
                        countNum: $this.text()
                    }).animate({

                        countNum: countTo
                    },



                      {

                          duration: 6000,
                          easing: 'swing',
                          step: function () {
                              $this.text(Math.floor(this.countNum));
                          },
                          complete: function () {
                              //console.log(formatter(this.countNum, { decimals: 2 }));
                              $this.text(formatter(this.countNum,{decimals:0}));
                              //alert('finished');
                          }

                      });
                });
                a = 1;
            }

        });


/*Isotop*/

$(".js-iso").each(function (a) {
        var i = $(this);
        i.imagesLoaded(function () {
            i.isotope({
                filter: ".blog-item",
                itemSelector: ".js-iso-item",
                layoutMode: "masonry",
                masonry: {
                    columnWidth: ".js-iso-item"
                }
            })
        })
    });


/*Zoom Gallery 1*/
$(".zoom-gallery").magnificPopup({
    delegate: "a",
    type: "image",
    closeOnContentClick: !1,
    closeBtnInside: !1,
    mainClass: "mfp-with-zoom mfp-img-mobile",
    image: {
        verticalFit: !0
    },
    zoom: {
        enabled: !0,
        duration: 500,
        opener: function(e) {
            return e.find("img")
        }
    },
      
      
    gallery:{enabled:true},
    callbacks: {

    buildControls: function() {
        // re-appends controls inside the main container
        this.contentContainer.append(this.arrowLeft.add(this.arrowRight));
    }

    }
      
});