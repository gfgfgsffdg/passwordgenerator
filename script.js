document.addEventListener('DOMContentLoaded', function() {
    var generateBtn = document.getElementById('generateBtn');
    generateBtn.addEventListener('click', generatePassword);

    function generatePassword() {
        var passwordLength = document.getElementById('length').value;
        var includeNumbers = document.getElementById('includeNumbers').checked;
        var includeSymbols = document.getElementById('includeSymbols').checked;

        var characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        if (includeNumbers) {
            characters += '0123456789';
        }
        if (includeSymbols) {
            characters += '!@#$%^&*()_-+=~`[]{}|:;"<>,.?/';
        }

        var password = '';
        for (var i = 0; i < passwordLength; i++) {
            password += characters.charAt(Math.floor(Math.random() * characters.length));
        }

        document.getElementById('generatedPassword').value = password;
    }
});
