from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()


async def main():
    r = await asession.get("https://fex.net")
    await r.html.arender()
    title = r.html.text
    print(title)


asession.run(main)
