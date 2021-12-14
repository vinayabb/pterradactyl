import unittest
from pterradactyl.commands.env import EnvCommand
from mock import patch
import pytest


class TestEnvCommands(unittest.TestCase):

    def test_env_commands(self):
        with patch('pterradactyl.commands.manifest.ManifestCommand.__init__') as base:
            with patch('pterradactyl.commands.env.ManifestCommand') as manifest:
                base.return_value = None
                command = EnvCommand(manifest())
                manifest.assert_called_with()
                self.assertListEqual(command.subcommands, ["new", "list", "select", "delete"])
