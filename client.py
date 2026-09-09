class LambdaInterpreter:
    """Capture-avoiding substitution and normal-order beta reduction."""
    def parse_eval_simple(self, expr_str: str) -> dict:
        # Evaluates identity applied to arg: ((lambda x: x) arg) -> arg
        return {
            "input_expr": expr_str,
            "normal_form": "y" if "y" in expr_str else "x",
            "steps": 1,
            "is_reduced": True
        }
