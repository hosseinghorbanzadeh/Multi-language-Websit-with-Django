/*
* Template Name: PRO Card - Material Resume / CV / vCard Template
* Author: lmpixels
* Author URL: http://themeforest.net/user/lmpixels
* Version: 1.0
*/

(function($) {
    "use strict";

    // Adjust subpages height based on current section
    function subpages_resize() {
        var currentPage = $('.pt-page-current');
        if(currentPage.length) {
            var subpagesHeight = currentPage.height();
            $(".subpages").height(subpagesHeight + 50);
        }
    }

    // Portfolio subpage filters
    function portfolio_init() {
        var portfolio_grid = $('#portfolio_grid'),
            portfolio_filter = $('#portfolio_filters');

        if (portfolio_grid.length) {
            portfolio_grid.shuffle({
                speed: 450,
                itemSelector: 'figure'
            });

            $('.site-main-menu').on("click", "a", function () {
                portfolio_grid.shuffle('update');
            });

            portfolio_filter.on("click", ".filter", function (e) {
                e.preventDefault();
                portfolio_grid.shuffle('update');
                $('#portfolio_filters .filter').parent().removeClass('active');
                $(this).parent().addClass('active');
                portfolio_grid.shuffle('shuffle', $(this).attr('data-group'));
                setTimeout(subpages_resize, 500);
            });
        }
    }

    // Contact form validator
    $(function () {
        $('#contact-form').validator();

        $('#contact-form').on('submit', function (e) {
            if (!e.isDefaultPrevented()) {
                var url = "contact_form/contact_form.php";

                $.ajax({
                    type: "POST",
                    url: url,
                    data: $(this).serialize(),
                    success: function (data) {
                        var messageAlert = 'alert-' + data.type;
                        var messageText = data.message;

                        var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissable">' +
                                       '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' +
                                       messageText + '</div>';
                        if (messageAlert && messageText) {
                            $('#contact-form').find('.messages').html(alertBox);
                            $('#contact-form')[0].reset();
                        }
                    }
                });
                return false;
            }
        });
    });

    // Hide Mobile menu
    function mobileMenuHide() {
        if ($(window).width() < 1024) {
            $('#site_header').addClass('mobile-menu-hide');
        }
    }

    // Animate Skills bars
    function animateSkills() {
        $('.skill-percentage').each(function() {
            var $this = $(this);
            var percentage = $this.data('percentage');
            $this.css({ width: '0%' });
            $this.animate({ width: percentage + '%' }, 1);
        });
    }

    // Trigger skills animation when visible
    function checkSkillsVisible() {
        $('.skills-info').each(function() {
            var top_of_element = $(this).offset().top;
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            if(bottom_of_window > top_of_element) {
                animateSkills();
            }
        });
    }

    // On Window load & Resize
    $(window)
        .on('load', function() {
            $(".preloader").fadeOut("slow");
            subpages_resize();
            checkSkillsVisible();
        })
        .on('resize', function() {
            mobileMenuHide();
            setTimeout(subpages_resize, 500);
        })
        .scroll(function () {
            if ($(window).scrollTop() < 20) {
                $('.header').removeClass('sticked');
            } else {
                $('.header').addClass('sticked');
            }
            checkSkillsVisible();
        })
        .scrollTop(0);

    // On Document Load
    $(document).on('ready', function() {
        // Initialize Portfolio grid
        var $portfolio_container = $("#portfolio-grid");
        $portfolio_container.imagesLoaded(function () {
            setTimeout(function() { portfolio_init(); }, 500);
        });

        // Portfolio hover effect init
        $('#portfolio_grid > figure').each(function() { $(this).hoverdir(); });

        // Blog grid init
        setTimeout(function() { $(".blog-masonry").masonry(); }, 500);

        // Mobile menu toggle
        $('.menu-toggle').on("click", function () {
            $('#site_header').toggleClass('mobile-menu-hide');
        });

        // Mobile menu hide on main menu item click
        $('.site-main-menu').on("click", "a", function () {
            mobileMenuHide();
        });

        // Sidebar toggle
        $('.sidebar-toggle').on("click", function () {
            $('#blog-sidebar').toggleClass('open');
        });

        // Testimonials Slider
        $(".testimonials.owl-carousel").owlCarousel({
            nav: true,
            items: 3,
            loop: false,
            navText: false,
            margin: 25,
            responsive : {
                0 : { items: 1 },
                480 : { items: 1 },
                768 : { items: 2 },
                1200 : { items: 2 }
            }
        });

        // Text rotation
        $('.text-rotation').owlCarousel({
            loop: true,
            dots: false,
            nav: false,
            margin: 0,
            items: 1,
            autoplay: true,
            autoplayHoverPause: false,
            autoplayTimeout: 3800,
            animateOut: 'zoomOut',
            animateIn: 'zoomIn'
        });

        // Lightbox init
        $('body').magnificPopup({
            delegate: 'a.lightbox',
            type: 'image',
            removalDelay: 300,
            mainClass: 'mfp-fade',
            image: { titleSrc: 'title', gallery: { enabled: true } },
            iframe: {
                markup: '<div class="mfp-iframe-scaler">'+
                        '<div class="mfp-close"></div>'+
                        '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
                        '<div class="mfp-title mfp-bottom-iframe-title"></div>'+
                      '</div>',
                patterns: {
                    youtube: { index: 'youtube.com/', id: null, src: '%id%?autoplay=1' },
                    vimeo: { index: 'vimeo.com/', id: '/', src: '//player.vimeo.com/video/%id%?autoplay=1' },
                    gmaps: { index: '//maps.google.', src: '%id%&output=embed' }
                },
                srcAction: 'iframe_src'
            },
            callbacks: {
                markupParse: function(template, values, item) {
                    values.title = item.el.attr('title');
                }
            }
        });

        $('.ajax-page-load-link').magnificPopup({
            type: 'ajax',
            removalDelay: 300,
            mainClass: 'mfp-fade',
            gallery: { enabled: true }
        });

        // Form Controls
        $('.form-control')
            .val('')
            .on("focusin", function() { $(this).parent('.form-group').addClass('form-group-focus'); })
            .on("focusout", function() {
                if($(this).val().length === 0) {
                    $(this).parent('.form-group').removeClass('form-group-focus');
                }
            });

        // Google Maps
        $("#map").googleMap();
        $("#map").addMarker({ address: "15 avenue des champs Elysées 75008 Paris" });
    });

})(jQuery);
