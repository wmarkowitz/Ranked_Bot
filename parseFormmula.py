ADD_SYMBOL = "+"
MINUS_SYMBOL = "-"
MULTIPLY_SYMBOL = "*"
DIVISION_SYMBOL = "/"
LEFT_PARENTHESIS_SYMBOL = "("
RIGHT_PARENTHESIS_SYMBOL = ")"
TIER_DIFFERENCE_SYMBOL = "TIER_DIFFERENCE"
POINT_DIFFERENCE_SYMBOL = "POINT_DIFFERENCE"


def recursiveFindClosingSymbol(formula, openingSymbol, closingSymbol):
    if closingSymbol not in formula:
        raise SyntaxError("There was a syntax error in the formula. Ensure that all parentheses are properly closed.")
    firstOpeningSymbol = formula.index(openingSymbol) if openingSymbol in formula else None
    firstClosingSymbol = formula.index(closingSymbol) if closingSymbol in formula else None
    if firstOpeningSymbol is None or firstOpeningSymbol > firstClosingSymbol:
        return firstClosingSymbol
    else:
        charsSeen = firstOpeningSymbol + 1
        substring = formula[charsSeen:]
        nextSubstringBegin = recursiveFindClosingSymbol(substring, openingSymbol, closingSymbol) + charsSeen + 1
        nextSubstring = formula[nextSubstringBegin:]
        result = nextSubstringBegin + recursiveFindClosingSymbol(nextSubstring, openingSymbol, closingSymbol)
        return result


def evaluateFormula(formula, tierDifference, pointDifference):
    formulaArray = formula.split(' ')
    formulaArray = [el for el in formulaArray if el != ""]
    return int(evaluateFormulaArray(formulaArray, tierDifference, pointDifference))


def evaluateFormulaArray(formula, tierDifference, pointDifference):
    print("eval", formula)
    if len(formula) == 1:
        val = formula[0]
        if val.replace('.', '', 1).replace('-', '', 1).isdigit():
            return float(val)
        if val == TIER_DIFFERENCE_SYMBOL:
            return tierDifference
        if val == POINT_DIFFERENCE_SYMBOL:
            return pointDifference
        else:
            raise SyntaxError("There was a syntax error in the formula. Please check this and try again. Are there any missing spaces?")
    leftParenthesisIndex = formula.index(LEFT_PARENTHESIS_SYMBOL) if LEFT_PARENTHESIS_SYMBOL in formula else None
    if leftParenthesisIndex is not None:
        associatedRightIndex = leftParenthesisIndex + 1 + \
                               recursiveFindClosingSymbol(formula[leftParenthesisIndex + 1:], LEFT_PARENTHESIS_SYMBOL,
                                                          RIGHT_PARENTHESIS_SYMBOL)
        replacedTerm = str(
            evaluateFormulaArray(formula[leftParenthesisIndex + 1:associatedRightIndex], tierDifference, pointDifference))
        newFormula = formula[:leftParenthesisIndex] + [replacedTerm] + formula[associatedRightIndex + 1:]
        return evaluateFormulaArray(newFormula, tierDifference, pointDifference)
    addIndex = formula.index(ADD_SYMBOL) if ADD_SYMBOL in formula else None
    if addIndex is not None:
        return evaluateFormulaArray(formula[:addIndex], tierDifference, pointDifference) \
               + evaluateFormulaArray(formula[(addIndex + 1):], tierDifference, pointDifference)
    minusIndex = formula.index(MINUS_SYMBOL) if MINUS_SYMBOL in formula else None
    if minusIndex is not None:
        return evaluateFormulaArray(formula[:minusIndex] + [ADD_SYMBOL, "-1", MULTIPLY_SYMBOL] + formula[(minusIndex + 1):],
                                    tierDifference, pointDifference)
    multiplyIndex = formula.index(MULTIPLY_SYMBOL) if MULTIPLY_SYMBOL in formula else None
    divisionIndex = formula.index(DIVISION_SYMBOL) if DIVISION_SYMBOL in formula else None
    if multiplyIndex is not None and divisionIndex is not None:
        if multiplyIndex < divisionIndex:
            divisionIndex = None
        else:
            multiplyIndex = None
    if multiplyIndex is not None:
        return evaluateFormulaArray(formula[:multiplyIndex], tierDifference, pointDifference) \
               * evaluateFormulaArray(formula[(multiplyIndex + 1):], tierDifference, pointDifference)
    if divisionIndex is not None:
        return evaluateFormulaArray(formula[:divisionIndex], tierDifference, pointDifference) \
               / float(evaluateFormulaArray(formula[(divisionIndex + 1):],
                                            tierDifference, pointDifference))
