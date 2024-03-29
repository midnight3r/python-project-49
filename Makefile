install: #poetry install
	poetry install
brain-games: #run brain-games
	poetry run brain-games
brain-even: #run brain-even
	poetry run brain-even
brain-calc: #run brain-calc
	poetry run brain-calc
brain-gcd: #run brain-gcd
	poetry run brain-gcd
brain-progression: #run brain-progression
	poetry run brain-progression
brain-prime: #run brain-prime
	poetry run brain-prime
build: #poetry build
	poetry build
publish: #poetry publish
	poetry publish --dry-run
package-install: #install package
	python3 -m pip install --user dist/*.whl
package-reinstall: #reinstall
	pip install --user --force-reinstall dist/*.whl
lint: #lint check
	poetry run flake8 brain_games
