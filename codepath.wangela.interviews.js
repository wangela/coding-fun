inputArray = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]];

function spiralOrder(A) {
    var top = 0;
    var bottom = A.length;
    var left = 0;
    var right = A[0].length;
    var dir = 0;

    var newArray = [];
    var newIndex = 0;

    while (top < bottom && left < right) {
        console.log("while");
        if (dir == 0) {
            for (i = left; i < right; i++) {
                newArray[newIndex] = A[top][i];
                console.log("i = " + i + ", push " + newArray[newIndex]);
                newIndex++;
            }
            top++;
            console.log("top = " + top);
            dir = 1;
        } else if (dir == 1) {
            for (j = top; j < bottom; j++) {
                newArray[newIndex] = A[j][right - 1];
            console.log("j = " + j + ", push " + newArray[newIndex]);
                newIndex++;
            }
            right--;
            dir = 2;
        } else if (dir == 2) {
            for (k = (right - 1); k >= left; k--) {
                newArray[newIndex] = A[bottom - 1][k];
                newIndex++;
            }
            bottom--;
            dir = 3;
        } else if (dir == 3) {
            for (l = (bottom - 1); l >= top; l--) {
                newArray[newIndex] = A[l][left];
                newIndex++;
            }
            left++;
            dir = 0;
        }
    }
    return newArray;
}

spiralOrder(inputArray);

function coverPoints(A, B) {
    var len = A.length;
    var xDist = 0;
    var yDist = 0;
    var step = 0;

    for (i = 0; i < (len - 1); i++) {
        xDist = Math.abs(A[i+1] - A[i]);
        yDist = Math.abs(B[i+1] - B[i]);
        step += Math.max(xDist, yDist);
    }

    return step;
}

function prettyPrint(A) {
    var dim = (2*(A - 1)) + 1;
    var sqArray = [];
    var dir = 0;
    var top = 0;
    var right = dim;
    var bottom = dim;
    var left = 0;

    while (A > 0 && bottom > top) {
        if (dir == 0) {
            for (i = left; i < right; i++) {
                sqArray[top][i] = A;
            }
            top++;
            dir = 1;
        } else if (dir == 1) {
            for (j = top; j < bottom; j++) {
                sqArray[j][right] = A;
            }
            right--;
            dir = 2;
        } else if (dir == 2) {
            for (i = right - 1; i >= left; i--) {
                sqArray[i][bottom] = A;
            }
            bottom--;
            dir = 3;
        } else if (dir == 3) {
            for (j = bottom - 1; j >= top; j--) {
                sqArray[j][left] = A;
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