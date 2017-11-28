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

function findCount(A, B) {
    var lowIndex = 0;
    var highIndex = 0;

    function oneWay(C, D, highFirst) {
        var low = 0;
        var high = C.length - 1;
        var result = -1;

        while (low <= high) {
            var mid = Math.floor(low + (high - low)/2);
            if (C[mid] == D) {
                result = mid;
                if (highFirst) {
                    low = mid + 1;
                }
                else high = mid - 1;
            } else if (D < C[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return result;
    }

    highIndex = oneWay(A, B, true);

    if (highIndex == -1) {
        return 0;
    } else {
        lowIndex = oneWay(A, B, false);
    }

    return highIndex - lowIndex + 1;
}

function findMin (A) {
    var n = A.length;
    var low = 0;
    var high = n - 1;

    while (low <= high) {
        if (A[low] <= A[high]) return low; // Case 1

        var mid = Math.floor((high + low)/2);
        console.log("mid = " + mid);
        var next = (mid + 1) % n;
        var prev = (mid + n - 1) % n;

        if ((A[mid] <= A[next]) && (A[mid] <= A[prev])) { // Case 2
            console.log("case 2");
            return mid;
        } else if (A[mid] <= A[high]) { // Case 3
            console.log("case 3");
            high = mid - 1;
        } else if (A[mid] >= A[low]) { // Case 4
            console.log("case 4")
            low = mid + 1;
        }
    }

    console.log("oops2");
}

function MinHeap() {
    this.content = [];
}

MinHeap.prototype = {
    push: function(element) {
        this.content.push(element);
    },

    pop: function() {
        var result = this.content[0];
        var end = this.content.pop();

        if (this.content.length > 0) {
            this.content[0] = end;
            this.sinkDown(0);
        }

        return result;
    },

    remove: function(node) {
        var length = this.content.length;

        for (i = 0; i < length; i++) {
            if (this.content[i] != node) continue;

            var end = this.content.pop();

            if (i == length - 1) break;

            this.content[i] = end;
            this.bubbleUp(i);
            this.sinkDown(i);
            break;
        }
    },

    size: function() {
        return this.content.length;
    },

    bubbleUp: function(n) {
        var element = this.content[n];

        while (n > 0) {
            var parentN = Math.floor((n + 1)/2) - 1
            var parent = this.content[parentN];

            if (element < parent) {
                this.content[parentN] = element;
                this.content[n] = parent;
                n = parentN;
            }
        }
    },

    sinkDown: function(n) {
        var length = this.content.length;
        var element = this.content[n];

        while (true) {
            var child2N = (n + 1) * 2;
            var child1N = child2N - 1;

            var swap = null;

            if (child1N < length) {
                var child1 = this.content[child1N];

                if (child1 > element) {
                    swap = child1N;
                }
            }

            if (child2N < length) {
                var child2 = this.content[child2N];

                if (child2 > (swap == null ? element : child1)) {
                    swap = child2N;
                }
            }

            if (swap == null) break;

            this.content[n] = this.content[swap];
            this.content[swap] = element;
            n = swap;
        }
    }
}

function kthSmallest(A, k) {
    var heap = new MinHeap(function(x) {return x});
    var result = -1;

    for (i = 0; i < k; i++) {
        heap.push(A[i]);
        heap.bubbleUp(heap.size - 1);
    }

    for (i = k; i < A.length; i++) {
        heap.push(A[i]);
        heap.bubbleUp(heap.size - 1);
        heap.remove(k);
    }

    for (i = 0; i < k; i++) {
        result = heap.pop();
    }

    return result;
}
