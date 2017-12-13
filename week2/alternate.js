    var __input_stdin = "";
    var __input_stdin_array = "";
    var __input_currentline = 0;


    __input_stdin_array = __input_stdin.split("\n");
    var n = parseInt(__input_stdin_array[__input_currentline].trim(), 10);
    __input_currentline += 1;
    for (var i = 0; i<n;i++) {
        var _line = __input_stdin_array[__input_currentline].trim();
        __input_currentline += 1;
        var degrees = -1;
        var c = _line;
        var individual_lengths = 0;

        if (c.length % 2 == 1) {
            process.stdout.write(degrees+"\n");
            continue;
        } else {
          individual_lengths = c.length / 2;
          degrees = 0;
        }

        var a = c.slice(0, individual_lengths);
        var b = c.slice(individual_lengths, c.length);
        var dict_b = new Map();

        for (var character in b) {
          if (dict_b.has(character)) {
            var value = dict_b.get(character);
            value++;
            dict_b.set(character, value);
          } else {
            dict_b.set(character, 1);
          }
        }

        for (var char in a) {
          if (dict_b.has(char)) {
            var value = dictb.get(char);
            if (value > 1) {
              value--;
              dict_b.set(char, value);
            } else if (value == 1) {
              dict_b.delete(char);
            }
          } else {
            degrees++;
          }
        }

        process.stdout.write(degrees+"\n");
    }
