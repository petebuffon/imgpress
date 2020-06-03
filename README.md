imgpress
========

A utility for encoding and compressing images for optimal web use.

## Usage

Pass in at least an input file image format.

Resize test.jpeg to 1000 x 1000, set quality to 75, and save file as test-1000.jpeg:

```
$ imgpress test.jpeg -f JPEG -r 1000 1000 -q 75 -o test-1000.jpeg
```

Resize test.jpeg to 1000 wide while preserving aspect ratio, encode to WEBP format, and set quality to 65:

```
$ imgpress image.jpeg -f WEBP -r 1000 0 -q 65
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone `
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
