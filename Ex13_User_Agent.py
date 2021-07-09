import pytest
import requests

class TestUserAgent:
    headers_and_expected_results = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mobile", "No", "Android"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Unknown", "Googlebot", "Unknown"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", "Web", "Chrome", "No"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "Mobile", "No", "iPhone")
    ]

    @pytest.mark.parametrize('agent, platform, browser, device', headers_and_expected_results)
    def test_user_agent(self, agent, platform, browser, device):
        key_agent = "user_agent"
        key_platform = "platform"
        key_browser = "browser"
        key_device = "device"
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"user-agent": agent}

        response = requests.get(url, headers=headers)

        assert response.status_code == 200, "Response code is not 200"
        assert response.json()[key_agent] == agent, "Agent from response is not equal to expected one"
        assert response.json()[key_platform] == platform,"Platform from response is not equal to expected one"
        assert response.json()[key_browser] == browser, "Browser from response is not equal to expected one"
        assert response.json()[key_device] == device, "Device from response is not equal to expected one"

