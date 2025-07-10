<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>rune</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 800px;
      margin: 2rem auto;
      padding: 0 1.5rem;
      background: #fff;
      color: #24292f;
    }
    h1, h2, h3 {
      border-bottom: 1px solid #e1e4e8;
      padding-bottom: 0.3em;
      margin-top: 2em;
    }
    pre, code {
      font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
      background-color: #f6f8fa;
      padding: 0.2em 0.4em;
      border-radius: 6px;
    }
    pre {
      padding: 1em;
      overflow-x: auto;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 1em;
    }
    th, td {
      border: 1px solid #d0d7de;
      padding: 6px 13px;
    }
    th {
      background-color: #f6f8fa;
      text-align: left;
    }
    a {
      color: #0969da;
      text-decoration: none;
    }
  </style>
</head>
<body>

<h1>🧱 rune</h1>
<p><strong>rune</strong> is a message scripting engine for Discord bots.</p>
<p>It parses a block of text, replaces variables, and turns it into an embed with optional buttons.<br>
No GUI. No builder. Just script → message.</p>

<h2>▶ Example</h2>
<pre><code>{content:welcome, {user.name}}
{title:infrared online}
{description:this server runs cold}
{color:#ED1C24}
{author:Pusha && https://i.imgur.com/pusha.png}
{field:Rank && King && inline}
{footer:real bars only && https://i.imgur.com/footer.png}
{button:enter && 🚪 && https://infrared.zone && red}
{timestamp}</code></pre>

<h2>✅ Supported Fields</h2>
<p>All fields are optional. Missing or invalid values are ignored.</p>

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Format</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>content</code></td><td><code>{content:text}</code></td></tr>
    <tr><td><code>title</code></td><td><code>{title:text}</code></td></tr>
    <tr><td><code>description</code></td><td><code>{description:text}</code></td></tr>
    <tr><td><code>color</code></td><td><code>{color:#hex}</code></td></tr>
    <tr><td><code>author</code></td><td><code>{author:Name && Icon && URL}</code></td></tr>
    <tr><td><code>footer</code></td><td><code>{footer:Text && Icon}</code></td></tr>
    <tr><td><code>field</code></td><td><code>{field:Name && Value && inline}</code></td></tr>
    <tr><td><code>button</code></td><td><code>{button:Label && Emoji && URL && Style}</code></td></tr>
    <tr><td><code>timestamp</code></td><td><code>{timestamp}</code></td></tr>
  </tbody>
</table>

<h2>🔀 Variables</h2>
<p>Variables are replaced in any field:</p>
<pre><code>{user.name}       {user.id}         {user.avatar}
{guild.name}      {guild.id}         {guild.owner}
{target.name}     {target.id}        {target.avatar}
...</code></pre>

<h2>🧪 Bot Usage</h2>
<pre><code>from rune import Rune

@bot.command()
async def rune(ctx, *, script: str):
    r = Rune(script, ctx.author)

    await ctx.send(
        content=r.content,
        embed=r.render(),
        view=r.view()
    )</code></pre>

<p>If the script defines nothing, <code>r.content</code>, <code>r.render()</code>, and <code>r.view()</code> all return <code>None</code>.</p>

<h2>📁 Structure</h2>
<pre><code>rune/
├── engine.py     # core logic
├── blocks.py     # components
├── inject.py     # variable replacement
├── utils.py      # helpers
├── __init__.py   # exports Rune
</code></pre>

<h2>⚙️ Install</h2>
<pre><code>pip install -e .</code></pre>
<p>Or just copy the <code>rune/</code> folder into your bot project.</p>

<h2>✸</h2>
<p>You write the script. <code>rune</code> formats it.</p>
<p>No templates. No editors. Just bars.</p>

</body>
</html>
