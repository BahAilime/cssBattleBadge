# CSSBattle.dev Badge

A simple web app to generate a badge for your CSSBattle.dev stats.

## Usage
https://css-battle-badge.vercel.app/badge/?id=5tYbW8kVmGO2qbk0u14n1XLFWSU2&username=HAHAHA

1. Go to [css-battle-badge.now.sh/badge](https://css-battle-badge.now.sh/badge)
2. Set the `id` parameter to your CSSBattle.dev user ID.
3. Optionally, set the `username` parameter to your CSSBattle.dev username.
4. The app will generate a SVG badge for your stats.

## How to get your id

1. Go on your CSSBattle.dev profile.
2. Use the page source button from your browser or use the `Ctrl + U` shortcut.
3. Search for `data-userid="` in the page source.
4. Copy the value between the quotes.

## Example

```md
[![CSSBattle.dev](https://css-battle-badge.vercel.app/badge/?id=GFhoaJX4SFgdWOBXdWUee4jsaNq2&username=Emilia)](https://cssbattle.dev/player/ailime)
```

```html
<a href="https://cssbattle.dev/player/ailime" target="_blank"><img src="https://css-battle-badge.vercel.app/badge/?id=GFhoaJX4SFgdWOBXdWUee4jsaNq2&username=Emilia" height="250"/></a>
```

[![CSSBattle.dev](https://css-battle-badge.vercel.app/badge/?id=GFhoaJX4SFgdWOBXdWUee4jsaNq2&username=Emilia)](https://cssbattle.dev/player/ailime)

## You can use this basic badge generator (at /badge/)

[![Url generator](/static/generator.png)](https://css-battle-badge.vercel.app/badge/)
[Badge Generator](https://css-battle-badge.vercel.app/badge/)

## Development

1. Clone the repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run the app with `python main.py`.
4. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Deployment

The app is deployed to [Vercel](https://vercel.com/).

<!-- 
## Star History

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://api.star-history.com/svg?repos=BahAilime/cssBattleBadge&type=Date&theme=dark
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://api.star-history.com/svg?repos=BahAilime/cssBattleBadge&type=Date
    "
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=BahAilime/cssBattleBadge&type=Date"
  />
</picture> -->