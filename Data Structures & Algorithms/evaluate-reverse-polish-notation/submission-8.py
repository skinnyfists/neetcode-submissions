class Solution:
    OPERATORS = {"+", "-", "*", "/"}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(self._eval_operator(token, op1, op2))
            else:
                stack.append(int(token))
        return stack[0]

    def _eval_operator(self, operator: str, op1: int, op2: int) -> int:
        match operator:
            case "+":
                return op1 + op2
            case "-":
                return op1 - op2
            case "*":
                return op1 * op2
            case "/":
                return int(op1 / op2)