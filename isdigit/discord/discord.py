from discord.ext import commands
from ... import isdigit
import typing

_isdigit = isdigit.IsDigit()

class DigitConverter(commands.Converter):
    async def convert(self, ctx, argument) -> typing.Optional[int]:
        if (item := _isdigit.isdigit(argument, return_digit=True)):
            return item
        else:
            raise commands.BadArgument(f'{argument} is not a valid number.')