window.addEventListener("load", function () {
    (function ($) {
        $(document).ready(function () {


            let a = django.jQuery('.module > table > tbody > .has_original')
            django.jQuery.each(a, function (index, el) {
                item = django.jQuery(el).find(`#id_comments-${index}-is_active`)
                !django.jQuery(item).attr('checked') ? django.jQuery(el).hide() : django.jQuery(el).show()
            })


            django.jQuery('fieldset.module>h2').last()
                .append('<a class="custom_show_btn" style="margin-left: 20px" href="#">Show</a>')
                .on('click', function (e) {
                    e.preventDefault()
                    django.jQuery.each(a, function (index, el) {
                        item = django.jQuery(el).find(`#id_comments-${index}-is_active`)
                        if (!django.jQuery(item).attr('checked') && django.jQuery(el).is(":visible")) {
                            django.jQuery(el).hide()
                        } else {
                            django.jQuery(el).show()
                        }

                    })
                })
        });
    })(django.jQuery);
})