install: #poetry install
	poetry install
brain-games: #run brain-games
	poetry run brain-games
build: #poetry build
	poetry build
publish: #poetry publish
	poetry publish --dry-run
package-install: #install package
	python3 -m pip install --user dist/*.whl

