class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder clean = new StringBuilder();

        for (char i : s.toCharArray()) {
            if (Character.isLetterOrDigit(i)) {
                clean.append(Character.toLowerCase(i));

            }
        }

        String forward = clean.toString();
        String backward = clean.reverse().toString();

        return forward.equals(backward);
    }
}
