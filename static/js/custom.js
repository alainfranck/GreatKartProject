$(document).ready(function () {
    
    $('.d-icon-plus').click(function (e) {
        e.preventDefault();
        var inc_value = $(this).closest('.product-data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;

        if (value < 10)
        {
            value++;
            $(this).closest('.product-data').find('.qty-input').val(value);
        }
    });

});