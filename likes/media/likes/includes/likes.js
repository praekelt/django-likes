function like(click_selector, url, replace_selector) {
    $(click_selector).click(function() {
        $.ajax({
            url: url,
            success: function(html){
                $(replace_selector).replaceWith(html);
            }
        });
        return false;
    });
}
