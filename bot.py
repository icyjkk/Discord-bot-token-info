import discord
from discord.ext import commands
import requests


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def getTokenInfo(token):

    cookies = {
        '__cuid': '564ce8c671d04c29988ef3bf5650a3ae',
        'amp_fef1e8': '1231c735-835b-458f-86b5-7ca59a8ff877R...1hh35rdtr.1hh35rint.3.0.3',
        '_gid': 'GA1.2.2106193160.1710344871',
        'cf_clearance': 'ofnjg1_QKFMsooB_dHSqXOsQF0aV.T3bplzeQjdjUKE-1710347647-1.0.1.1-Q9iN_BEEbDuzZaCudqipkN4ymxz9SXXij8XSS6ojyeSd7mfBXw.Km9cHOWtieYG7sR2w4seknQ3L5IaIrKvTJQ',
        '_ga': 'GA1.1.1912829170.1698755408',
        '_ga_RD6VMQDXZ6': 'GS1.1.1710354793.3.1.1710354807.0.0.0',
        '__cf_bm': 'IAlocBYcEU6ywoJg.iqJkeb1qWud28IAITfJQ1qIBmc-1710354943-1.0.1.1-6vLZdmxAE_tdFWkMQCZHzY13PrY_57wQs4FooLmEobq0X5r9x_hT7VRBc6yYU1bcANsRNrjG1oWGNeYh6K7kST_cbc6rN5rn75UM70Z7c24',
        '_ga_532KFVB4WT': 'GS1.1.1710347650.210.1.1710354997.20.0.0',
    }

    headers = {
        'authority': 'api.dexscreener.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '__cuid=564ce8c671d04c29988ef3bf5650a3ae; amp_fef1e8=1231c735-835b-458f-86b5-7ca59a8ff877R...1hh35rdtr.1hh35rint.3.0.3; _gid=GA1.2.2106193160.1710344871; cf_clearance=ofnjg1_QKFMsooB_dHSqXOsQF0aV.T3bplzeQjdjUKE-1710347647-1.0.1.1-Q9iN_BEEbDuzZaCudqipkN4ymxz9SXXij8XSS6ojyeSd7mfBXw.Km9cHOWtieYG7sR2w4seknQ3L5IaIrKvTJQ; _ga=GA1.1.1912829170.1698755408; _ga_RD6VMQDXZ6=GS1.1.1710354793.3.1.1710354807.0.0.0; __cf_bm=IAlocBYcEU6ywoJg.iqJkeb1qWud28IAITfJQ1qIBmc-1710354943-1.0.1.1-6vLZdmxAE_tdFWkMQCZHzY13PrY_57wQs4FooLmEobq0X5r9x_hT7VRBc6yYU1bcANsRNrjG1oWGNeYh6K7kST_cbc6rN5rn75UM70Z7c24; _ga_532KFVB4WT=GS1.1.1710347650.210.1.1710354997.20.0.0',
        'if-none-match': 'W/"472-PXqWUUviH6F/JJ/XNp2y2CsCiHs"',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://api.dexscreener.com/latest/dex/tokens/{token}',
        cookies=cookies,
        headers=headers,
    )

    response_dict = response.json()
    pair_info = response_dict['pairs'][0]

    # Extraer información adicional
    chain = pair_info['chainId']
    dex = pair_info['dexId']
    url = pair_info['url']
    pair_address = pair_info['pairAddress']
    symbol = pair_info['baseToken']['symbol']
    # name = pair_info['baseToken']['name']
    ca = pair_info['baseToken']['address']
    price_usd = pair_info['priceUsd']
    price_native = pair_info['priceNative']
    fdv = pair_info['fdv']
    liquidity_usd = pair_info['liquidity']['usd']
    volume_24h = pair_info['volume']['h24']
    price_change_24h = pair_info['priceChange']['h24']
    highest_price_24h = pair_info['priceRange']['h24']['high'] if 'priceRange' in pair_info else "N/A"
    lowest_price_24h = pair_info['priceRange']['h24']['low'] if 'priceRange' in pair_info else "N/A"
    market_cap = pair_info.get('marketCap', "N/A")
    image_url = pair_info['info']['imageUrl'] if 'info' in pair_info else None
    website_url = pair_info['info']['websites'][0]['url'] if 'info' in pair_info and 'websites' in pair_info['info'] else None
    twitter_url = next((s['url'] for s in pair_info['info']['socials'] if s['type'] == 'twitter'), None) if 'info' in pair_info and 'socials' in pair_info['info'] else None
    telegram_url = next((s['url'] for s in pair_info['info']['socials'] if s['type'] == 'telegram'), None) if 'info' in pair_info and 'socials' in pair_info['info'] else None

    return (chain, dex, url, symbol, ca, price_usd, price_native, fdv, liquidity_usd, volume_24h,
            price_change_24h, highest_price_24h, lowest_price_24h, market_cap, pair_address,
            image_url, website_url, twitter_url, telegram_url)

@bot.command()
async def token(ctx, parametro):
    (chain, dex, url, symbol, ca, price_usd, price_native, fdv, liquidity_usd, volume_24h,
     price_change_24h, highest_price_24h, lowest_price_24h, market_cap, pair_address,
     image_url, website_url, twitter_url, telegram_url) = getTokenInfo(parametro)

    # Crear un embed con toda la información relevante
    embed = discord.Embed(
        title=f"{symbol} Information",
        url=url,
        description=f"Details about the {symbol} token.",
        color=0x7289DA
    )

    # Añadir campos con la información
    # embed.add_field(name="Token Name", value=name, inline=True)
    embed.add_field(name="Symbol", value=symbol, inline=True)
    embed.add_field(name="Chain", value=chain, inline=True)
    embed.add_field(name="DEX", value=dex, inline=True)
    embed.add_field(name="Contract Address", value=ca, inline=False)
    embed.add_field(name="Price (USD)", value=f"${price_usd}", inline=True)
    embed.add_field(name="Price (Native)", value=f"{price_native}", inline=True)
    embed.add_field(name="FDV (Fully Diluted Valuation)", value=f"${fdv:,}", inline=True)
    embed.add_field(name="Liquidity (USD)", value=f"${liquidity_usd:,}", inline=True)
    embed.add_field(name="Volume 24h (USD)", value=f"${volume_24h:,}", inline=True)
    embed.add_field(name="Price Change (24h)", value=f"{price_change_24h:.2f}%", inline=True)
    embed.add_field(name="Highest Price (24h)", value=f"${highest_price_24h}", inline=True)
    embed.add_field(name="Lowest Price (24h)", value=f"${lowest_price_24h}", inline=True)
    embed.add_field(name="Market Cap", value=f"${market_cap}", inline=True)
    embed.add_field(name="Pair Address", value=pair_address, inline=False)
    embed.add_field(name="Links", value=f"[BirdEye](https://birdeye.so/token/{ca}) | [DEX](https://dexscreener.com/solana/{ca})", inline=False)
    
    # Añadir enlaces adicionales si están disponibles
    if website_url:
        embed.add_field(name="Website", value=f"[Official Website]({website_url})", inline=False)
    if twitter_url:
        embed.add_field(name="Twitter", value=f"[Twitter]({twitter_url})", inline=False)
    if telegram_url:
        embed.add_field(name="Telegram", value=f"[Telegram]({telegram_url})", inline=False)

    # Añadir la imagen del token si está disponible
    if image_url:
        embed.set_thumbnail(url=image_url)

    # Enviar el embed al canal
    await ctx.send(embed=embed)

# Inicia el bot con el token de tu aplicación de Discord
bot.run(' ')
