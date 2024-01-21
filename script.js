(function() {
    var lengthEl = document.getElementById('length');
    var includeLettersEl = document.getElementById('include-letters');
    var includeNumbersEl = document.getElementById('include-numbers');
    var includeSymbolsEl = document.getElementById('include-symbols');
    var generateButton = document.getElementById('generate-button');
    var passwordEl = document.getElementById('password');

    function generatePassword() {
        var length = parseInt(lengthEl.value);
        var includeLetters = includeLettersEl.checked;
        var includeNumbers = includeNumbersEl.checked;
        var includeSymbols = includeSymbolsEl.checked;
        var characters = '';

        if (includeLetters) {
            characters += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        }
        if (includeNumbers) {
            characters += '0123456789';
        }
        if (includeSymbols) {
            characters += '!@#$%^&*()_+~`|}{[]\:;?><,./-=';
        }

        var password = '';
        for (var i = 0; i < length; i++) {
            password += characters.charAt(Math.floor(Math.random() * characters.length));
        }

        passwordEl.value = password;
    }

    generateButton.addEventListener('click', generatePassword);
})();
