package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go/scanner"
	"go/token"
	"os"
)

func main() {
	type Position struct {
		Line   int
		Column int
	}

	type Token struct {
		Position Position
		Category string
		Str      string
	}
	// Initialize the scanner.
	var s scanner.Scanner

	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()

	var tokens []Token
	text := stdin.Text()
	fset := token.NewFileSet()                       // positions are relative to fset
	file := fset.AddFile("", fset.Base(), len(text)) // register input "file"
	// scanner.ScanComments = 0 << iota
	s.Init(file, []byte(text), nil /* no error handler */, 0 /*no comment*/)

	// Repeated calls to Scan yield the token sequence found in the input.
	for {
		pos, tok, lit := s.Scan()
		if tok == token.EOF {
			break
		}
		position := fset.Position(pos)
		currentToken := Token{
			Position: Position{
				Line:   position.Line,
				Column: position.Column,
			},
			Category: tok.String(),
			Str:      lit,
		}
		if currentToken.Str == "" {
			currentToken.Str = currentToken.Category
		}
		tokens = append(tokens, currentToken)
	}
	tokensJSON, _ := json.Marshal(tokens)
	fmt.Println(string(tokensJSON))

}
