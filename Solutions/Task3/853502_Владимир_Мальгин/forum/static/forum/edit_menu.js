function sendMessage() {
    let messageId = $('#editMenuMessageId').val();
    let themeId = $('#editMenuThemeId').val();
    let text = $('#editMenuTextArea').val();
    console.log(text);
    if (messageId) {
        $.ajax({
            url: '/forum/message/?messageId=' + messageId + '&themeId=' + themeId,
            type: 'update',
            data: text,
            success: (data, status) => {
                location.reload()
            }
        });
    } else {
        $.ajax({
            url: '/forum/message/?themeId=' + themeId,
            type: 'post',
            data: text,
            success: (data, status) => {
                location.reload()
            }
        });
    }
}
