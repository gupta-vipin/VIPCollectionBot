def start(bot, update):
    message = (
        "Hi, I'm VIPCollectionBot! \n"
        "These are my skills:\n\n"
        "/pelicula - Gives Movie Details\n"
        "/serie - Gives TV Series Details with Torrent Link\n"
        "/yts - Return YTS Random Torrent\n"
        "/snippets - Code snippets / troubleshooting / anything\n"
        "/cartelera - Most popular movies on theaters\n"
        "If you find any bug or suggestion, you can send it through /feedback\n"
        "I'm also open source so you can see how i work with /code"
    )
    update.message.reply_text(message, parse_mode='markdown', disable_web_page_preview=True)
