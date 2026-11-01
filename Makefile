.PHONY: test

test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/design-trends-2027/tests -v
	git diff --check
