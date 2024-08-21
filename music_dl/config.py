#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: HJK
@file: config.py
@time: 2019-01-27

全局变量

"""

__all__ = ["init", "set", "get"]


def init():
    global opts
    opts = {
        # 自定义来源 -s --source
        "source": "baidu netease qq kugou",
        # 自定义数量 -n --number
        "number": 5,
        # 保存目录 -o --outdir
        "outdir": ".",
        # 搜索关键字 -k --keyword
        "keyword": "",
        # 从URL下载 -u --url
        "url": "",
        # 下载歌单 -p --playlist
        "playlist": "",
        # 代理 -x --proxy
        "proxies": None,
        # 显示详情 -v --verbose
        "verbose": False,
        # 搜索结果不排序去重 --nomerge
        "nomerge": False,
        # 下载歌词 --lyrics
        "lyrics": False,
        # 下载封面 --cover
        "cover": False,
        # 一般情况下的headers
        "fake_headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  # noqa
            "Accept-Charset": "UTF-8,*;q=0.5",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "en-US,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",  # noqa
            "referer": "https://www.google.com",
        },
        # QQ下载音乐不能没有User-Agent
        # 百度下载音乐User-Agent不能是浏览器
        # 下载时的headers
        "wget_headers": {
            "Accept": "*/*",
            "Accept-Encoding": "identity",
            "User-Agent": "Wget/1.19.5 (darwin17.5.0)",
        },
        # 移动端useragent
        "ios_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46"
        + " (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
        "netease_cookies": {
            "ntes_kaola_ad": "1",
            "JSESSIONID-WYYY": "eHCk5XgoikQlFshz8khzVZiO6Ya9zqpSMtfwZm9v/ETRInDIpZAZpyX5RGDViAtlpAlKHiebA1+HHamZWo1q8MvXN/IfTUgCK4I7H1xNGvcDK82yS29GVYjKokE2mkSj5UOvJBe9Qm0bd5SWORorw3eiZH9canKb00UiCY+38odsX3j7:A1724229385768",
            "_iuqxldmzr_": "32",
            "ntes_utid": "tid._.XN%2FEvqXpcx9FEgEBBBfTAzpNo1rfDFhM._.0",
            "WM_NI": "o47NzAWjYtxlp22LAe1jVsmL9KjmEB9WaY9xDv3GEfkeVaOyuCC5YGTBW91sh8MEjb7I6ZCVMTOR/U+klsw4jZZnTiImg48zf9yOG0lVjRzRlaC3ADOk50PY4mOX8K5ZY1I=",
            "WM_NIKE": "9ca17ae2e6ffcda170e2e6eea7b43c9395aad8d433b09e8ea6c54b838e9ab1c74bbbeb86dab47e8eb3a4affb2af0fea7c3b92aadecf9aff94b95b69795fb68b4eefeadc46ff3b69a94f048fb95a68ec84afb89afbabc7488aafda8c86ea9bb9a82ce73b79d8dd6dc4d989e99dab479ace883a6e96af597fabbc25e8f8c81b3ae5fe9b5a494f640aa86968fd7638bb3a9d5bb72a6e7b7b0c63cb08aa6b3f95ab0bf8dd4c4508db5fbd1d353f8b381b9bb41f78697d2cc37e2a3",
            "WM_TID": "2SSzx6KqGPVARQVRBFLGRz5dshrc3xNh",
            "_ntes_nnid": "0d6d64142bf6f6baa4a24dbf606a5ae9,1724208357683",
            "_ntes_nuid": "0d6d64142bf6f6baa4a24dbf606a5ae9",
            "MUSIC_U": "0017FEF491070425CB60279184B0D50B8E33D582882818FCBA70BCB93955C43812945DF2EE6D2FAA4D9A27E85E3C443DF35ADE805B4E7F59B74E5AF12B42091B1137A93D4E3A951864B015222E8E7C22CE23D6A96DC07CE6D031EC315E76848DE2BFDE1731AF82E582B32A24A5A2BD61471754BC1851A67A348CD24527A3E0EEB0EC1556CB13E06534EADD52AB49090282C125B692683ECF35CAD4B40AF3C74AE002FD0D12AABBF825EEC1DD2E612637EDF3760A4C8032DFAA69079C446901DCF7EB73AB2C47C25F29F77369B92BF376679A24BB390A2C7E601DE5ED5D41054F7EF610B9F3EE0AEA2C0FE01C581A5CF14A6546E0457F91FB17D384520065EC983465FA51A7E0A4EAF8C8A49B6D93055035C62BD15CC86F32966238B8D9143BE09DBFE735F7D665AD514DFED3FF919CC5E65BAFE47EB6482D827A7E3323EA918CDAEFDED33ADDB40F9CDF0E9919F52A5A55ECB80EBDA34BED920384EA499018E336",
            "__csrf": "e650d40be260b6aff1b3be4ec539568e",
            "__remember_me": "true",
            "sDeviceId": "YD-KIH8e6AXcGxFQ0QBFEOTQaGU8blqAa1y",
            "NMTID": "00OBSB1B22vWKcUfEbUs7GK6hkwr9IAAAGQyM5ZwQ"
        }
    }


def get(key):
    return opts.get(key, "")


def set(key, value):
    opts[key] = value
