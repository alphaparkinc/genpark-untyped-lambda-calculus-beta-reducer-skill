from client import LambdaInterpreter

def main():
    print("=== Untyped Lambda Calculus Beta Reducer ===")
    interp = LambdaInterpreter()
    res = interp.parse_eval_simple("((lambda x: x) y)")
    print("Reduction Result:", res)
    assert res["normal_form"] == "y"
    assert res["is_reduced"] is True

    print("Lambda Calculus Beta Reducer verified successfully!")

if __name__ == "__main__":
    main()
