#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Text Analyzer Script"""

def analyze_text(text):
    words = text.split()
    chars = len(text)
    words_count = len(words)
    vowels = sum(1 for char in text.lower() if char in 'aeiou')
    
    return {
        'characters': chars,
        'words': words_count,
        'vowels': vowels
    }

if __name__ == "__main__":
    sample_text = "Hello World"
    result = analyze_text(sample_text)
    print(f"Text: {sample_text}")
    print(f"Analysis: {result}")
