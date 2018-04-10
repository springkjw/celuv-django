// 검색 기능
$(function() {
  // 검색 창에서 엔터 키 누르면 폼 전송
  $('.search-form input[name=search]').on('input', function(e) {
    if (e.which == 13) {
      e.preventDefault();
      $(this)
        .parent()
        .submit();
    }
  });
});
