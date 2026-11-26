import base64
H='/home/claude/qui-offre-a-qui/tools/fonts/'
def u(n): return 'data:font/woff2;base64,'+base64.b64encode(open(H+n,'rb').read()).decode()
CSS=f"""@font-face{{font-family:'Bricolage Grotesque';font-weight:500 800;src:url({u('bricolage-grotesque-latin-800-normal.woff2')}) format('woff2')}}
@font-face{{font-family:'Atkinson Hyperlegible';font-weight:400;src:url({u('atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}
@font-face{{font-family:'Atkinson Hyperlegible';font-weight:700;src:url({u('atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"""
def route(ctx):
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=CSS))
    ctx.route('**/pagead2.googlesyndication.com/**', lambda r: r.fulfill(status=200, content_type='application/javascript', body=''))
