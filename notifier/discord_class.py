from discord_webhook import DiscordWebhook, DiscordEmbed


class Discord(object):
  def __init__(self, webhook_url, manual_call=False):
    self.webhook_url = webhook_url
    self.webhook = DiscordWebhook(url=webhook_url)
    self.error_img = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/linux/error.png'
    self.success_img = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/linux/success.png'
    self.logo = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/logo.png'
    if manual_call:
      self.description = 'Message:'
    else:
      self.description = 'Your function finished sucessfully with this result:'
  def send_message(self, title='', description='', error=None, start=None, end=None):
    color = '44AA00'

    if error is not None:
      color = 'BB250C'
    if description is not None and error is None:
      description = f'{self.description}\n```{description}```'
    elif description is None and error is None:
      description = f'{self.description}\n```{None}```'
    elif description is None and error is not None:
      description = 'Your function finished with this error:\n```{}```'.format(error)

    embed = DiscordEmbed(title=title, description=description, color=color)
    #embed.set_image(url=img_msg)
    #embed.set_thumbnail(url=img_msg)
    #embed.set_footer(text='Notify function')
    #embed.set_timestamp()
    if start is not None and end is not None:
      delta = end - start
      embed.add_embed_field(name='Start time', value=start.strftime('%H:%M:%S'))
      embed.add_embed_field(name='End time', value=end.strftime('%H:%M:%S'))
      embed.add_embed_field(name='Elapsed time', value=f'{delta}')

    embed.set_author(name='Notify Function', url='https://github.com/enmanuel-mag', icon_url=self.logo)

    self.webhook.add_embed(embed)
    self.webhook.execute()
