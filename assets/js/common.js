// aHR0cHM6Ly9naXRodWIuY29tL2x1b3N0MjYvYWNhZGVtaWMtaG9tZXBhZ2U=
$(function () {
    lazyLoadOptions = {
        scrollDirection: 'vertical',
        effect: 'fadeIn',
        effectTime: 300,
        placeholder: "",
        onError: function(element) {
            console.log('[lazyload] Error loading ' + element.data('src'));
        },
        afterLoad: function(element) {
            if (element.is('img')) {
                // remove background-image style
                element.css('background-image', 'none');
                element.css('min-height', '0');
            } else if (element.is('div')) {
                // set the style to background-size: cover; 
                element.css('background-size', 'cover');
                element.css('background-position', 'center');
            }
        }
    }

    $('img.lazy, div.lazy:not(.always-load)').Lazy({visibleOnly: true, ...lazyLoadOptions});
    $('div.lazy.always-load').Lazy({visibleOnly: false, ...lazyLoadOptions});

    $('[data-toggle="tooltip"]').tooltip()

    var $grid = $('.grid').masonry({
        "percentPosition": true,
        "itemSelector": ".grid-item",
        "columnWidth": ".grid-sizer"
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });

    $(".lazy").on("load", function () {
        $grid.masonry('layout');
    });

    var $lightbox = $('#edu-lightbox');
    if ($lightbox.length) {
        function closeEducationLightbox() {
            $lightbox.attr('hidden', true);
            $lightbox.find('img').attr({ src: '', alt: '' });
            $lightbox.find('figcaption').text('');
        }

        $(document).on('click', '.education-photo', function (event) {
            event.preventDefault();
            event.stopPropagation();
            var $photo = $(this);
            var caption = $photo.data('caption') || '';
            $lightbox.find('img').attr({
                src: $photo.data('full') || $photo.find('img').attr('src'),
                alt: caption
            });
            $lightbox.find('figcaption').text(caption);
            $lightbox.removeAttr('hidden');
        });

        $lightbox.on('click', function (event) {
            if (event.target === this || $(event.target).closest('.edu-lightbox-close').length) {
                closeEducationLightbox();
            }
        });

        $(document).on('keydown', function (event) {
            if (event.key === 'Escape' && !$lightbox.attr('hidden')) {
                closeEducationLightbox();
            }
        });

        $('.education-entry.has-photos').on('click', function (event) {
            if ($(event.target).closest('.education-photos').length) {
                return;
            }
            if (window.matchMedia('(hover: none)').matches) {
                $(this).toggleClass('is-open').siblings('.education-entry').removeClass('is-open');
            }
        });
    }
})
