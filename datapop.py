import click


@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.option('-f', is_flag=True, help="Mark this command as fun")
@click.argument('country')
# @click.password_option()
def cli(verbose,name,f,country):
	"""This is an example script to learn Click"""
	if verbose:
		click.echo("This here is verbose content.")
	click.echo('hello {0}'.format(country))
	for n in name:
		click.echo("Bye {0}".format(n))
	click.echo("This is " + ("fun" if f else "not fun") + "!")
		# click.echo('We received {0} as password.'.format(password))