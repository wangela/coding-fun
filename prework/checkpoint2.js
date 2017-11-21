function prettyPrint(A) {
    var dim = (2*(A - 1)) + 1;
    var sqArray = [];
    var dir = 0;
    var top = 0;
    var right = dim - 1;
    var bottom = dim - 1;
    var left = 0;

    for (x = 0; x < dim; x++) {
        sqArray[x] = [];
    }

    while (A > 0 && bottom >= top) {
        if (dir == 0) {
            for (i = left; i <= right; i++) {
                sqArray[top][i] = A;
            }
            top++;
            dir = 1;
        }
        if (dir == 1) {
            for (j = top; j <= bottom; j++) {
                sqArray[j][right] = A;
            }
            right--;
            dir = 2;
        }
        if (dir == 2) {
            for (i = right; i >= left; i--) {
                sqArray[bottom][i] = A;
            }
            bottom--;
            dir = 3;
        }
        if (dir == 3) {
            for (j = bottom; j >= top; j--) {
                sqArray[j][left] = A;
            }
            left++;
            dir = 0;
        }
        A--;
    }

    return sqArray;
}

function prettyPrintWithPrint(A) {
    /*
    Arguments:
      A is a positive integer
    Output:
      A concentric regular pattern in a 2d matrix with "1" at the center and a
      concentric ring around it with the next integer until A is reached.
    */
    var dim = (2*(A - 1)) + 1;
    var sqArray = [];
    var dir = 0;
    var top = 0;
    var right = dim - 1;
    var bottom = dim - 1;
    var left = 0;

    for (x = 0; x < dim; x++) {
        sqArray[x] = [];
    }

    while (A > 0 && bottom >= top) {
        if (dir == 0) {
            for (i = left; i <= right; i++) {
                sqArray[top][i] = A;
                console.log('sqArray[' + top + "][" + i + "] = " + A);
            }
            top++;
            dir = 1;
        }
        if (dir == 1) {
            for (j = top; j <= bottom; j++) {
                sqArray[j][right] = A;
                console.log('sqArray[' + j + "][" + right + "] = " + A);
            }
            right--;
            dir = 2;
        }
        if (dir == 2) {
            for (i = right; i >= left; i--) {
                sqArray[bottom][i] = A;
                console.log('sqArray[' + i + "][" + bottom + "] = " + A);
            }
            bottom--;
            dir = 3;
        }
        if (dir == 3) {
            for (j = bottom; j >= top; j--) {
                sqArray[j][left] = A;
                console.log('sqArray[' + j + "][" + left + "] = " + A);
            }
            left++;
            dir = 0;
        }
        A--;
        console.log("top = " + top + ", bottom = " + bottom);
    }

    console.log(JSON.stringify(sqArray));
    return sqArray;
}
