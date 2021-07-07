from ..treat_data import separate


def render_quotes(number, words_to_highlight) -> str:
    print("QUOTES:\nPlease type 2 of your favourite quotes from the album.\n(to end a quote type 'e')")
    all_quotes = []
    for i in range(number):
        quote = get_quote(i)
        quote["quote"] = process_quote(quote["quote"], words_to_highlight)
        all_quotes.append(quote)
    html = f"""
<div class="quotes">
    {generate_quote_html(all_quotes)}
</div>
    """
    return html


def generate_quote_html(all_quotes: list) -> str:
    inner = ""
    for i in range(len(all_quotes)):
        quote = all_quotes[i]
        inner += f"""
<p>
    <strong>Quote {i+1} :</strong>
    {quote["quote"]}
    <em>({quote["artist"]} - {quote["track"]})</em>
</p>
        """

    return inner


def process_quote(quote: str, words_to_highlight: list) -> str:
    for i in range(len(words_to_highlight)):
        word = words_to_highlight[i][0].title()
        quote = quote.replace(word+" ", f'<mark class="m{i+1}">{word} </mark>')
    return quote


def get_quote(index: int) -> list:
    print("-- Quote ", index+1, " --")
    quote = ""
    while True:
        verse = input("Verse : ")
        verse = verse.title()
        if verse == "E":
            break
        else:
            quote += verse + " <br/>"
    artist = input("Artist: ")
    track = input("Track: ")
    return {
        "quote": quote,
        "artist": artist,
        "track": track
    }
