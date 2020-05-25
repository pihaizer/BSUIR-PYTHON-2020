$('#editMenuThemeId').val(themeId);

function editMessage(messageId) {
    let editMenuTextArea = $('#editMenuTextArea');
    editMenuTextArea.text($('#messageText' + messageId)[0].innerText);
    $('#containerToHide' + messageId).css('display', 'none');
    let messageEditContainer = $('#editMessageContainer' + messageId);
    messageEditContainer.append($('#editMenu'));
    $('#editMenuMessageId').val(messageId);
}

function deleteMessage(messageId) {
    $.ajax({
        url: '/forum/message/?messageId=' + messageId,
        type: 'delete',
        success: (data, status) => {
            location.reload()
        }
    });
}