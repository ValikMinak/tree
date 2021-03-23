$(document).ready(function () {
    // $('.back').css({'color': 'red'})
    a = $('.query_input').data('id')

});

// События

// mouse ----- click, dblclick, mouseenter, mouseleave

// keyboard ------ keypress keydown keyup

// form ----- change submit

// window resize scroll


$(document).ready(function () {
    $(window).resize(function () {
        let width = $(this).width()
        let height = $(this).height()
        // console.log(width, height)
    })
})

$(document).ready(function () {
    $('.query_input').on('keyup', function () {
        let value = $(this).val()
        // console.log(value)
    })

    $('.query_btn').on('click', function () {
        // console.log('HEY')
    })
})


// Show/Hide elements

// css hide() show(timer) delay(time) attr()
// animate() fadeIn fadeOut

$(document).ready(function () {
    let input = $('.query_input').on('keyup', function () {
        let value = $(this).val()
        // console.log(value)
    })
    let btn = $('.query_btn').on('click', function () {
        // input.hide(1000).delay(2000).show(1000)
        // console.log(input.attr('value'))
    })
})


// addClass removeClass, toggleClass

$(document).ready(function () {
    let btn = $('.query_btn')
    $('.query_hover').hover(function () {
        btn.addClass('change_color')
        $(this).on('click', function () {
            btn.removeClass('change_color')
        })
    })
})

// text() html() append() prepend() after()

$(document).ready(function () {
    let btn = $('.query_btn')
    let text = $('.query_hover')
    btn.on('click', function () {
        text.text('Новый текст')
    })
})

$(document).ready(function () {
    let HTML = '<li>Кастомная ссылка</li>'
    let text = $('.query_hover')
    let btn = $('.query_btn')
    // btn.on('click', function () {
    //     text.html(HTML)
    // })
    btn.on('click', function () {
        text.append(HTML)
    })

})


// wrap() unwrap()
$(document).ready(function () {
    let text = $('.query_hover')
    // text.wrap("<div>wrap</div>")
})