# Context Window Budgeter

Select ordered text chunks within a caller-specified approximate token budget.

```bash
cat chunks.json | python tool.py
python -m unittest -v
```

Token estimates are character-based approximations. Use a model-specific tokenizer when exact provider token counts are required.
