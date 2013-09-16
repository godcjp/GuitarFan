$(".gt-tabs-hot, .gt-tabs-new").hover(
    function () {
        $(this).find('.icon').addClass("animated active rotateIn");
        $(this).find('h4').addClass("animated active fadeInRight");
    },
    function () {
        $(this).find('.icon').removeClass("animated active rotateIn");
        $(this).find('h4').removeClass("animated active fadeInRight");
    }
);

$(".gt-styles, .gt-tags").hover(
    function () {
        $(this).find('h4').addClass("animated active fadeIn");

    },
    function () {
        $(this).find('h4').removeClass("animated active fadeIn");
    }
);

$(function() {
    $('.gt-landing .input-group').removeClass("hidden");
    $('.gt-landing .input-group').addClass("animated fadeInDown");
});