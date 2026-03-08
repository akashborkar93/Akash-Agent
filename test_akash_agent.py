#!/usr/bin/env python3
"""
Unit tests for Akash-Agent DevOps Testing Framework
"""

import unittest
import json
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the current directory to the path so we can import akash_agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from akash_agent import AkashAgent


class TestAkashAgent(unittest.TestCase):
    """Test cases for the AkashAgent class."""

    def setUp(self):
        """Set up test fixtures."""
        self.agent = AkashAgent()

    def test_initialization(self):
        """Test agent initialization with default config."""
        self.assertIsInstance(self.agent.config, dict)
        self.assertIn('environment', self.agent.config)
        self.assertEqual(self.agent.config['environment'], 'development')

    def test_config_loading(self):
        """Test loading configuration from file."""
        # Test with non-existent file
        agent = AkashAgent("nonexistent.json")
        self.assertEqual(agent.config['environment'], 'development')

    @patch('akash_agent.time.sleep')
    def test_validate_infrastructure_success(self, mock_sleep):
        """Test successful infrastructure validation."""
        result = self.agent.validate_infrastructure()
        self.assertTrue(result)
        # Should have called sleep for AWS connectivity check
        mock_sleep.assert_called()

    @patch('akash_agent.time.sleep')
    def test_deploy_application_success(self, mock_sleep):
        """Test successful application deployment."""
        with patch.object(self.agent, 'validate_infrastructure', return_value=True):
            result = self.agent.deploy_application("test-app", "1.0.0")
            self.assertTrue(result)

    def test_monitor_performance(self):
        """Test performance monitoring functionality."""
        metrics = self.agent.monitor_performance(duration=1)
        self.assertIsInstance(metrics, dict)
        self.assertIn('cpu_usage', metrics)
        self.assertIn('memory_usage', metrics)
        self.assertIn('start_time', metrics)
        self.assertIn('end_time', metrics)

    def test_get_status(self):
        """Test getting agent status."""
        status = self.agent.get_status()
        self.assertIsInstance(status, dict)
        self.assertEqual(status['agent_name'], 'Akash-Agent')
        self.assertIn('version', status)
        self.assertIn('status', status)

    @patch('akash_agent.time.sleep')
    def test_cleanup_resources_success(self, mock_sleep):
        """Test successful resource cleanup."""
        result = self.agent.cleanup_resources()
        self.assertTrue(result)

    def test_cpu_usage_simulation(self):
        """Test CPU usage simulation."""
        usage = self.agent._get_cpu_usage()
        self.assertIsInstance(usage, float)
        self.assertGreater(usage, 0)
        self.assertLess(usage, 100)

    def test_memory_usage_simulation(self):
        """Test memory usage simulation."""
        usage = self.agent._get_memory_usage()
        self.assertIsInstance(usage, float)
        self.assertGreater(usage, 0)
        self.assertLess(usage, 100)


class TestAkashAgentCLI(unittest.TestCase):
    """Test cases for the CLI interface."""

    def setUp(self):
        """Set up test fixtures."""
        self.agent = AkashAgent()

    @patch('builtins.print')
    def test_status_command(self, mock_print):
        """Test status command output."""
        # Simulate command line arguments
        with patch('sys.argv', ['akash_agent.py', 'status']):
            # We can't easily test main() without more complex mocking
            # So we'll test the underlying functionality
            status = self.agent.get_status()
            self.assertIsInstance(status, dict)


if __name__ == '__main__':
    # Configure test runner
    unittest.main(verbosity=2)