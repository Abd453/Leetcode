/**
 * @param {any} val
 * @returns {Object} An object with testing functions
 */
function expect(val) {
    return {
        /**
         * Checks if the value is equal to the given value.
         * @param {any} val2 - The value to compare with
         * @throws {Error} If the values are not equal
         * @returns {boolean} True if the values are equal
         */
        toBe: function(val2) {
            if (val !== val2) throw new Error("Not Equal");
            return true;
        },
        /**
         * Checks if the value is not equal to the given value.
         * @param {any} val2 - The value to compare with
         * @throws {Error} If the values are equal
         * @returns {boolean} True if the values are not equal
         */
        notToBe: function(val2) {
            if (val === val2) throw new Error("Equal");
            return true;
        }
    };
}

/**
 * Example usage:
 */
try {
    expect(5).toBe(5); // No error, because 5 is equal to 5
    console.log("Test passed: 5 is equal to 5");

    expect(5).notToBe(5); // Throws "Equal" error, because 5 is equal to 5
} catch (error) {
    console.error(error.message);
}
