""" Tests for updating a configuration object's genome_servers section """

import pytest
from refgenconf.const import *


class TestUpdateServers:
    @pytest.mark.parametrize("urls", ["www.new_url.com"])
    def test_add_basic(self, my_rgc, urls):
        my_rgc.update_genome_servers(url=urls)
        assert urls in my_rgc[CFG_SERVERS_KEY]

    @pytest.mark.parametrize("urls", [1, ["a", 1]])
    def test_faulty_url(self, my_rgc, urls):
        with pytest.raises(TypeError):
            my_rgc.update_genome_servers(url=urls)

    @pytest.mark.parametrize("urls", [["www.new_url.com", "www.url.pl"]])
    def test_multiple_urls(self, my_rgc, urls):
        my_rgc.update_genome_servers(url=urls)
        assert urls[0] in my_rgc[CFG_SERVERS_KEY] and \
               urls[1] in my_rgc[CFG_SERVERS_KEY]

    @pytest.mark.parametrize("urls", [["www.new_url.com", "www.new_url.com"]])
    def test_uniqueness(self, my_rgc, urls):
        ori_len = len(my_rgc[CFG_SERVERS_KEY])
        my_rgc.update_genome_servers(url=urls)
        assert len(my_rgc[CFG_SERVERS_KEY]) == ori_len + 1

    @pytest.mark.parametrize("urls", [["www.new_url.com", "www.new_url.com"]])
    def test_reset(self, my_rgc, urls):
        my_rgc.update_genome_servers(url=urls, reset=True)
        assert len(my_rgc[CFG_SERVERS_KEY]) == 1
