<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>rune</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      line-height: 1.6;
      max-width: 720px;
      margin: 2rem auto;
      padding: 0 1rem;
      color: #ddd;
      background: #0f0f0f;
    }
    h1, h2, h3 {
      color: #fff;
    }
    code {
      background: #1a1a1a;
      padding: 0.2em 0.4em;
      border-radius: 4px;
      color: #f94f4f;
      font-family: monospace;
    }
    pre {
      background: #1a1a1a;
      padding: 1em;
      border-radius: 6px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0;
      font-size: 0.95em;
    }
    th, td {
      padding: 0.5em;
      border: 1px solid #444;
    }
    th {
      background: #222;
      color: #ccc;
      text-align: left;
    }
    a {
      color: #f94f4f;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

<h1>rune</h1>
<p><strong>rune</strong> is a message scripting engine for Discord bots.</p>
<p>It parses a block of text, replaces variables, and turns it into an embed with optional buttons. No GUI. No builder. Just script → message.</p>

<h2>Example</h2>
<pre><code>{content:welcome, {user.name}}
{title:infrared online}
{description:this server runs cold}
{color:#ED1C24}
{author:Pusha && https://i.imgur.com/pusha.png}
{field:Rank && King && inline}
{footer:real bars only && https://i.imgur.com/footer.png}
{button:enter && 🚪 && https://infrared.zone && red}
{timestamp}</code></pre>

<h2>Supported Fields</h2>
<p>All optional. Any invalid/missing ones are ignored.</p>
<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Format</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>content</td><td><code>{content:text}</code></td></tr>
    <tr><td>title</td><td><code>{title:text}</code></td></tr>
    <tr><td>description</td><td><code>{description:text}</code></td></tr>
    <tr><td>color</td><td><code>{color:#hex}</code></td></tr>
    <tr><td>author</td><td><code>{author:Name && Icon && URL}</code></td></tr>
    <tr><td>footer</td><td><code>{footer:Text && Icon}</code></td></tr>
    <tr><td>field</td><td><code>{field:Name && Value && inline}</code></td></tr>
    <tr><td>button</td><td><code>{button:Label && Emoji && URL && Style}</code></td></tr>
    <tr><td>timestamp</td><td><code>{timestamp}</code></td></tr>
  </tbody>
</table>

<h2>Available Variables</h2>
<p>Any string can use these placeholders:</p>
<pre><code>{user.name}         {user.id}          {user.avatar}
{guild.name}        {guild.id}         {guild.owner}
{target.name}       {target.id}        ...</code></pre>

<h2>Bot Usage</h2>
<pre><code>from rune import Rune

@bot.command()
async def rune(ctx, *, script: str):
    r = Rune(script, ctx.author)

    await ctx.send(
        content=r.content,
        embed=r.render(),
        view=r.view()
    )</code></pre>

<p>If the script defines nothing, everything returns <code>None</code>. No checks needed.</p>

<h2>Structure</h2>
<pre><code>rune/
├── engine.py     # core logic
├── blocks.py     # components
├── inject.py     # var replacement
├── utils.py      # text helpers
├── __init__.py   # exports Rune
</code></pre>

<h2>Install</h2>
<pre><code>pip install -e .</code></pre>
<p>Or just copy the <code>rune/</code> folder.</p>

<h2 style="margin-top: 2em;">✸</h2>
<p>You write the script. <code>rune</code> formats it.</p>
<p>No templates. No editors. Just bars.</p>

</body>
</html>
