import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from mcp_server import MCPAcademicServer


class TestMCPAcademicServer(unittest.TestCase):
    def test_call_tool_academic_query_returns_jsonrpc(self):
        server = MCPAcademicServer()
        result = server.call_tool("academic_query", {"student_id": "SV2026001"})

        self.assertEqual(result["jsonrpc"], "2.0")
        self.assertEqual(result["server"], "vinuni-academic-mcp-server")
        self.assertEqual(result["tool"], "academic_query")
        self.assertEqual(result["result"]["status"], "SUCCESS")
        self.assertEqual(result["result"]["data"]["full_name"], "Nguyễn Văn An")

    def test_schedule_tool_schema_is_defined(self):
        from tools import TOOLS_SCHEMA

        tool = next((t for t in TOOLS_SCHEMA if t["name"] == "schedule_appointment"), None)
        self.assertIsNotNone(tool)
        props = tool["parameters"]["properties"]
        self.assertIn("student_id", props)
        self.assertIn("datetime_str", props)
        self.assertIn("advisor_name", props)
        self.assertIn("student_id", tool["parameters"]["required"])


if __name__ == "__main__":
    unittest.main()
