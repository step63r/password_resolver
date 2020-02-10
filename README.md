# password_resolver

## Description

Show password depends on your environment variables and hint string from command line argument.

## Requirement

- Python 3.7.4

## Usage

Add environment variable of your password like this.

| KEY  | VALUE    |
|:---- |:-------- |
| PW1  | p@ssw0rd |
| PW2  | mypass   |
| PW3  | hogehoge |

Create password list with environment variables.

```
P@ssw0rd -> 'f\"{PW1.capitalize()}\"'
MYPASS -> 'f\"{PW2.upper()}\"'
```

Execute script.

```
$ python password_resolver.py 'f\"{PW1.capitalize()}\"'
P@ssw0rd
```

## Install

Fork and clone this repository.

```
$ git clone https://github.com/yourname/password_resolver.git
```

## Contribution

1. Fork this repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create new Pull Request

## License

## Author

[minato](https://blog.minatoproject.com/)
